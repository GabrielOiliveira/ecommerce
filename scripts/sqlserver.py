import pandas as pd
import pyodbc

df = pd.read_csv("data/ecom_data.csv")

df = df.drop_duplicates()
df = df.dropna()

df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])
df["Valor_Total"] = df["Valor_Unitario"] * df["Quantidade"]

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=EcommerceDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO vendas (
            ID_Transacao, Data_Venda, ID_Cliente,
            Nome_Produto, Categoria_Produto,
            Valor_Unitario, Quantidade, Valor_Total
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    int(row.ID_Transacao),
    row.Data_Venda,
    int(row.ID_Cliente),
    row.Nome_Produto,
    row.Categoria_Produto,
    float(row.Valor_Unitario),
    int(row.Quantidade),
    float(row.Valor_Total)
    )

conn.commit()
conn.close()

print("ETL finalizado!")