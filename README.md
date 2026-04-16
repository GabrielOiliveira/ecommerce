# E-commerce Analytics Project

Desafio Final PD - Trilha de Dados

## Descrição

Este projeto tem como objetivo analisar dados de vendas de um e-commerce, aplicando técnicas de engenharia de dados, análise exploratória e modelagem preditiva.

O pipeline cobre todas as etapas:

- Geração de dados
- ETL (limpeza e transformação)
- Armazenamento em banco relacional (SQL Server)
- Análise exploratória (EDA)
- Visualização em dashboard (Power BI)
- Previsão de vendas com modelo de regressão

## Objetivos

- Entender o comportamento dos clientes
- Identificar produtos e categorias mais relevantes
- Analisar tendências de vendas
- Prever o faturamento futuro

## Tecnologias Utilizadas

- Python 3.13
- Pandas / NumPy
- Matplotlib / Plotly
- Scikit-learn
- PyODBC
- SQL Server Express
- SQL Server Management Studio (SSMS)
- Power BI

## Estrutura do Projeto

```
ecommerce/
│
├── data/
│   └── ecom_data.csv
│
├── scripts/
│   ├── gerar_dados.py
│   └── etl_sqlserver.py
│
├── sql/
│   └── queries.sql
│
├── notebooks/
│   ├── analise.ipynb
│   └── previsao.ipynb
│
├── dashboard/
│   ├── dashboard.pbix
│   └── imagens/
│
├── requirements.txt
└── README.md
```

## Dependências

Instale as dependências com:

```
pip install -r requirements.txt
```

Conteúdo do requirements.txt:

```
pandas
numpy
matplotlib
plotly
scikit-learn
pyodbc
faker
nbformat
```

## Pré-requisitos

Para executar o projeto completo, é necessário:

- Python 3.13
- SQL Server Express instalado
- SQL Server Management Studio (SSMS)
- ODBC Driver 17 for SQL Server
- Power BI Desktop

## Configuração do Banco de Dados

Importante: o script de ETL depende de configuração externa do SQL Server e não funciona em ambiente Python padrão sem essa preparação.

### Criar banco de dados

```
CREATE DATABASE EcommerceDB;
```

### Selecionar o banco

```
USE EcommerceDB;
```

### Criar tabela

```
CREATE TABLE vendas (
    ID_Transacao INT,
    Data_Venda DATE,
    ID_Cliente INT,
    Nome_Produto VARCHAR(100),
    Categoria_Produto VARCHAR(100),
    Valor_Unitario FLOAT,
    Quantidade INT,
    Valor_Total FLOAT
);
```

### Configurar conexão no Python

No arquivo etl_sqlserver.py:

```
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=EcommerceDB;"
    "Trusted_Connection=yes;"
)
```

Caso o nome do servidor seja diferente, ajuste o campo SERVER.

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone <url-do-repositorio>
cd ecommerce
```

### 2. Instalar dependências

```
pip install -r requirements.txt
```

### 3. Gerar dataset

```
python scripts/gerar_dados.py
```

Isso irá gerar o arquivo:

```
data/ecom_data.csv
```

### 4. Configurar o banco SQL Server

Antes de executar o ETL, é necessário:

- Banco EcommerceDB criado
- Tabela vendas criada
- SQL Server em execução
- Driver ODBC instalado

### 5. Executar ETL

```
python scripts/etl_sqlserver.py
```

O script realiza:

- Remoção de duplicados
- Remoção de valores nulos
- Conversão de datas
- Criação da coluna Valor_Total
- Inserção dos dados no banco

### 6. Executar análise

Abrir os notebooks:

- notebooks/analise.ipynb
- notebooks/previsao.ipynb

### 7. Abrir dashboard

Abrir o arquivo no Power BI:

```
dashboard/dashboard.pbix
```

## ETL

- Remoção de valores nulos
- Remoção de duplicados
- Conversão de datas
- Criação da coluna Valor_Total
- Carga no SQL Server

## Análise Exploratória (EDA)

- Faturamento total
- Ticket médio
- Volume de pedidos
- Vendas ao longo do tempo
- Faturamento por categoria
- Produtos mais vendidos
- Identificação de outliers
- Correlação entre variáveis

## Dashboard

O dashboard apresenta:

- KPIs principais
- Evolução das vendas
- Faturamento por categoria
- Produtos mais vendidos
- Filtros interativos

## Modelo Preditivo

Foi utilizado um modelo de regressão linear para prever vendas.

### Metodologia

- Agrupamento das vendas por mês
- Conversão da variável temporal em formato numérico
- Treinamento com Linear Regression

### Resultado

O modelo indica tendência de crescimento nas vendas ao longo do tempo.

## Insights

- Algumas categorias concentram maior faturamento
- Existe tendência de crescimento nas vendas
- Há variações mensais que podem indicar sazonalidade
- Produtos específicos dominam o resultado

## Limitações

- Dados simulados
- Modelo simples
- Não considera fatores externos
- Dependência de configuração do SQL Server

## Conclusão

O projeto demonstra um pipeline completo de dados, desde a geração até a previsão, integrando Python, banco de dados e ferramentas de visualização.
