# Purpose: Show category-level inconsistencies before standardization.
# This makes spelling mistakes visible in a simple grouped view.

display(raw_df.groupBy("Category").count().orderBy(col("count").desc()))
