# Adım 1 - RFM Analizi
# RFM Analizi Müşterileri Segmente etmeye yarayan yöntemlerden biridir.
# Bu projede Online Retail veriseti kullanılacak olup sadece Almanya müşterilerinden oluşan grup segmente edilecek.

# Kütüphaneler
import pandas as pd
import datetime as dt
import pickle

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