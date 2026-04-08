import pandas as pd

df = pd.read_csv("C:/Users/HP/Documents/SQL Python projects/electronics-analysis/dirty.csv")
print(df)

print(df .head())

print(df .info())
print(df .isnull() .sum())

df["Product"] = df["Product"].str.strip()
df["Region"] = df["Region"].str.strip()

df["Product"] = df["Product"].str.title()
df["Region"] = df["Region"].str.title()


df["Region"] = df["Region"].replace({
    "Kzn": "KZN",
    "Western cape": "Western Cape"
})


df["Amount"] = df["Amount"].fillna(df["Amount"].mean())
df["Region"] = df["Region"].fillna("Unknown")


df["Date"] = pd.to_datetime(df["Date"])
df["Amount"] = df["Amount"].astype(float)


sales_by_region = df.groupby("Region")["Amount"].sum()
print(sales_by_region)