import matplotlib as plt
import pandas as pd
import os

df = pd.read_csv("data/transactions_oct_25.csv")
header = df.iloc[2, 1:]
df = df.iloc[3:, 1:]
df = pd.DataFrame(df.values, columns=header)
df.columns.name = None

print(df.head())

print(f"\n{df.describe()}")