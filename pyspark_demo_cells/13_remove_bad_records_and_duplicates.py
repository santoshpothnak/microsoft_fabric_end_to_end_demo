# Purpose: Keep only records that are usable for reporting.
# This removes invalid dates, missing sales values, and duplicate orders.

# Keep records with a valid parsed order date.
clean_df = clean_df.filter(col("OrderDateParsed").isNotNull())

# Keep records where sales can be calculated or converted.
clean_df = clean_df.filter(col("SalesClean").isNotNull())

# Keep one record per business order key.
clean_df = clean_df.dropDuplicates(["OrderID"])
