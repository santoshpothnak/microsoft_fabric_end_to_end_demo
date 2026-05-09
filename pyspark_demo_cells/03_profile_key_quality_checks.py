# Purpose: Run the main data quality checks in one cell so the audience
# can quickly see why the raw data is not report-ready.

# Check category values to expose typos such as "Electornics".
display(raw_df.groupBy("Category").count().orderBy(col("count").desc()))

# Check region values to expose inconsistent labels such as APAC, apac,
# and Asia Pacific.
display(raw_df.groupBy("Region").count().orderBy(col("count").desc()))

# Check distinct order date values to show mixed and invalid date formats.
display(raw_df.select("OrderDate").distinct())

# Check numeric fields that are stored as messy text, such as "$800"
# or "10 units".
display(raw_df.select("Quantity", "UnitPrice", "Sales"))
