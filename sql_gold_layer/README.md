# SQL Gold Layer Scripts

Copy these SQL scripts into the Fabric SQL editor after `SalesOrders_Silver` has been created by the notebook.

| File | Demo step | Purpose |
|---|---|---|
| `01_create_vw_sales_monthly_region.sql` | 8 | Create a monthly sales and profit view by region |
| `02_create_vw_product_performance.sql` | 8 | Create a product and category performance view |
| `03_verify_gold_views.sql` | 8 | Preview both gold-layer views before building the Power BI report |

These scripts use `CREATE OR ALTER VIEW`, which makes the demo repeatable if you rerun the SQL during practice.
They create the gold layer used by the Power BI visuals in the demo.
