import pandas as pd
df = pd.read_csv("Date.csv")
print("Number of transactions:", len(df))
print("Mean transaction price:", df["price"].mean())
# Print the largest sale:
print("Largest transaction:", df["Price"].max())