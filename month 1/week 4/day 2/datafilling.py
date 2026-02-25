import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\SaiTej Barla\OneDrive\Desktop\infosys\India_Car_Sales_2025_Dataset.csv")

df.loc[2, 'Price'] = None

df.isnull().sum()

df.fillna(df.mean(numeric_only = True ,inplace=True))

print(df)

df.dropna(inplace=True)