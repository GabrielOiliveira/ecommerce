# E-commerce Analytics Project

Desafio Final PD - Trilha de Dados

## Descrição

Este projeto tem como objetivo analisar dados de vendas de um e-commerce, aplicando técnicas de engenharia de dados, análise exploratória, visualização e modelagem preditiva.

O projeto foi ajustado para ser simples de executar em qualquer ambiente, utilizando SQLite como banco de dados padrão. A integração com SQL Server foi mantida apenas como uma opção avançada.

## Objetivos

- Entender o comportamento dos clientes
- Identificar produtos e categorias mais relevantes
- Analisar tendências de vendas
- Criar um dashboard para visualização dos dados
- Prever o faturamento futuro com regressão linear

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib
- Plotly
- Scikit-learn
- Power BI
- SQL Server opcional

## Estrutura do Projeto

```text
ecommerce/
│
├── data/
│   └── ecom_data.csv
│
├── database/
│   └── ecommerce.db
│
├── scripts/
│   ├── gera_dados.py
│   ├── sqlite.py
│   └── sqlserver.py
│
├── sql/
│   └── consultas.sql
│
├── notebooks/
│   ├── analise.ipynb
|   ├── dashboard_plotly.ipynb
│   └── previsao.ipynb
│
├── dashboard/
│   ├── Dashboard.pbix
│   └── imagens/
|       └──dashboard.png
│
├── requirements.txt
└── README.md
```

## Dependências

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Conteúdo do arquivo `requirements.txt`:

```txt
pandas
numpy
matplotlib
plotly
scikit-learn
faker
nbformat
```

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd ecommerce
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3. Gerar o dataset

```bash
python scripts/gera_dados.py
```

Esse comando cria o arquivo:

```text
data/ecom_data.csv
```

### 4. Executar o ETL com SQLite

```bash
python scripts/sqlite.py
```

Esse comando cria automaticamente o banco local:

```text
database/ecommerce.db
```

Também cria automaticamente a tabela:

```text
vendas
```

## Execução Padrão

A execução padrão do projeto utiliza SQLite.

Essa escolha foi feita para reduzir a dependência de ambiente externo, evitando a necessidade de instalar e configurar SQL Server, SSMS, driver ODBC e instância local.

Com SQLite, o projeto pode ser executado apenas com Python e as bibliotecas listadas no `requirements.txt`.

## Execução Opcional com SQL Server

O projeto também possui um script opcional para carga no SQL Server:

```bash
python scripts/sqlserver.py
```

Essa execução exige configuração externa, como:

- SQL Server Express instalado
- SQL Server Management Studio instalado
- ODBC Driver 17 for SQL Server instalado
- Banco `EcommerceDB` criado
- Tabela `vendas` criada
- Ajuste da string de conexão no script

Por esse motivo, o SQL Server não é a forma principal de execução do projeto.

## ETL

As etapas de ETL realizadas foram:

- Leitura do arquivo CSV
- Remoção de valores nulos
- Remoção de duplicados
- Conversão da coluna `Data_Venda` para formato de data
- Criação da coluna `Valor_Total`
- Carga dos dados no banco SQLite

## Análise Exploratória

Foram analisados:

- Faturamento total
- Ticket médio
- Volume de pedidos
- Vendas ao longo do tempo
- Faturamento por categoria
- Produtos mais vendidos
- Identificação de outliers
- Correlação entre variáveis

## Dashboard

O dashboard foi desenvolvido no Power BI e apresenta:

- KPIs principais
- Evolução das vendas
- Faturamento por categoria
- Produtos mais vendidos
- Filtros interativos

O arquivo do dashboard está localizado em:

```text
dashboard/Dashboard.pbix
```

## Modelo Preditivo

Foi utilizado um modelo de regressão linear para prever vendas futuras.

### Metodologia

- Agrupamento das vendas por mês
- Conversão da variável temporal em formato numérico
- Treinamento com `LinearRegression`
- Previsão do próximo período

### Resultado

O modelo indicou uma tendência de crescimento nas vendas ao longo do tempo.

## Insights

- Algumas categorias concentram maior faturamento
- Existe tendência de crescimento nas vendas
- Há variações mensais que podem indicar sazonalidade
- Produtos específicos apresentam maior impacto no resultado total

## Limitações

- Dados simulados
- Modelo preditivo simples
- Não considera fatores externos
- O dashboard depende do arquivo local do Power BI
- A execução com SQL Server depende de configuração externa

## Conclusão

O projeto demonstra um pipeline completo de dados, passando por geração, tratamento, armazenamento, análise, visualização e previsão.

A versão padrão com SQLite torna o projeto mais simples de executar em diferentes ambientes, enquanto a versão opcional com SQL Server mantém a possibilidade de simular um cenário mais próximo de ambientes corporativos.
