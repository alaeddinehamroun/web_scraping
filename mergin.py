import pandas as pd

f1 = pd.read_csv("/home/alaeddine/Desktop/web_scraping/pcs_tunisianet.csv")
f2 = pd.read_csv("/home/alaeddine/Desktop/web_scraping/pcs_mytek.csv")

f1["price_mytek"] = ""
f1["availability_mytek"] = ""
f1["link_mytek"] = ""
# comm = f2.reference.isin(f1.reference)
# for (reference, i) in zip(f1["reference"], comm):
#     if i:
#         f1.loc["i"] = i

# print(f1)
comm = f1.reference.isin(f2.reference)
for index,row in f1[comm].iterrows():
    f1._set_value(index, "price_mytek", f2.loc[f2["reference"] == row["reference"]].values[0][-2])
    f1._set_value(index, "availability_mytek", f2.loc[f2["reference"] == row["reference"]].values[0][-1])
    f1._set_value(index, "link_mytek", f2.loc[f2["reference"] == row["reference"]].values[0][1])
    # if (row["reference"].isin(f2.reference)):
        
    #     print(f2.loc[f2['reference'] == row["reference"]].to_string())

f1.to_csv("/home/alaeddine/Desktop/web_scraping/merge.csv")
