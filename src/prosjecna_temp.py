import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import requests


df_lokacije = pd.read_csv("data/mars_lokacije.csv", sep = ";", decimal = ",")
df_uzorci = pd.read_csv("data/mars_uzorci.csv", sep = ";", decimal = ",")

df_spojeno = pd.merge(
    df_lokacije,
    df_uzorci,
    on="ID_Uzorka")


df_filtrirano = df_spojeno[df_spojeno["Temp_Tla_C"] < 150]
ukupna_temp = 0


for i in range(0,len(df_filtrirano)):
    ukupna_temp += df_filtrirano["Temp_Tla_C"][i]


print(ukupna_temp/len(df_filtrirano))
