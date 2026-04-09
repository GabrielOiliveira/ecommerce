# ecommerce
Desafio Final PD - Trilha de Dados

## Descrição

Este projeto tem como objetivo analisar dados de vendas de um e-commerce, aplicando técnicas de engenharia de dados, análise exploratória e modelagem preditiva.

---

## Objetivos

- Entender o comportamento dos clientes
- Identificar produtos e categorias mais relevantes
- Analisar tendências de vendas
- Prever o faturamento futuro

---

## Tecnologias Utilizadas

- Python (Pandas, NumPy)
- SQL Server
- Power BI
- Matplotlib / Plotly
- Scikit-learn

---

## ETL (Extração, Transformação e Carga)

- Remoção de dados nulos e duplicados
- Conversão de datas
- Criação da variável `Valor_Total`
- Inserção dos dados no SQL Server

---

## Análise Exploratória (EDA)

Foram analisados:

- Faturamento total
- Ticket médio
- Volume de pedidos
- Vendas ao longo do tempo
- Distribuição por categoria

---

## Dashboard

O dashboard foi desenvolvido no Power BI e apresenta:

- KPIs principais
- Evolução das vendas
- Faturamento por categoria
- Filtros dinâmicos

---

## Modelo Preditivo

Foi utilizado um modelo de regressão linear para prever o volume de vendas.

### Metodologia:

- Agrupamento das vendas por mês
- Transformação do tempo em variável numérica
- Treinamento com Linear Regression

### Resultado:

O modelo indicou uma tendência de crescimento nas vendas ao longo do tempo.

---

## Insights

- Algumas categorias concentram a maior parte do faturamento
- Existe tendência de crescimento nas vendas
- Há variações mensais que podem indicar sazonalidade

---

## Limitações

- Dados simulados
- Modelo simples
- Não considera fatores externos

---

## Conclusão

O projeto demonstra um pipeline completo de dados, desde a geração até a previsão, permitindo análises estratégicas e apoio à tomada de decisão.
