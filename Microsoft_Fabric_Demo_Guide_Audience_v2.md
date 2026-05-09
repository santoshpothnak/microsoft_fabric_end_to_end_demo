# End-to-End Microsoft Fabric Demo Guide

This guide walks through a complete 55-minute Microsoft Fabric demo using a sales dataset designed specifically for data ingestion, notebook-based cleaning, warehouse modeling, Power BI reporting, and a short Copilot/governance finish. The flow aligns with common end-to-end Fabric tutorials and Microsoft Learn guidance for lakehouses, notebooks, end-to-end analytics, and Power BI on Fabric.[cite:31][cite:16][cite:20][cite:62]

## Session overview

**Session title:** From Lakehouse to Insights: End-to-End Analytics in Microsoft Fabric (with Copilot & Governance)

**Audience:** Power BI professionals, Fabric learners, analytics engineers, and community attendees who want a practical architecture-led walkthrough.

**Duration:** 55 minutes.

**Primary objective:** Show how raw business data can be landed in a Lakehouse, cleaned in a notebook, shaped into a gold layer, and consumed in Power BI inside one Fabric experience.[cite:31][cite:44][cite:48]

## Assets used in this demo

### Dataset
Use the provided 100-row CSV file created for this session. It contains intentional data quality issues such as invalid dates, inconsistent region values, missing fields, malformed numeric values, and category typos so the notebook cleaning stage has visible value.

[cite:124]

### Fabric items to create
- One workspace.
- One Lakehouse.
- One notebook attached to the Lakehouse.
- One SQL Warehouse.
- One Power BI report.

## Data model design

The raw file contains these columns, each chosen to support both cleansing and reporting:

| Column | Why it exists |
|---|---|
| OrderID | Used for duplicate checks and business key validation |
| OrderDate | Used to demonstrate date parsing and trend reporting |
| ShipDate | Used to show missing values and potential SLA analysis |
| Region | Used to standardize values like APAC, apac, and Asia Pacific |
| Country | Used to normalize country names and codes |
| CustomerName | Used to show trimming and blank handling |
| Product | Used for product-level reporting |
| Category | Used to fix typos such as Electornics |
| Quantity | Used to clean malformed numeric values like N/A and 10 units |
| UnitPrice | Used to remove symbols such as $ and USD |
| Sales | Used for KPI and trend visuals |
| Profit | Used for margin and profitability analysis |

## Demo flow

### 1. Open with the business problem (0-5 min)
Start with a simple business story: leadership wants to understand sales trends by region, top-performing products, and whether the data behind the dashboard can be trusted. Explain that the demo will show the full path from raw CSV to trusted report inside Microsoft Fabric.[cite:44][cite:48]

Suggested talk track:
- The business has raw operational sales data.
- The file is messy and not report-ready.
- The goal is to turn it into trusted insights using Fabric.

### 2. Create or open the Lakehouse (5-10 min)
In the Fabric workspace, create a new Lakehouse or open an existing one. Microsoft documents the Lakehouse as the central store for data files and Delta tables, making it a natural landing zone for raw business data.[cite:16][cite:19]

Steps:
1. Open the Fabric workspace.
2. Select **New** > **Lakehouse**.
3. Name it `SalesAnalytics_Lakehouse`.
4. Open the Lakehouse item.

Suggested talk track:
- The Lakehouse will act as the landing area for raw data.
- This is the bronze layer in a medallion-style architecture.[cite:53][cite:55]

### 3. Load the raw CSV into the Lakehouse (10-15 min)
Upload the generated CSV file into the Lakehouse and create a table from it. End-to-end Fabric tutorials and the Lakehouse tutorial both use this landing pattern to move source data into a structured environment.[cite:16][cite:31]

Steps:
1. In the Lakehouse, choose **Files** or **Upload**.
2. Upload the `SalesOrders_Raw_100Rows.csv` file.
3. Use **Load to Tables** or **Create table**.
4. Name the table `SalesOrders_Raw`.
5. Open the table preview and point out the visible data quality problems.

What to highlight on screen:
- Invalid and mixed date formats in `OrderDate`.
- Inconsistent values in `Region`.
- Blank `CustomerName` values.
- Typos in `Category`.
- `Quantity` and `UnitPrice` stored as messy text.

### 4. Create a notebook and attach it to the Lakehouse (15-18 min)
Fabric notebooks are designed for interactive data exploration and transformation against Lakehouse data, which makes them ideal for the silver-layer cleaning step in this demo.[cite:20][cite:23]

