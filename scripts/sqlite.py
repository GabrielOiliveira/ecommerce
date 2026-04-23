import os
import sqlite3
import pandas as pd

os.makedirs("database", exist_ok=True)

df = pd.read_csv("data/ecom_data.csv")

df = df.drop_duplicates()
df = df.dropna()

df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])
df["Valor_Total"] = df["Valor_Unitario"] * df["Quantidade"]

conn = sqlite3.connect("database/ecommerce.db")

df.to_sql("vendas", conn, if_exists="replace", index=False)

conn.close()

print("ETL finalizado com SQLite!")