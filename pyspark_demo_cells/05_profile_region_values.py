# Purpose: Show inconsistent region labels before standardization.
# Multiple labels for the same region would split report visuals.

display(raw_df.groupBy("Region").count().orderBy(col("count").desc()))