Steps:
1. Inside the Lakehouse, select **Open notebook** or create **New notebook**.
2. Confirm the notebook is attached to `SalesAnalytics_Lakehouse`.
3. Rename the notebook to `SalesOrders_Cleaning_Notebook`.

Suggested talk track:
- The notebook will convert raw data into a clean analytical table.
- This is where the silver layer is created.

### 5. Read and profile the raw table (18-22 min)
Run a first cell to read the raw table and display sample records. This establishes the “before” state and makes the cleanup story visible to the audience.[cite:20][cite:23]

Use this PySpark code:

```python
from pyspark.sql.functions import *

raw_df = spark.read.table("SalesOrders_Raw")
display(raw_df)
```

Then add a quick profiling cell:

```python
display(raw_df.select(
    count("*").alias("row_count"),
    countDistinct("OrderID").alias("distinct_orders")
))
```

Add these focused profiling checks so the inconsistencies are obvious on screen:

```python
display(raw_df.groupBy("Category").count().orderBy(col("count").desc()))
display(raw_df.groupBy("Region").count().orderBy(col("count").desc()))
display(raw_df.select("OrderDate").distinct())
display(raw_df.select("Quantity", "UnitPrice", "Sales"))
```

### 5.1 What to highlight before cleaning
The dataset was intentionally created with visible quality issues so the notebook transformation step demonstrates clear business value. Common data quality problems include inconsistent labels, malformed dates, missing values, and incorrect data types, all of which can affect reporting accuracy.[cite:104][cite:105][cite:113]

#### Category inconsistencies
The `Category` field includes a typo: `Electornics` instead of `Electronics`. If left unresolved, this would split category-level visuals and slicers into separate buckets, producing inaccurate totals for the same business concept.[cite:132][cite:140]

Use this check:

```python
display(raw_df.groupBy("Category").count().orderBy(col("count").desc()))
```

Expected explanation:
- `Electronics` is the intended value.
- `Electornics` is a misspelling.
- The audience should see why standardization matters before any reporting starts.

#### Region inconsistencies
The `Region` field contains multiple labels for the same region, including `APAC`, `apac`, and `Asia Pacific`. In a report, these values would create multiple bars or trend lines for what is logically one region, which weakens trust in the dashboard.[cite:128][cite:132]

Use this check:

```python
display(raw_df.groupBy("Region").count().orderBy(col("count").desc()))
```

Expected explanation:
- `APAC`, `apac`, and `Asia Pacific` all represent the same business region.
- Standardizing them into one value avoids duplicate groupings in charts.

#### Date inconsistencies
The `OrderDate` column includes mixed date formats such as `MM/DD/YYYY`, `DD/MM/YYYY`, `YYYY/MM/DD`, and `MM-DD-YYYY`, along with invalid values like `invalid_date`. This prevents clean trend analysis until the dates are parsed into a single valid date type.[cite:104][cite:113]

Use this check:

```python
display(raw_df.select("OrderDate").distinct())
```

Expected explanation:
- Trend visuals depend on one consistent date column.
- Invalid or mixed formats must be converted before monthly or daily analysis is possible.

#### Quantity and UnitPrice inconsistencies
The `Quantity` and `UnitPrice` columns contain numeric values stored as text, including entries such as `10 units`, `$800`, `100 USD`, and blanks. These values cannot be reliably aggregated until they are converted into numeric types.[cite:105][cite:113]

Use this check:

```python
display(raw_df.select("Quantity", "UnitPrice", "Sales"))
```

Expected explanation:
- Symbols and text fragments must be removed.
- Numeric conversion is required before computing totals, averages, or margins.

#### Missing values
Some records have blank `ShipDate`, `CustomerName`, `Quantity`, `UnitPrice`, or `Sales` values. Missing data forces a design choice: either filter out incomplete rows or apply business rules for default handling.[cite:105][cite:140]

Use this check:

```python
raw_df.select([
    count(when(col(c).isNull() | (trim(col(c)) == ""), c)).alias(c)
    for c in raw_df.columns
]))
```

Expected explanation:
- Not every missing field has the same impact.
- Missing customer names might be tolerated, but missing dates or sales amounts usually affect analysis quality.

### 5.2 Suggested narration for this section
Use a short explanation like this while profiling the raw data:

> The file has landed successfully in the Lakehouse, but it is not yet analysis-ready. The same category appears under more than one label, the same region appears in multiple formats, dates are inconsistent, and some numeric fields contain text. If this data is used directly in a dashboard, the results will be fragmented and unreliable. The notebook step fixes these issues so the final Power BI report is based on a trusted dataset.

