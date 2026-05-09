# Purpose: Profile the size of the raw dataset and check whether
# duplicate OrderID values may exist.

display(raw_df.select(
    # Total number of rows loaded from the raw table.
    count("*").alias("row_count"),

    # Number of unique business keys. If this is lower than row_count,
    # duplicate orders are present.
    countDistinct("OrderID").alias("distinct_orders")
))
