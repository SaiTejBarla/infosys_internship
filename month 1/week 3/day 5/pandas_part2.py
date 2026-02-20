import pandas as pd

df = pd.read_csv(r"C:\Users\SaiTej Barla\OneDrive\Desktop\infosys\month 1\week 3\day 3 and 4\India_Car_Sales_2025_Dataset.csv")

print(df.head())
df.columns = df.columns.str.replace('"' , '').str.strip()
print(df.columns)

df.shape

df.columns

df.info()

df.describe()

df['Brand']

df.iloc[0]

df.iloc[0:4]

