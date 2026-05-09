# Purpose: Optional alternative to saving the silver table in the Lakehouse.
# This writes the cleaned silver_df DataFrame directly to a Fabric Warehouse.
#
# Use this if you want your curated silver table to live in a Warehouse instead
# of the Lakehouse. Run it after 14_select_final_silver_columns.py.

# Required for the Fabric Data Warehouse Spark connector in Fabric notebooks.
import com.microsoft.spark.fabric

# Replace this with the exact name of your Fabric Warehouse item.
WAREHOUSE_NAME = "SalesAnalytics_Warehouse"

# Use dbo unless you created a different schema in the Warehouse.
SCHEMA_NAME = "dbo"

# Destination Warehouse table name.
TABLE_NAME = "SalesOrders_Silver"

# The connector expects a three-part name:
# <warehouse name>.<schema name>.<table name>
target_table = f"{WAREHOUSE_NAME}.{SCHEMA_NAME}.{TABLE_NAME}"

# overwrite mode keeps the live demo repeatable.
# If the table exists, its data is replaced. If it does not exist, it is created.
silver_df.write.mode("overwrite").synapsesql(target_table)

