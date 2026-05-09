-- Purpose: Create a gold-layer view for product and category performance.
-- Use this view for product ranking, category analysis, and profitability visuals.

CREATE OR ALTER VIEW vw_Product_Performance AS
SELECT
    -- Product hierarchy fields used for slicing and ranking.
    Category,
    Product,

    -- Aggregated measures used in Power BI visuals.
    SUM(Quantity) AS TotalQuantity,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM SalesOrders_Silver
GROUP BY
    Category,
    Product;
