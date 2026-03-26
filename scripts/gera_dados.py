import pandas as pd
import random
from datetime import datetime, timedelta

produtos = ["Teclado", "Mouse", "Monitor", "Headset", "Notebook"]
categorias = ["Periféricos", "Periféricos", "Hardware", "Áudio", "Hardware"]

dados = []

for i in range(5000):
    data_venda = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
    idx = random.randint(0, len(produtos)-1)

    dados.append({
        "ID_Transacao": i,
        "Data_Venda": data_venda,
        "ID_Cliente": random.randint(1, 1000),
        "Nome_Produto": produtos[idx],
        "Categoria_Produto": categorias[idx],
        "Valor_Unitario": round(random.uniform(50, 5000), 2),
        "Quantidade": random.randint(1, 5)
    })

df = pd.DataFrame(dados)

df.loc[10, "Valor_Unitario"] = None
df = pd.concat([df, df.iloc[:5]])

df.to_csv("data/ecom_data.csv", index=False)

print("Dataset criado!")