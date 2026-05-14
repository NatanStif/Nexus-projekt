import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import json
import requests

df_lokacije = pd.read_csv("data/mars_lokacije.csv", sep = ";", decimal = ",")
df_uzorci = pd.read_csv("data/mars_uzorci.csv", sep = ";", decimal = ",")