What to say:
- The file loaded successfully, but the structure is not analysis-ready.
- The next step is to clean data types, standardize text, and remove invalid records.

### 6. Clean the data in the notebook (22-32 min)
This is the core of the demo. Data cleaning commonly includes fixing date formats, standardizing text values, handling missing values, removing duplicates, and converting numeric fields into usable types.[cite:104][cite:105][cite:113]

Use the following PySpark code in sequence.

#### 6.1 Standardize text columns
```python
clean_df = raw_df \
    .withColumn("Region", trim(col("Region"))) \
    .withColumn("Country", trim(col("Country"))) \
    .withColumn("CustomerName", trim(col("CustomerName"))) \
    .withColumn("Category", trim(col("Category")))

clean_df = clean_df.withColumn(
    "Region",
    when(lower(col("Region")).isin("apac", "asia pacific"), "APAC")
    .when(lower(col("Region")) == "north america", "North America")
    .when(lower(col("Region")) == "emea", "EMEA")
    .when(lower(col("Region")) == "latam", "LATAM")
    .otherwise(col("Region"))
)

clean_df = clean_df.withColumn(
    "Category",
    when(lower(col("Category")) == "electornics", "Electronics")
    .otherwise(col("Category"))
)
```

#### 6.2 Parse mixed date formats
```python
clean_df = clean_df.withColumn(
    "OrderDateParsed",
    coalesce(
        to_date(col("OrderDate"), "MM/dd/yyyy"),
        to_date(col("OrderDate"), "dd/MM/yyyy"),
        to_date(col("OrderDate"), "yyyy/MM/dd"),
        to_date(col("OrderDate"), "MM-dd-yyyy")
    )
)

clean_df = clean_df.withColumn(
    "ShipDateParsed",
    coalesce(
        to_date(col("ShipDate"), "MM/dd/yyyy"),
        to_date(col("ShipDate"), "dd/MM/yyyy"),
        to_date(col("ShipDate"), "yyyy/MM/dd"),
        to_date(col("ShipDate"), "MM-dd-yyyy")
    )
)
```

#### 6.3 Clean quantity and price columns
```python
clean_df = clean_df.withColumn(
    "QuantityClean",
    regexp_extract(col("Quantity"), r"(\\d+)", 1).cast("int")
)

clean_df = clean_df.withColumn(
    "UnitPriceClean",
    regexp_replace(col("UnitPrice"), r"[^0-9.]", "").cast("double")
)
```

#### 6.4 Recalculate sales and margin fields
```python
clean_df = clean_df.withColumn(
    "SalesClean",
    when(col("QuantityClean").isNotNull() & col("UnitPriceClean").isNotNull(), col("QuantityClean") * col("UnitPriceClean"))
    .otherwise(col("Sales").cast("double"))
)

clean_df = clean_df.withColumn("ProfitClean", col("Profit").cast("double"))
clean_df = clean_df.withColumn(
    "ProfitMarginPct",
    round((col("ProfitClean") / col("SalesClean")) * 100, 2)
)
```

#### 6.5 Remove bad records and duplicates
```python
clean_df = clean_df.filter(col("OrderDateParsed").isNotNull())
clean_df = clean_df.filter(col("SalesClean").isNotNull())
clean_df = clean_df.dropDuplicates(["OrderID"])
```

#### 6.6 Select final silver-layer columns
```python
silver_df = clean_df.select(
    col("OrderID"),
    col("OrderDateParsed").alias("OrderDate"),
    col("ShipDateParsed").alias("ShipDate"),
    col("Region"),
    col("Country"),
    col("CustomerName"),
    col("Product"),
    col("Category"),
    col("QuantityClean").alias("Quantity"),
    col("UnitPriceClean").alias("UnitPrice"),
    col("SalesClean").alias("Sales"),
    col("ProfitClean").alias("Profit"),
    col("ProfitMarginPct")
)

display(silver_df)
```

### 7. Save the cleaned table to the Lakehouse (32-34 min)
Save the notebook result as a clean Delta table named `SalesOrders_Silver`. This follows the common Fabric lakehouse pattern of moving from raw to refined data within the same environment.[cite:16][cite:18][cite:53]

```python
silver_df.write.mode("overwrite").saveAsTable("SalesOrders_Silver")
```

Then verify it:

```python
display(spark.read.table("SalesOrders_Silver"))
```

