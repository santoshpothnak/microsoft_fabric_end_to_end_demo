# Purpose: Create reliable sales, profit, and margin fields for analytics.
# Sales is recalculated when clean quantity and price are available.

clean_df = clean_df.withColumn(
    "SalesClean",
    when(
        col("QuantityClean").isNotNull() & col("UnitPriceClean").isNotNull(),
        col("QuantityClean") * col("UnitPriceClean")
    ).otherwise(col("Sales").cast("double"))
)

# Cast profit to a numeric type so it can be aggregated.
clean_df = clean_df.withColumn("ProfitClean", col("Profit").cast("double"))

# Calculate profit margin as a percentage rounded to two decimals.
clean_df = clean_df.withColumn(
    "ProfitMarginPct",
    round((col("ProfitClean") / col("SalesClean")) * 100, 2)
)
