-- Purpose: Quickly verify that both gold-layer views return data.
-- Run this after creating the views and before connecting Power BI.

SELECT TOP 10
    OrderYear,
    OrderMonth,
    Region,
    TotalSales,
    TotalProfit,
    AvgProfitMarginPct
FROM vw_Sales_Monthly_Region
ORDER BY
    OrderYear,
    OrderMonth,
    Region;

SELECT TOP 10
    Category,
    Product,
    TotalQuantity,
    TotalSales,
    TotalProfit
FROM vw_Product_Performance
ORDER BY
    TotalSales DESC;

