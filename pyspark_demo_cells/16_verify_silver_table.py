# Purpose: Verify that the silver table was written successfully.
# This displays the persisted table that downstream SQL views and reports use.

display(spark.read.table("SalesOrders_Silver"))
