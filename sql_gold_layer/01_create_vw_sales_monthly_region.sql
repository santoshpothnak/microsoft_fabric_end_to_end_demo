-- Purpose: Create a gold-layer view for monthly sales and profit by region.
-- Use this view for trend visuals and regional performance reporting in Power BI.

CREATE OR ALTER VIEW vw_Sales_Monthly_Region AS
SELECT
    -- Calendar fields used for monthly trend analysis.
    YEAR(OrderDate) AS OrderYear,
    MONTH(OrderDate) AS OrderMonth,

    -- Business grouping used for comparing regional sales.
    Region,

    -- Aggregated measures for report KPIs and visuals.
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit,
    ROUND(AVG(ProfitMarginPct), 2) AS AvgProfitMarginPct
FROM SalesOrders_Silver
GROUP BY
    YEAR(OrderDate),
    MONTH(OrderDate),
    Region;
