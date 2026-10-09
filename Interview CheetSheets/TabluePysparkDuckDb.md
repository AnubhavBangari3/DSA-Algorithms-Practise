# UBER PYTHON AUTOMATION ENGINEER — JD QUICK REVISION
**Topics:** Tableau Basics | PySpark Overview | DuckDB Overview
**Interview:** 1 Hour | **Priority:** Low to Medium
**Objective:** Understand fundamentals, important commands, practical ETL scenarios, and interview-ready answers without spending excessive preparation time.
## PART 1 — TABLEAU BASICS
### 1. What Is Tableau?
Tableau is a business intelligence and data visualization tool used to create interactive dashboards, reports, and analytical visualizations.
**Interview Answer:** "Tableau helps convert structured datasets into interactive visualizations and dashboards. In a Python ETL workflow, Pandas can clean and transform the data, while Tableau can visualize the prepared output for business users."
### 2. Where Does Tableau Fit in an ETL Pipeline?
**Workflow:** Excel/CSV/Oracle → Python/Pandas ETL → Clean Database/Parquet → Tableau → Business Dashboard.
**Explanation:** Python performs extraction, cleaning, validation, and transformation. Tableau connects to the prepared data and presents business insights.
### 3. Important Tableau Concepts
| Concept | Explanation |
|---|---|
| Workbook | Tableau file containing worksheets, dashboards, and stories |
| Worksheet | Individual visualization |
| Dashboard | Collection of visualizations |
| Story | Sequence of sheets/dashboards used to communicate insights |
| Data Source | Database, file, or other connected dataset |
| Dimension | Categorical field such as Department, Region, Customer |
| Measure | Quantitative field such as Sales, Amount, Count |
| Filter | Restricts displayed data |
| Calculated Field | Custom calculation using Tableau expressions |
| Parameter | User-controlled value that can influence calculations or filters |
| Extract | Stored snapshot of data optimized for analysis |
| Live Connection | Queries the underlying data source |
### 4. Dimensions vs Measures
**Dimensions:** Department, Country, TransactionType, CustomerID.
**Measures:** TransactionAmount, Quantity, Revenue, Profit.
**Interview Question:** What is the difference between a dimension and a measure?
**Answer:** "Dimensions categorize data, while measures represent numerical values that can be aggregated."
### 5. Tableau Live Connection vs Extract
| Live Connection | Extract |
|---|---|
| Queries the source database | Uses a stored data snapshot |
| Reflects source updates when queried | Requires refresh to reflect updates |
| Performance depends on source/query | Often improves analytical performance |
| Suitable when source freshness is important | Suitable for optimized reporting and reduced source load |
**Interview Answer:** "I would choose a live connection when freshness is important and the source can handle queries. I would consider an extract when dashboard performance or reducing source load is more important."
### 6. Important Tableau Charts
| Chart | Use Case |
|---|---|
| Bar Chart | Compare amounts across departments |
| Line Chart | Show monthly trends |
| Pie Chart | Show simple part-to-whole breakdowns |
| Scatter Plot | Explore relationships between numeric fields |
| Heatmap | Identify patterns across categories |
| Histogram | Show value distributions |
| KPI Card | Show total records, revenue, failure counts |
### 7. Filters in Tableau
**Common Filters:**
- Data source filters.
- Extract filters.
- Context filters.
- Dimension filters.
- Measure filters.
**Interview Question:** How would you display only failed transactions for a particular month?
**Answer:** "I would apply a date filter and a transaction-status filter to the dashboard."
### 8. Calculated Fields
**Definition:** A calculated field creates a new value using an expression.
**Example:**
```text
IF [Amount] >= 1000 THEN "High"
ELSE "Normal"
END
```
**Another Example:**
```text
SUM([Amount])
```
**Interview Answer:** "Calculated fields help create derived metrics or categories directly within Tableau. For complex or reusable business logic, I would prefer implementing and validating it upstream in Python or SQL."
### 9. Tableau Joins vs Relationships
**Join:** Combines tables at the physical layer using a defined join condition.
**Relationship:** Connects logical tables while allowing Tableau to determine appropriate joins during analysis.
**Interview Answer:** "Relationships can help preserve each table's level of detail, while physical joins directly combine records and can duplicate rows when join keys are not unique."
### 10. Tableau Dashboard Performance
**Question:** A Tableau dashboard is slow. How would you improve it?
**Answer:**
1. Check source query performance.
2. Reduce unnecessary columns and rows.
3. Apply appropriate filters.
4. Pre-aggregate data using Python or SQL.
5. Consider extracts where appropriate.
6. Reduce unnecessary visualizations and expensive calculations.
7. Check join cardinality and data relationships.
### 11. Tableau Interview Scenarios
| Scenario | Expected Answer |
|---|---|
| Show total transaction amounts by department | Bar chart with Department and SUM(Amount) |
| Show monthly transaction trends | Line chart with Month and SUM(Amount) |
| Show failed transaction percentage | Calculate failed count / total count |
| Dashboard is slow | Optimize source queries, extracts, filters, aggregations |
| Data changes daily | Schedule extract refresh or use live connection |
| Duplicate records inflate totals | Validate joins, source keys, and aggregation grain |
| Business wants interactive filters | Add date, region, status, or department filters |
### 12. Top Tableau Interview Questions
| Question | Short Answer |
|---|---|
| What is Tableau? | BI and data visualization tool |
| What is a worksheet? | Individual visualization |
| What is a dashboard? | Collection of visualizations |
| Dimension vs measure? | Categorical vs quantitative |
| What is a calculated field? | Custom calculation or derived field |
| What is a parameter? | User-controlled input |
| What is a filter? | Restricts data shown |
| Live vs extract? | Query source vs stored snapshot |
| What is a relationship? | Logical connection between tables |
| How do you optimize a dashboard? | Optimize source, filters, calculations, extracts, and visuals |
## PART 2 — PYSPARK OVERVIEW
### 13. What Is PySpark?
PySpark is the Python API for Apache Spark, a distributed data-processing engine.
It is used to process large datasets across multiple CPU cores or machines.
**Interview Answer:** "PySpark allows Python developers to process large datasets using Apache Spark. It supports distributed transformations, SQL operations, and scalable ETL pipelines."
### 14. Pandas vs PySpark
| Feature | Pandas | PySpark |
|---|---|---|
| Processing | Primarily single-machine | Distributed |
| Typical use | Small to moderately large datasets fitting available resources | Large-scale datasets and distributed ETL |
| Execution | Generally eager | Lazy for DataFrame transformations |
| API | Pandas DataFrame | Spark DataFrame |
| Scaling | Limited by local resources | Scales across cluster resources |
| Overhead | Usually lower | Distributed execution overhead |
**Interview Question:** Would you use PySpark for 1 million rows?
**Answer:** "Not automatically. I would first evaluate memory usage, file size, transformation complexity, and available infrastructure. Pandas may be sufficient for one million rows."
### 15. Important PySpark Concepts
| Concept | Explanation |
|---|---|
| SparkSession | Main entry point for Spark DataFrame operations |
| Spark DataFrame | Distributed structured dataset |
| Transformation | Defines operations such as filter, select, join |
| Action | Triggers computation, such as count or show |
| Lazy Evaluation | Spark delays execution until an action requires results |
| Partition | Logical subdivision of distributed data |
| Shuffle | Redistribution of data between partitions |
| Cache | Reuse previously computed data |
### 16. Install PySpark
```bash
pip install pyspark
```
### 17. Create a SparkSession
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("UberETL").getOrCreate()
```
### 18. Read CSV and Parquet
```python
df = spark.read.option("header", True).option("inferSchema", True).csv("transactions.csv")
parquet_df = spark.read.parquet("transactions.parquet")
```
**Important:** For production pipelines, explicit schemas are often preferable to schema inference.
### 19. Select and Filter
```python
from pyspark.sql import functions as F
result = df.select("TransactionID", "Amount")
filtered = df.filter(F.col("Amount") > 1000)
```
### 20. Handle Null Values
```python
clean = df.dropna(subset=["TransactionID", "Amount"])
filled = df.fillna({"Description": "Unknown"})
```
**Interview Answer:** "I would apply column-specific business rules rather than blindly dropping or filling all null values."
### 21. GroupBy and Aggregation
```python
summary = df.groupBy("Department").agg(
    F.sum("Amount").alias("TotalAmount"),
    F.count("*").alias("RecordCount")
)
```
### 22. Joins
```python
joined = transactions.join(
    customers,
    on="CustomerID",
    how="left"
)
```
**Interview Follow-up:** What if row counts increase after joining?
**Answer:** "I would check for duplicate join keys and unexpected one-to-many or many-to-many relationships."
### 23. Write Parquet
```python
df.write.mode("overwrite").parquet("output/transactions")
```
**Important:** Spark typically writes a directory containing partition files rather than one single Parquet file.
### 24. Lazy Evaluation
**Question:** What is lazy evaluation in Spark?
**Answer:** "Spark builds an execution plan for transformations and executes it when an action such as `count()`, `show()`, or `collect()` requires results."
**Example:**
```python
filtered = df.filter(F.col("Amount") > 1000)
filtered.show()
```
### 25. What Is a Shuffle?
A shuffle redistributes data across partitions, commonly during joins, aggregations, and certain sorting operations.
**Interview Answer:** "Shuffles can be expensive because they involve moving data between partitions. I would minimize unnecessary shuffles and inspect execution plans for performance issues."
### 26. PySpark Interview Scenarios
| Scenario | Expected Answer |
|---|---|
| Process a very large dataset | Use distributed DataFrames when justified |
| Handle null values | `dropna()`, `fillna()` based on business rules |
| Join two datasets | DataFrame `join()` with validated keys |
| Aggregate by department | `groupBy().agg()` |
| Read Parquet | `spark.read.parquet()` |
| Save transformed data | `df.write.parquet()` |
| Job is slow | Inspect execution plan, partitions, shuffles, skew |
| 1 million rows | Evaluate Pandas first; Spark may be unnecessary |
### 27. Top PySpark Interview Questions
| Question | Short Answer |
|---|---|
| What is PySpark? | Python API for Apache Spark |
| Why use Spark? | Distributed large-scale data processing |
| What is SparkSession? | Entry point for Spark operations |
| What is a Spark DataFrame? | Distributed structured dataset |
| What is lazy evaluation? | Delayed execution until action |
| Transformation vs action? | Defines work vs triggers execution |
| What is partitioning? | Splitting data for parallel processing |
| What is a shuffle? | Data redistribution across partitions |
| Pandas vs PySpark? | Local processing vs distributed processing |
| When use PySpark? | When scale and workload justify distributed execution |
## PART 3 — DUCKDB OVERVIEW
### 28. What Is DuckDB?
DuckDB is an in-process analytical SQL database optimized for OLAP queries.
It can query CSV, Parquet, and Pandas DataFrames using SQL.
**Interview Answer:** "DuckDB is a lightweight analytical SQL database that runs inside an application process. It is useful for fast aggregations, joins, and analytical queries over local files or DataFrames."
### 29. DuckDB vs Pandas vs PySpark
| Feature | Pandas | DuckDB | PySpark |
|---|---|---|---|
| Primary interface | Python DataFrame API | SQL | DataFrame API + SQL |
| Main use | Data manipulation | Analytical SQL | Distributed ETL |
| Execution | Single machine | Single machine, parallel query execution | Distributed-capable |
| Parquet support | Yes | Yes, direct SQL querying | Yes |
| Best fit | Python-centric transformations | SQL-centric local analytics | Cluster-scale processing |
### 30. Install DuckDB
```bash
pip install duckdb
```
### 31. Query a Pandas DataFrame
```python
import duckdb
import pandas as pd
df = pd.DataFrame({
    "Department": ["Tax", "Finance", "Tax"],
    "Amount": [100, 200, 300]
})
result = duckdb.sql("""
    SELECT Department, SUM(Amount) AS TotalAmount
    FROM df
    GROUP BY Department
""").df()
print(result)
```
### 32. Query a Parquet File
```python
import duckdb
result = duckdb.sql("""
    SELECT Department, SUM(Amount) AS TotalAmount
    FROM read_parquet('transactions.parquet')
    GROUP BY Department
""").df()
```
**Interview Answer:** "DuckDB can query Parquet directly, which is useful when I need SQL aggregations without first loading the entire dataset into Pandas."
### 33. Query a CSV File
```python
result = duckdb.sql("""
    SELECT *
    FROM read_csv_auto('transactions.csv')
    LIMIT 10
""").df()
```
### 34. Join Two Parquet Files
```python
result = duckdb.sql("""
    SELECT t.TransactionID, t.Amount, c.CustomerName
    FROM read_parquet('transactions.parquet') t
    LEFT JOIN read_parquet('customers.parquet') c
    ON t.CustomerID = c.CustomerID
""").df()
```
**Interview Scenario:** "You have two large Parquet datasets and need to join them."
**Answer:** "I could use DuckDB to query and join Parquet files directly, select only necessary columns, and materialize only the required results."
### 35. DuckDB vs Oracle
| DuckDB | Oracle |
|---|---|
| In-process analytical database | Enterprise relational database |
| Optimized for analytical workloads | Supports transactional and analytical workloads |
| Convenient for local file analytics | Commonly used as a central enterprise data store |
| Simple embedded deployment | Enterprise database infrastructure |
**Interview Answer:** "DuckDB is useful for local analytical processing, while Oracle is generally used as an enterprise database system."
### 36. Why Use DuckDB with Parquet?
**Advantages:**
- Query Parquet directly using SQL.
- Read selected columns when supported by the query.
- Apply filters and aggregations efficiently.
- Avoid unnecessary conversion of complete files into Pandas.
- Integrate SQL analytics into Python ETL workflows.
**Important:** Performance and memory requirements still depend on query complexity, file layout, and available resources.
### 37. DuckDB Interview Scenarios
| Scenario | Expected Answer |
|---|---|
| Query a 5 GB Parquet file | Use DuckDB SQL with filters and selected columns |
| Aggregate millions of rows | SQL `GROUP BY` and aggregate functions |
| Join two local datasets | DuckDB SQL joins |
| Read CSV | `read_csv_auto()` |
| Work with Pandas DataFrame | Query registered/in-scope DataFrame |
| Compare with PySpark | DuckDB is in-process; Spark supports distributed execution |
| Avoid loading entire file into Pandas | Query files directly and materialize required output |
### 38. Top DuckDB Interview Questions
| Question | Short Answer |
|---|---|
| What is DuckDB? | In-process analytical SQL database |
| What is OLAP? | Online Analytical Processing |
| Why use DuckDB? | Efficient local analytical SQL |
| Can DuckDB read Parquet? | Yes |
| Can DuckDB query CSV? | Yes |
| Can DuckDB query Pandas? | Yes |
| DuckDB vs Pandas? | SQL-centric vs DataFrame-centric |
| DuckDB vs Spark? | In-process vs distributed-capable |
| DuckDB vs Oracle? | Embedded analytics vs enterprise RDBMS |
| When use DuckDB? | Local SQL analytics over files/DataFrames |
## PART 4 — COMBINED UBER INTERVIEW SCENARIOS
### 39. Scenario: Process 2 Million Rows from Excel/CSV
**Question:** "Which tool would you use: Pandas, PySpark, or DuckDB?"
**Answer:** "I would evaluate actual file size, available memory, data types, and transformations. I would start with Pandas if the workload fits comfortably in memory. For SQL-heavy transformations over large CSV or Parquet files, I would consider DuckDB. If the workload requires distributed processing, I would consider PySpark."
### 40. Scenario: Build a Business Dashboard
**Question:** "How would you build a dashboard for a tax team?"
**Answer:** "I would extract source data from Excel or Oracle, clean and transform it using Python/Pandas, validate record counts and totals, load the prepared dataset, and create a Tableau dashboard with KPIs, filters, and trend visualizations."
### 41. Scenario: Large Parquet Dataset
**Question:** "You have a large Parquet file and need only three columns."
**Answer:** "I would select only required columns, using a Parquet-aware reader or DuckDB SQL. I would avoid reading unrelated columns."
### 42. Scenario: Tableau Dashboard Shows Incorrect Totals
**Question:** "The dashboard shows higher totals than the source. What will you check?"
**Answer:** "I would validate source totals, duplicate records, join cardinality, aggregation level, calculated fields, and filters. I would reconcile the dashboard output with the cleaned dataset."
### 43. Scenario: Slow ETL Pipeline
**Question:** "Your Pandas ETL pipeline is slow. Would you immediately migrate to PySpark?"
**Answer:** "No. I would first profile the pipeline, optimize Pandas operations, reduce memory usage, use efficient file formats, and consider DuckDB for SQL-heavy workloads. I would adopt Spark only when workload scale justifies distributed processing."
## PART 5 — FINAL QUICK REVISION
| Priority | Topic | What You Must Know |
|---|---|---|
| 🟠 1 | Tableau | Dimensions/measures, dashboards, filters, charts, live vs extract, calculated fields |
| 🟠 2 | Tableau Scenarios | Dashboard creation, data refresh, incorrect totals, performance |
| 🟢 3 | PySpark | SparkSession, DataFrame, transformations/actions, lazy evaluation, partitions, shuffle |
| 🟢 4 | PySpark Scenarios | Large data, joins, nulls, aggregations, Parquet |
| 🟢 5 | DuckDB | In-process SQL, Pandas integration, CSV/Parquet queries |
| 🟢 6 | DuckDB Scenarios | Large Parquet queries, joins, aggregation, tool selection |
## PART 6 — HONEST EXPERIENCE ANSWERS
**If Asked About Tableau:** "My main experience is in Python-based backend and data-processing workflows. I understand how Tableau connects to prepared datasets and how dashboards use dimensions, measures, filters, and calculated fields. I would need hands-on practice for advanced Tableau development."
**If Asked About PySpark:** "I understand PySpark's distributed processing model, DataFrames, lazy evaluation, joins, aggregations, and Parquet support. My primary practical experience is with Python, so I would use PySpark when the workload justifies distributed processing."
**If Asked About DuckDB:** "I understand DuckDB as an in-process analytical SQL engine that can query Pandas DataFrames, CSV, and Parquet files. I can see its value for SQL-heavy local ETL and analytical processing."
## FINAL INTERVIEW ANSWER — WHICH TOOL WOULD YOU CHOOSE?
"For data cleaning, joins, reshaping, and automation, Pandas would be my primary choice. NumPy would support efficient numerical calculations. DuckDB could help with SQL-heavy analytics over large local files. PySpark would be suitable when distributed processing is genuinely required. Tableau would be used to present the cleaned and validated data through business dashboards. I would choose based on data volume, transformation complexity, performance requirements, and existing infrastructure."
**FINAL ADVICE:** Tableau is part of the main JD, so revise its fundamentals and business scenarios. PySpark and DuckDB are Nice to Have, so focus on conceptual understanding and basic code examples rather than advanced internals.