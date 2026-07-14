import pandas as pd
df = pd.read_csv("Date.csv")
print("Number of rows:", len(df))
print("Mean price:", df["price"].mean())