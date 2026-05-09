# Purpose: Build the final silver-layer DataFrame with clean names and
# report-ready columns.

# Select the business columns and replace raw messy fields with clean versions.
silver_df = clean_df.select(
    col("OrderID"),
    col("OrderDateParsed").alias("OrderDate"),
    col("ShipDateParsed").alias("ShipDate"),
    col("Region"),
    col("Country"),
    col("CustomerName"),
    col("Product"),
    col("Category"),
    col("QuantityClean").alias("Quantity"),
    col("UnitPriceClean").alias("UnitPrice"),
    col("SalesClean").alias("Sales"),
    col("ProfitClean").alias("Profit"),
    col("ProfitMarginPct")
)

# Display the finished silver dataset before saving it to the Lakehouse.
display(silver_df)
