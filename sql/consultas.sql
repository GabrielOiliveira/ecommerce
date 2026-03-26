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

-- Faturamento por Categoria
SELECT Categoria_Produto,
       SUM(Valor_Total) AS faturamento
FROM vendas
GROUP BY Categoria_Produto
ORDER BY faturamento DESC;

-- Ranking de Clientes
SELECT 
    ID_Cliente,
    SUM(Valor_Total) AS total_gasto,
    RANK() OVER (ORDER BY SUM(Valor_Total) DESC) AS ranking
FROM vendas
GROUP BY ID_Cliente;

-- Vendas por Mês
SELECT 
    FORMAT(Data_Venda, 'yyyy-MM') AS mes,
    SUM(Valor_Total) AS total
FROM vendas
GROUP BY FORMAT(Data_Venda, 'yyyy-MM')
ORDER BY mes;