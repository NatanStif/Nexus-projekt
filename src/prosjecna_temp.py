import pandas as pd


df_lokacije = pd.read_csv("data/mars_lokacije.csv", sep = ";", decimal = ",")
df_uzorci = pd.read_csv("data/mars_uzorci.csv", sep = ";", decimal = ",")


df_spojeno = pd.merge(
    df_lokacije,
    df_uzorci,
    on="ID_Uzorka")


df_filtrirano = df_spojeno[df_spojeno["Temp_Tla_C"] < 150]
prosjek = df_filtrirano["Temp_Tla_C"].mean()


print(f"Prosjek = {round(prosjek,2)}°C")
