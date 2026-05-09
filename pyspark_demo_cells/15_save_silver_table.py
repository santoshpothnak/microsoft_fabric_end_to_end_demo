# Purpose: Save the cleaned silver DataFrame as a managed Lakehouse table.
# overwrite mode keeps the demo repeatable if you rerun the notebook.

silver_df.write.mode("overwrite").saveAsTable("SalesOrders_Silver")
