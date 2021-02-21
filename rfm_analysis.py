# Adım 1 - RFM Analizi
# RFM Analizi Müşterileri Segmente etmeye yarayan yöntemlerden biridir.
# Bu projede Online Retail veriseti kullanılacak olup sadece Almanya müşterilerinden oluşan grup segmente edilecek.

# Kütüphaneler
import pandas as pd
import datetime as dt

###########################################
# Veri Setinin Yüklenmesi
###########################################
df = pd.read_csv("online-retail-germany.csv", sep=";")

###########################################
# Veri Ön İşleme
###########################################

# InvoiceDate dönüşümü
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# İadeleri çıkarma
df = df[~(df["Invoice"].astype(str).str.contains("C"))]

# Fatura numaraları alfanumerik olmayan faturaları çıkarma
df = df[~(df["Invoice"].astype(str).str.isalpha())]

# Eksik değerlere ait gözlemleri silme
df.dropna(inplace=True)

# Toplam ücreti hesaplama
df["TotalPrice"] = df["Quantity"] * df["Price"]

# Customer ID dönüşümü
df["Customer ID"] = df["Customer ID"].astype(int).astype(str)

# RFM Tablosunun Oluşturulması
today_date = dt.datetime(2011, 12, 11)
rfm = df.groupby('Customer ID').agg({'InvoiceDate': lambda date: (today_date - date.max()).days,
                                     'Invoice': lambda num: len(num),
                                     'TotalPrice': lambda TotalPrice: TotalPrice.sum()})

rfm.columns = ['Recency', 'Frequency', 'Monetary']
rfm = rfm[(rfm["Monetary"]) > 0 & (rfm["Frequency"] > 0)]

# RFM Skorlarının Belirlenmesi
rfm["RecencyScore"] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["FrequencyScore"] = pd.qcut(rfm['Frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm["MonetaryScore"] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
rfm["RFM_SCORE"] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str) + rfm['MonetaryScore'].astype(str)

# RFM Segmentlerinin isimlendirilmesi
seg_map = {
    r'[1-2][1-2]': 'Hibernating',
    r'[1-2][3-4]': 'At_Risk',
    r'[1-2]5': 'Cant_Loose',
    r'3[1-2]': 'About_to_Sleep',
    r'33': 'Need_Attention',
    r'[3-4][4-5]': 'Loyal_Customers',
    r'41': 'Promising',
    r'[4-5][2-3]': 'Potential_Loyalists',
    r'51': 'New_Customers',
    r'5[4-5]': 'Champions'
}

rfm['Segment'] = rfm['RecencyScore'].astype(str) + rfm['FrequencyScore'].astype(str)
rfm['Segment'] = rfm['Segment'].replace(seg_map, regex=True)
rfm = rfm[['Recency', 'Frequency', 'Monetary', 'Segment']]
rfm.reset_index(inplace=True)

pd.to_pickle(rfm,"rfm_table.pkl")

rfm_statistics = rfm[["Segment", "Recency", "Frequency", "Monetary"]].groupby("Segment").agg({"Recency": "mean", "Frequency": "mean", "Monetary": ["mean", "count"]})
rfm_statistics.columns = ["_".join(x) for x in rfm_statistics.columns.ravel()]
rfm_statistics.reset_index(inplace=True)

pd.to_pickle(rfm_statistics,"rfm_statistics.pkl")