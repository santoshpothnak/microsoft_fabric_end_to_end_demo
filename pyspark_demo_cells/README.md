# PySpark Demo Cells

Copy these files into the Fabric notebook in numeric order. They map to the notebook steps in `Microsoft_Fabric_Demo_Guide_Audience_v2.md`.

| File | Demo step | Purpose |
|---|---|---|
| `01_read_and_display_raw_table.py` | 5 | Read `SalesOrders_Raw` and show the raw data |
| `02_profile_row_counts.py` | 5 | Show total rows and distinct order count |
| `03_profile_key_quality_checks.py` | 5 | Show the main visible data quality issues |
| `04_profile_category_values.py` | 5.1 | Show category typos |
| `05_profile_region_values.py` | 5.1 | Show inconsistent region labels |
| `06_profile_order_dates.py` | 5.1 | Show mixed and invalid dates |
| `07_profile_quantity_price_sales.py` | 5.1 | Show numeric fields stored as messy text |
| `08_profile_missing_values.py` | 5.1 | Show missing values by column |
| `09_standardize_text_columns.py` | 6.1 | Trim and standardize text values |
| `10_parse_mixed_date_formats.py` | 6.2 | Parse order and ship dates |
| `11_clean_quantity_and_price.py` | 6.3 | Convert quantity and unit price to numeric fields |
| `12_recalculate_sales_and_margin.py` | 6.4 | Recalculate sales, profit, and margin |
| `13_remove_bad_records_and_duplicates.py` | 6.5 | Filter invalid rows and remove duplicate orders |
| `14_select_final_silver_columns.py` | 6.6 | Select the final silver-layer columns |
| `15_save_silver_table.py` | 7 | Save the silver table |
| `15b_optional_save_silver_table_to_warehouse.py` | 7 optional | Save the silver table directly to a Fabric Warehouse instead of the Lakehouse |
| `16_verify_silver_table.py` | 7 | Display the saved silver table |
| `16b_optional_verify_silver_table_from_warehouse.py` | 7 optional | Verify the silver table from the Fabric Warehouse |
