# Purpose: Parse date strings into real date columns.
# coalesce returns the first successful parse across the supported formats.

# Convert mixed OrderDate text formats into a single date column.
clean_df = clean_df.withColumn(
    "OrderDateParsed",
    coalesce(
        to_date(col("OrderDate"), "MM/dd/yyyy"),
        to_date(col("OrderDate"), "dd/MM/yyyy"),
        to_date(col("OrderDate"), "yyyy/MM/dd"),
        to_date(col("OrderDate"), "MM-dd-yyyy")
    )
)

# Convert mixed ShipDate text formats into a single date column.
clean_df = clean_df.withColumn(
    "ShipDateParsed",
    coalesce(
        to_date(col("ShipDate"), "MM/dd/yyyy"),
        to_date(col("ShipDate"), "dd/MM/yyyy"),
        to_date(col("ShipDate"), "yyyy/MM/dd"),
        to_date(col("ShipDate"), "MM-dd-yyyy")
    )
)
