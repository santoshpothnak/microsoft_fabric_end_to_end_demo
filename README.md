# Microsoft Fabric End to End Demo

This repository contains a collection of PySpark scripts and notebook cells demonstrating an end-to-end data engineering workflow in Microsoft Fabric.

## Overview
The code guides you through taking a raw bronze sales dataset and transforming it into a clean, report-ready silver table. It covers:
- Data profiling and quality checks (checking row counts, missing values, date formats).
- Standardizing text columns and parsing dates.
- Cleaning numeric fields (Quantity, UnitPrice) and recalculating accurate Sales and Profit margins.
- Saving the curated DataFrame to a Fabric Lakehouse or Data Warehouse.