# Purpose: Count nulls and blank strings in every raw column.
# This helps decide which records or fields need filtering or defaults.

display(raw_df.select([
    # For each column, count rows where the value is null or an empty string.
    count(when(col(c).isNull() | (trim(col(c)) == ""), c)).alias(c)
    for c in raw_df.columns
]))