Optional Warehouse path:
If you want the silver table to live directly in a Fabric Warehouse instead of the Lakehouse, use `pyspark_demo_cells/15b_optional_save_silver_table_to_warehouse.py` after the final `silver_df` cell. Update `WAREHOUSE_NAME` in that script to match your Warehouse item name, then use `pyspark_demo_cells/16b_optional_verify_silver_table_from_warehouse.py` to verify it.

Suggested talk track:
- The silver layer now contains trusted columns and valid data types.
- This is the source for downstream analytics and modeling.

### 8. Create the gold layer with business aggregates (34-40 min)
Use either the SQL analytics endpoint or a Warehouse to create aggregated tables ready for reporting. Fabric’s end-to-end analytics guidance emphasizes shaping curated analytical data for consumption layers such as semantic models and reports.[cite:31][cite:44][cite:62]

Option A: Use the SQL analytics endpoint from the Lakehouse.

If you saved `SalesOrders_Silver` directly to a Warehouse in step 7, run the gold-layer SQL in that same Warehouse instead.

Create a gold table with monthly regional sales:

```sql
CREATE OR ALTER VIEW vw_Sales_Monthly_Region AS
SELECT
    YEAR(OrderDate) AS OrderYear,
    MONTH(OrderDate) AS OrderMonth,
    Region,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit,
    ROUND(AVG(ProfitMarginPct), 2) AS AvgProfitMarginPct
FROM SalesOrders_Silver
GROUP BY YEAR(OrderDate), MONTH(OrderDate), Region;
```

Create another gold view for product analysis:

```sql
CREATE OR ALTER VIEW vw_Product_Performance AS
SELECT
    Category,
    Product,
    SUM(Quantity) AS TotalQuantity,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM SalesOrders_Silver
GROUP BY Category, Product;
```

If preferred, a dedicated Warehouse can be created instead of using the Lakehouse SQL endpoint. Fabric supports both approaches for analytics workloads.[cite:48][cite:47]

### 9. Build the Power BI report (40-48 min)
Power BI can consume Fabric data directly, including data from Lakehouse SQL endpoints and Warehouses, making it straightforward to build an end-to-end reporting story in one workspace.[cite:62][cite:60][cite:48]

Steps:
1. Create a new Power BI report in the same workspace.
2. Connect to `vw_Sales_Monthly_Region` and `vw_Product_Performance`.
3. Create the following visuals:
   - Line chart: `OrderMonth` on axis, `TotalSales` as value, `Region` as legend.
   - Bar chart: `Region` by `TotalSales`.
   - Bar chart: `Product` by `TotalProfit`.
   - Card: total sales.
   - Slicer: category or region.
4. Add a report title such as `Sales Performance Overview`.

Suggested talk track:
- The report now sits on top of curated gold-layer data.
- Each visual is backed by data that has already been standardized and validated.

### 10. Add a detailed Copilot and governance finish (48-52 min)
Copilot in Power BI can generate summaries, answer natural-language questions, and create visuals from report and semantic model context, while Fabric and Purview governance capabilities help teams understand lineage, sensitivity, and compliance boundaries.[cite:28][cite:37][cite:43]

#### 10.1 Copilot walkthrough in Power BI
Use Copilot only after the report visuals are already working. Microsoft documents Copilot as working with Power BI reports and semantic models to summarize pages, answer questions, and help create visuals.[cite:28]

Steps:
1. Open the finished Power BI report inside the Fabric workspace.
2. Confirm the report page contains meaningful visuals such as sales trend, region comparison, and product profitability.
3. Open the **Copilot** pane from the report interface.
4. Start with a summarization prompt so the audience sees an easy win before asking analytical questions.

Suggested first prompt:
- `Summarize this report in 3 bullet points.`

What to say:
- Copilot is reading the report context rather than guessing from raw text.
- This is useful for business users who want a quick executive summary before they explore details.[cite:28]

Then move to analytical prompts.

Suggested prompts:
- `Which region generated the highest sales?`
- `Which product category has the highest total profit?`
- `Describe the monthly sales trend.`
- `Create a visual comparing total sales by region.`

What to highlight:
- Copilot can answer questions grounded in the semantic model and report context.[cite:28]
- Prompt quality matters; simple business language usually works best.
- Copilot is most valuable when the model is already clean and well named, which connects back to the notebook and gold-layer work.

#### 10.2 Copilot explanation
At this stage, the data has already been cleaned and modeled, so the focus shifts from engineering to consumption. Copilot helps business users interact with the report using natural language. Instead of building every visual manually, a user can ask which region performed best or request a quick summary of the report page. Copilot becomes more useful when the underlying data model is curated and governed.[cite:28][cite:37]

