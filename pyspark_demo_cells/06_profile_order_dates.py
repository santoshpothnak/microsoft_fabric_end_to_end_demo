# Purpose: Show mixed and invalid date values before parsing.
# Trend reporting needs one valid date type, not multiple text formats.

display(raw_df.select("OrderDate").distinct())
