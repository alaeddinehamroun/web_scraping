import pandas as pd
f1 = pd.read_csv("/home/alaeddine/Desktop/web_scraping/merged.csv")

Dup_Rows = f1[f1.duplicated("reference")]


print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))


f1 = f1.drop_duplicates(subset=['reference'], keep='first')
f1.to_csv("/home/alaeddine/Desktop/web_scraping/merged.csv")