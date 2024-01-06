import pandas as pd
import numpy as np
import math 

    #Excel dosyasını oku ve DataFrame'e dönustur
df_excel = pd.read_excel("C:/Users/gokha/OneDrive/Masaüstü/Tez/9.1-Merec.xlsx")
maliyet = df_excel.iloc[0:1].copy()
df = df_excel.iloc[1:]
satir_sayisi = df.shape[0] 
sutun_sayisi = df.shape[1]

minmax = []
for i in range(sutun_sayisi):
    if maliyet.iloc[0, i] == "maliyet":
        minmax.append(df.iloc[:, i].max())  
    else:
        minmax.append(df.iloc[:, i].min())
            
mins = []
maxs = []
for i in range(sutun_sayisi):
        mins.append(df.iloc[:, i].min())  
        maxs.append(df.iloc[:, i].max())
        
normalize_df = df.copy()
for i in range(sutun_sayisi):
    if maliyet.iloc[0, i] == "fayda":
        normalize_df.iloc[:, i] = minmax[i] / df.iloc[:, i] 
    else:
        normalize_df.iloc[:, i] = df.iloc[:, i]  / minmax[i]

si = []
for i in range(satir_sayisi):
    toplam = 0
    for j in range(sutun_sayisi):
        toplam = toplam + abs(math.log(normalize_df.iloc[i, j]))
    si.append(math.log(1 + (1 / sutun_sayisi) * toplam))
      

decision_df = normalize_df.copy()
for g in range(satir_sayisi):
    for j in range(sutun_sayisi):
        toplam = 0
        for i in range(sutun_sayisi):
            toplam = toplam + (abs(math.log(normalize_df.iloc[g, i])))
        yeni_toplam = toplam - abs(math.log(normalize_df.iloc[g,j]))
        decision_df.iloc[g,j] = math.log(1 + ((1 / sutun_sayisi) * yeni_toplam))

e = []
for i in range(sutun_sayisi):
    e.append(sum(abs(decision_df.iloc[:,i] - si)))

agirliklar = []
for i in range(len(e)):
    agirliklar.append(e[i] / sum(e))

print(f"Agirliklar Sirasiyla: {agirliklar}")