#### 10.3 Governance walkthrough
After Copilot, move immediately into governance so the audience sees that self-service analytics still needs trust and control. Microsoft’s Fabric and Purview guidance highlights governance for lineage, sensitivity, and compliance across analytics artifacts.[cite:37][cite:43]

Recommended governance path:
1. Return to the workspace view.
2. Open the lineage view, if enabled, and trace the flow from raw CSV or raw table to `SalesOrders_Silver`, then to the gold views, and finally to the Power BI report.
3. Point out that lineage helps answer: where did this number come from, and which upstream item would be affected by a change.[cite:43]
4. If the tenant supports sensitivity labels, open the relevant item settings and show how a label can be applied to business data.
5. Explain that governance is not only about security; it is also about auditability, trust, and impact analysis.[cite:37][cite:43]

#### 10.4 Governance explanation
The report looks simple to the business user, but behind it there is a governed chain of objects. The process starts with raw operational data, continues through notebook-based cleaning, moves into curated reporting views, and ends in Power BI. Lineage helps teams trace those dependencies end to end. If a source changes, teams can quickly assess downstream impact. Sensitivity and compliance controls add another layer by helping protect business data as it moves across analytics workflows.[cite:37][cite:43]

#### 10.5 If lineage or labels are unavailable
If the Fabric tenant does not expose full governance features during the live session, use a verbal fallback and the workspace item list to explain the same concept. This still works because the architectural dependency is visible through the objects created in the demo.[cite:31][cite:37]

Fallback approach:
- Show the Lakehouse raw table.
- Show the notebook that produced the silver table.
- Show the SQL view or Warehouse object used by the report.
- Show the final Power BI report.
- Explain that governance connects these objects into an auditable chain.

#### 10.6 Suggested audience questions for the Copilot and governance segment
- How much trust would there be in Copilot answers if region names were never standardized?
- If a sales number looks wrong on the report, where would the team investigate first?
- Should self-service users access raw tables or curated gold views?
- What changes when the same report is used in a regulated environment?

#### 10.7 Suggested timing for this segment
- 48:00 to 49:00: Transition from report visuals to AI-assisted consumption.
- 49:00 to 50:30: Demonstrate Copilot prompts and explain the business-user value.[cite:28]
- 50:30 to 51:45: Switch to lineage and governance explanation.[cite:37][cite:43]
- 51:45 to 52:00: Tie governance back to trusted analytics.

### 11. Close with architecture recap (52-55 min)
End by summarizing the layered architecture and the business value. Microsoft’s medallion and end-to-end Fabric guidance reinforces the value of separating raw, refined, and curated layers for clarity and trust.[cite:53][cite:55][cite:31]

Use this closing summary:
- Bronze: raw file landed in Lakehouse.
- Silver: notebook cleaned and standardized the data.
- Gold: SQL views prepared the business-ready model.
- Consumption: Power BI delivered insights.
- Trust: Copilot and governance improved usability and confidence.

## Recommended audience handout section

This section can be shared after the session as a short checklist.

### Build checklist
- Upload raw CSV to Lakehouse.
- Create raw table.
- Build attached notebook.
- Standardize text columns.
- Parse mixed date formats.
- Clean numeric fields.
- Remove bad records and duplicates.
- Save `SalesOrders_Silver`.
- Create monthly and product gold views.
- Build report visuals in Power BI.
- Demonstrate Copilot or lineage.

## Tips for a smooth live demo

- Keep all items pre-created except the key transformation moments so the audience sees value without waiting through setup screens.
- Use a small dataset because the point of the demo is architecture and flow, not scale testing.
- Practice the notebook cells in advance so the demo highlights cleaning logic rather than debugging syntax.[cite:48][cite:46][cite:31]
- Keep one backup report page ready in case report formatting takes longer than expected.
- Save screenshots of the final report and Lakehouse objects in case the internet or tenant performance is unstable.

## Suggested questions for audience engagement

Use one or two of these during the demo:
- If the business receives this file every day, where should quality rules live?
- Should reporting connect to raw tables or curated gold views?
- What happens to trust in analytics when region names are inconsistent?
- Where can Copilot help, and where is data modeling still essential?

## Post-session sharing note

This guide is intended to be shared as a follow-along reference after the session. Pair it with the dataset artifact so attendees can rebuild the same flow in their own Fabric trial or community tenant.
