# Purpose: Create the first cleaned DataFrame and standardize text fields.
# This prevents duplicate report buckets caused by spaces, casing, or typos.

# Trim leading and trailing spaces from key text columns.
clean_df = raw_df \
    .withColumn("Region", trim(col("Region"))) \
    .withColumn("Country", trim(col("Country"))) \
    .withColumn("CustomerName", trim(col("CustomerName"))) \
    .withColumn("Category", trim(col("Category")))

# Convert region variants into a single reporting label.
clean_df = clean_df.withColumn(
    "Region",
    when(lower(col("Region")).isin("apac", "asia pacific"), "APAC")
    .when(lower(col("Region")) == "north america", "North America")
    .when(lower(col("Region")) == "emea", "EMEA")
    .when(lower(col("Region")) == "latam", "LATAM")
    .otherwise(col("Region"))
)

# Correct known category spelling issues.
clean_df = clean_df.withColumn(
    "Category",
    when(lower(col("Category")) == "electornics", "Electronics")
    .otherwise(col("Category"))
)
