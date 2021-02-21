# Adım 1 - RFM Analizi
# RFM Analizi Müşterileri Segmente etmeye yarayan yöntemlerden biridir.
# Bu projede Online Retail veriseti kullanılacak olup sadece Almanya müşterilerinden oluşan grup segmente edilecek.

# Kütüphaneler
import pandas as pd
import datetime as dt
import pickle

# Veri Setinin Yüklenmesi
df = pd.read_csv("online-retail-germany.csv", sep=";")
