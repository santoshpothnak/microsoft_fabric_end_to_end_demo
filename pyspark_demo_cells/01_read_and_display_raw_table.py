# Purpose: Load the raw bronze table from the Lakehouse and show the
# "before cleaning" dataset to the audience.

# Import common PySpark SQL functions used by later cells as well.
from pyspark.sql.functions import *

# Read the raw table created from the uploaded CSV file.
raw_df = spark.read.table("SalesOrders_Raw")

# Display sample records so data quality issues are visible before cleanup.
display(raw_df)
