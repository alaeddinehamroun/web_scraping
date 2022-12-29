import pandas as pd

f1 = pd.read_csv("/home/alaeddine/Desktop/web_scraping/pcs_tunisianet.csv")
f2 = pd.read_csv("/home/alaeddine/Desktop/web_scraping/pcs_mytek.csv")

print(f2[f2.reference.isin(f1.reference)].to_string())
