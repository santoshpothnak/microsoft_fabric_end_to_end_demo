# Purpose: Show numeric values that are currently stored as text.
# Quantity and UnitPrice must be cleaned before reliable calculations.

display(raw_df.select("Quantity", "UnitPrice", "Sales"))
