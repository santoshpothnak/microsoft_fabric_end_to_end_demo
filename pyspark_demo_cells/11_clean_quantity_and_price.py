# Purpose: Convert messy quantity and price text into numeric columns.
# These clean numeric fields are used for sales recalculation and reporting.

# Extract the numeric part of values such as "10 units" and cast to integer.
clean_df = clean_df.withColumn(
    "QuantityClean",
    regexp_extract(col("Quantity"), r"(\d+)", 1).cast("int")
)

# Remove currency symbols/text such as "$" or "USD" and cast to double.
clean_df = clean_df.withColumn(
    "UnitPriceClean",
    regexp_replace(col("UnitPrice"), r"[^0-9.]", "").cast("double")
)
