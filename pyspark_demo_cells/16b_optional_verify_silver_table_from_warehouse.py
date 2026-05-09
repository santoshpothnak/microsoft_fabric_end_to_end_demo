# Purpose: Optional verification cell for the Warehouse save path.
# Use this after 15b_optional_save_silver_table_to_warehouse.py.

# Required for the Fabric Data Warehouse Spark connector in Fabric notebooks.
import com.microsoft.spark.fabric

# Keep these values aligned with 15b_optional_save_silver_table_to_warehouse.py.
WAREHOUSE_NAME = "SalesAnalytics_Warehouse"
SCHEMA_NAME = "dbo"
TABLE_NAME = "SalesOrders_Silver"

# The connector expects a three-part name:
# <warehouse name>.<schema name>.<table name>
target_table = f"{WAREHOUSE_NAME}.{SCHEMA_NAME}.{TABLE_NAME}"

# Display the persisted Warehouse table.
display(spark.read.synapsesql(target_table))

