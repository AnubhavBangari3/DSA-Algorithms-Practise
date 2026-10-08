# DATA TRANSFORMATION + ETL — UBER INTERVIEW CHEATSHEET

**Role:** Python Automation Engineer | **Experience:** 3–5 Years
**Focus:** Python, Pandas, ETL, Excel, CSV, Parquet, Oracle, Automation, Performance
**Interview approach:** Understand the input → clarify business rules → validate → transform → verify → deliver output.

# PART 1 — ETL FUNDAMENTALS

## 1. What is ETL?

ETL stands for Extract, Transform, Load. It is the process of extracting data from one or more sources, cleaning and transforming it according to business requirements, and loading it into a destination such as a database, file, or reporting system.
**Example:** Read employee records from Excel → remove duplicates → handle missing salaries → calculate department-wise average salary → export to CSV.
**ETL Flow:**
`Source → Extract → Inspect → Clean → Validate → Transform → Join → Aggregate → Final Validation → Load → Log/Monitor`
**Interview Answer:** "I first understand the source data and expected output. Then I extract the data, inspect its structure, clean invalid records, apply transformations, join reference datasets if required, perform aggregations, validate the final output, and load it into the destination. I also add logging, exception handling, and data-quality checks."

## 2. ETL vs ELT

| ETL                                  | ELT                                                         |
| ------------------------------------ | ----------------------------------------------------------- |
| Extract → Transform → Load           | Extract → Load → Transform                                  |
| Transform before loading             | Transform inside destination                                |
| Common in Python/Pandas pipelines    | Common in cloud data warehouses                             |
| Useful when data needs preprocessing | Useful when database can handle transformations efficiently |

## 3. ETL vs Data Transformation

| ETL                               | Data Transformation                                            |
| --------------------------------- | -------------------------------------------------------------- |
| Complete data-processing pipeline | One stage of ETL                                               |
| Includes extraction and loading   | Includes cleaning, formatting, calculations, restructuring     |
| Example: Excel → Python → Oracle  | Example: convert date strings, merge columns, calculate totals |

## 4. Types of Data Transformation

| Transformation  | Example                      | Pandas                                     |
| --------------- | ---------------------------- | ------------------------------------------ |
| Filtering       | Keep successful transactions | `df[df["Status"]=="Success"]`              |
| Cleaning        | Remove extra spaces          | `df["Name"].str.strip()`                   |
| Deduplication   | Remove repeated IDs          | `df.drop_duplicates("ID")`                 |
| Type conversion | String → number              | `pd.to_numeric(df["Amount"])`              |
| Date conversion | String → datetime            | `pd.to_datetime(df["Date"])`               |
| Mapping         | Convert status codes         | `df["Status"].map(mapping)`                |
| Calculation     | Revenue = Price × Quantity   | `df["Revenue"]=df["Price"]*df["Quantity"]` |
| Aggregation     | Total sales per region       | `df.groupby("Region")["Revenue"].sum()`    |
| Joining         | Add customer information     | `df.merge(customers,on="CustomerID")`      |
| Reshaping       | Wide → long                  | `df.melt()`                                |
| Normalization   | Standardize column values    | `df["City"].str.strip().str.title()`       |
| Validation      | Check negative amounts       | `df["Amount"].ge(0)`                       |

# PART 2 — COMPLETE ETL PIPELINE

## 5. Scenario: Transform an Employee CSV

**Input:**

| ID                | Name    | Department | Salary | Status   |
| ----------------- | ------- | ---------- | ------ | -------- |
| 1                 | Alice   | IT         | 50000  | Active   |
| 2                 | Bob     | HR         | 40000  | Active   |
| 2                 | Bob     | HR         | 40000  | Active   |
| 3                 | Charlie | IT         | NULL   | Active   |
| 4                 | David   | Sales      | -1000  | Inactive |
| **Requirements:** |         |            |        |          |

1. Read the CSV.
2. Remove duplicate employee IDs.
3. Handle missing salaries.
4. Remove negative salaries.
5. Keep active employees.
6. Calculate average salary by department.
7. Export the result.
   **Code:**

```python
import pandas as pd
df = pd.read_csv("employees.csv")
df.columns = df.columns.str.strip()
required = {"ID", "Name", "Department", "Salary", "Status"}
if not required.issubset(df.columns):
    raise ValueError("Missing required columns")
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Department"] = df["Department"].astype("string").str.strip()
df["Status"] = df["Status"].astype("string").str.strip().str.title()
df = df.drop_duplicates(subset=["ID"])
df = df[df["Status"] == "Active"].copy()
df = df[df["Salary"].isna() | (df["Salary"] >= 0)].copy()
df["Salary"] = df.groupby("Department")["Salary"].transform(
    lambda s: s.fillna(s.median())
)
df = df.dropna(subset=["Salary"])
result = df.groupby("Department", as_index=False).agg(
    AverageSalary=("Salary", "mean"),
    EmployeeCount=("ID", "count")
)
result.to_csv("department_summary.csv", index=False)
print(result)
```

**Important:** Filling missing salaries with a department median is an example business rule. In a real interview, ask whether missing values should be rejected, filled, or retained.
**Interview Explanation:** "I read the source, validate the schema, convert columns into correct data types, clean invalid records, deduplicate by business key, handle missing values according to business rules, aggregate the data, and export the final dataset."

## 6. What Questions Should You Ask Before Transforming Data?

| Question                                                                                                                                                                     | Why It Matters                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| What is the source format?                                                                                                                                                   | CSV, Excel, JSON, database, API           |
| What is the expected output?                                                                                                                                                 | Report, CSV, Excel, Parquet, Oracle table |
| What are the mandatory columns?                                                                                                                                              | Schema validation                         |
| What is the unique identifier?                                                                                                                                               | Deduplication and reconciliation          |
| How should nulls be handled?                                                                                                                                                 | Avoid incorrect assumptions               |
| What should happen to invalid records?                                                                                                                                       | Reject, quarantine, correct, or skip      |
| Are duplicates allowed?                                                                                                                                                      | Business-key validation                   |
| What is the expected data volume?                                                                                                                                            | Memory and performance planning           |
| Is this a one-time or recurring process?                                                                                                                                     | Automation and scheduling                 |
| Does the process need to be rerunnable?                                                                                                                                      | Idempotency and recovery                  |
| What accuracy checks are required?                                                                                                                                           | Row counts, totals, uniqueness            |
| **Best Interview Line:** "Before implementing a transformation, I clarify the source schema, expected output, business rules, data volume, and error-handling requirements." |                                           |

# PART 3 — DATA CLEANING SCENARIOS

## 7. Scenario: Missing Values

**Question:** You receive a file with missing customer names, transaction amounts, and dates. How would you handle it?
**Answer:** "I would first identify missing values and classify columns as mandatory or optional. For mandatory business fields, I would reject or quarantine invalid records. For optional fields, I would fill defaults only if the business rules permit it."

```python
import pandas as pd
df = pd.read_csv("transactions.csv")
print(df.isna().sum())
print(df.isna().mean() * 100)
invalid = df[df[["TransactionID", "Amount", "Date"]].isna().any(axis=1)]
valid = df.dropna(subset=["TransactionID", "Amount", "Date"])
invalid.to_csv("rejected_records.csv", index=False)
```

**Important:** Do not automatically replace missing transaction amounts with zero. Zero and missing can have different business meanings.

## 8. Scenario: Duplicate Records

**Question:** A file contains duplicate transaction IDs. How do you handle them?

```python
duplicates = df[df.duplicated(subset=["TransactionID"], keep=False)]
clean = df.drop_duplicates(subset=["TransactionID"], keep="first")
```

**If latest record should win:**

```python
df["UpdatedAt"] = pd.to_datetime(df["UpdatedAt"])
clean = (
    df.sort_values("UpdatedAt")
      .drop_duplicates(subset=["TransactionID"], keep="last")
)
```

**Interview Answer:** "I first identify the business key and understand whether duplicate records are exact duplicates or multiple versions of the same transaction. Then I apply the appropriate rule, such as keeping the latest record."

## 9. Scenario: Invalid Data Types

**Input:** Amount values = `["1000", "2500", "invalid", "3000"]`

```python
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
invalid = df[df["Amount"].isna()]
valid = df.dropna(subset=["Amount"])
```

**Explanation:** `errors="coerce"` converts invalid numeric values into `NaN`, allowing us to identify and handle them.

## 10. Scenario: Inconsistent Date Formats

**Question:** Dates arrive as strings. How do you convert them?

```python
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
invalid_dates = df[df["Date"].isna()]
```

**If a known format exists:**

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d-%m-%Y",
    errors="coerce"
)
```

**Interview Point:** "I prefer an explicit date format when the source contract defines one. If formats vary, I investigate them rather than silently interpreting ambiguous dates."

## 11. Scenario: Inconsistent Text

**Input:** `" Delhi "`, `"DELHI"`, `"delhi"`

```python
df["City"] = (
    df["City"]
    .astype("string")
    .str.strip()
    .str.lower()
)
```

**Output:** `delhi`, `delhi`, `delhi`

## 12. Scenario: Invalid Business Values

**Question:** How would you validate transaction amounts?

```python
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
valid_mask = df["Amount"].notna() & df["Amount"].ge(0)
valid = df[valid_mask].copy()
rejected = df[~valid_mask].copy()
```

**Important:** Negative amounts may represent refunds or reversals. Confirm business rules before rejecting them.

## 13. Scenario: Missing Columns

```python
required_columns = {"TransactionID", "Amount", "Date"}
missing = required_columns - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {sorted(missing)}")
```

**Interview Answer:** "I validate the schema before processing so that unexpected file structures fail early with meaningful error messages."

# PART 4 — EXCEL PROCESSING

## 14. Scenario: Read an Excel File and Transform Data

```python
import pandas as pd
df = pd.read_excel("sales.xlsx", sheet_name="Sales")
df.columns = df.columns.str.strip()
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df = df.dropna(subset=["Quantity", "Price"])
df["Revenue"] = df["Quantity"] * df["Price"]
df.to_excel("processed_sales.xlsx", index=False)
```

## 15. Scenario: Excel File with Multiple Sheets

**Question:** An Excel workbook has January, February, and March sheets. Combine them.

```python
sheets = pd.read_excel("sales.xlsx", sheet_name=None)
frames = []
for sheet_name, data in sheets.items():
    data = data.copy()
    data["SourceSheet"] = sheet_name
    frames.append(data)
combined = pd.concat(frames, ignore_index=True)
combined.to_csv("combined_sales.csv", index=False)
```

**Interview Explanation:** "`sheet_name=None` returns a dictionary of DataFrames. I process each sheet, optionally attach its source name, and concatenate the results."

## 16. Scenario: Different Column Names Across Excel Sheets

**Input:** One sheet uses `EmpID`, another uses `Employee_ID`.

```python
column_mapping = {
    "EmpID": "EmployeeID",
    "Employee_ID": "EmployeeID",
    "Emp_Name": "EmployeeName"
}
df = df.rename(columns=column_mapping)
```

**Interview Point:** "I standardize source schemas before combining datasets."

## 17. Scenario: Excel Has Extra Header Rows

```python
df = pd.read_excel("report.xlsx", skiprows=3)
```

**If the header is on Excel row 4:**

```python
df = pd.read_excel("report.xlsx", header=3)
```

## 18. Scenario: Write Multiple DataFrames into One Excel Workbook

```python
with pd.ExcelWriter("output.xlsx", engine="openpyxl") as writer:
    clean_df.to_excel(writer, sheet_name="CleanData", index=False)
    rejected_df.to_excel(writer, sheet_name="Rejected", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
```

**Interview Point:** "I can generate an Excel deliverable containing cleaned data, rejected records, and summary reports in separate sheets."

## 19. Pandas vs OpenPyXL

| Pandas                                                                                                                                               | OpenPyXL                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Data analysis and transformation                                                                                                                     | Excel workbook manipulation              |
| Filtering, joins, aggregation                                                                                                                        | Cell formatting, formulas, styles        |
| Reads Excel into DataFrame                                                                                                                           | Works directly with worksheets and cells |
| Best for tabular transformations                                                                                                                     | Best for workbook-level formatting       |
| **Interview Answer:** "I prefer Pandas for data processing and OpenPyXL when I need fine-grained control over Excel cells, formulas, or formatting." |                                          |

# PART 5 — MULTIPLE FILE PROCESSING

## 20. Scenario: Combine 100 CSV Files

**Question:** You receive 100 monthly CSV files. How would you combine them?

```python
from pathlib import Path
import pandas as pd
files = sorted(Path("input").glob("*.csv"))
frames = []
for file in files:
    data = pd.read_csv(file)
    data["SourceFile"] = file.name
    frames.append(data)
combined = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
combined.to_csv("combined.csv", index=False)
```

**Interview Answer:** "I iterate through the files, standardize their structure, attach source metadata for traceability, and combine them using `pd.concat()`."
**Performance Note:** This approach loads all files into memory. For large datasets, use chunking or incremental processing.

## 21. Scenario: Files Have Different Columns

```python
df1 = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
df2 = pd.DataFrame({"ID": [3], "Salary": [50000]})
combined = pd.concat([df1, df2], ignore_index=True)
```

**Result:** Missing columns are filled with `NaN`.
**Interview Point:** "If files have different schemas, I first decide whether to take the union of columns or enforce a strict schema. I don't silently accept missing mandatory columns."

## 22. Scenario: Process Files from a Folder Automatically

```python
from pathlib import Path
import pandas as pd
for file in Path("input").glob("*.csv"):
    try:
        df = pd.read_csv(file)
        df.columns = df.columns.str.strip()
        output = Path("output") / file.name
        output.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output, index=False)
        print(f"Processed: {file.name}")
    except Exception as exc:
        print(f"Failed: {file.name}: {exc}")
```

**Production Improvement:** Use `logging` instead of `print`, maintain processed-file tracking, and avoid treating failed files as successfully completed.

## 23. Scenario: Combine Files and Remove Duplicate IDs

```python
combined = pd.concat(frames, ignore_index=True)
combined = combined.drop_duplicates(subset=["TransactionID"])
```

**Interview Question:** What if duplicate IDs have different amounts?
**Answer:** "I would flag them for investigation or apply an explicitly defined versioning rule. Removing duplicates blindly could lose important information."

# PART 6 — JOINS & DATA RECONCILIATION

## 24. Scenario: Join Transactions with Customer Master

**Transactions:**

| TransactionID                                        | CustomerID   | Amount |
| ---------------------------------------------------- | ------------ | ------ |
| T1                                                   | C1           | 1000   |
| T2                                                   | C2           | 2000   |
| T3                                                   | C3           | 3000   |
| **Customers:**                                       |              |        |
| CustomerID                                           | CustomerName |        |
| ---                                                  | ---          |        |
| C1                                                   | Alice        |        |
| C2                                                   | Bob          |        |
| **Requirement:** Add customer names to transactions. |              |        |

```python
result = transactions.merge(
    customers,
    on="CustomerID",
    how="left",
    validate="many_to_one"
)
```

**Result:** T3 has a missing customer name.
**Interview Answer:** "I use a left join because I want to preserve all transactions. I then identify transactions whose customer IDs are missing from the master dataset."

## 25. Scenario: Find Unmatched Records

```python
result = transactions.merge(
    customers,
    on="CustomerID",
    how="left",
    indicator=True,
    validate="many_to_one"
)
unmatched = result[result["_merge"] == "left_only"]
```

**Interview Point:** "I use merge indicators for reconciliation and exception reporting."

## 26. Scenario: Compare Two Files

**Question:** File A has source transactions, File B has processed transactions. Find missing IDs.

```python
missing = source[
    ~source["TransactionID"].isin(target["TransactionID"])
]
```

**Alternative using merge:**

```python
comparison = source.merge(
    target[["TransactionID"]],
    on="TransactionID",
    how="left",
    indicator=True,
    validate="one_to_one"
)
missing = comparison[comparison["_merge"] == "left_only"]
```

## 27. Scenario: Find Amount Mismatches

```python
comparison = source.merge(
    target,
    on="TransactionID",
    suffixes=("_source", "_target"),
    validate="one_to_one"
)
comparison["Difference"] = (
    comparison["Amount_source"] - comparison["Amount_target"]
)
mismatches = comparison[
    comparison["Difference"].abs() > 0.01
]
```

**Interview Point:** "For financial data, I confirm the allowed tolerance and decimal precision before comparing amounts."

## 28. Scenario: Reconcile Source and Target

**Validation Checks:**

| Check                                                                                              | Purpose                            |
| -------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Source row count                                                                                   | Verify extracted records           |
| Target row count                                                                                   | Detect missing/extra records       |
| Unique key count                                                                                   | Detect duplicates                  |
| Sum of amounts                                                                                     | Detect value differences           |
| Unmatched keys                                                                                     | Identify missing records           |
| Amount mismatches                                                                                  | Identify incorrect transformations |
| Rejected records                                                                                   | Track invalid input                |
| **Important:** Row counts and totals are useful checks but do not prove that every record matches. |                                    |

# PART 7 — GROUPBY, AGGREGATION & REPORTING

## 29. Scenario: Total Revenue by Region

```python
summary = df.groupby("Region", as_index=False).agg(
    TotalRevenue=("Revenue", "sum"),
    TransactionCount=("TransactionID", "count")
)
```

## 30. Scenario: Monthly Sales Report

```python
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
summary = df.groupby("Month", as_index=False)["Revenue"].sum()
summary["Month"] = summary["Month"].astype(str)
```

## 31. Scenario: Top 3 Customers by Revenue

```python
summary = (
    df.groupby("CustomerID", as_index=False)["Revenue"]
      .sum()
      .sort_values("Revenue", ascending=False)
      .head(3)
)
```

## 32. Scenario: Calculate Department Average Without Losing Rows

```python
df["DepartmentAverage"] = (
    df.groupby("Department")["Salary"].transform("mean")
)
```

**Interview Question:** Difference between `agg()` and `transform()`?
**Answer:** "`agg()` produces group-level summaries, while `transform()` returns results aligned with the original rows."

## 33. Scenario: Pivot an Excel Report

**Input:**

| Region | Month | Sales |
| ------ | ----- | ----- |
| North  | Jan   | 100   |
| North  | Feb   | 200   |
| South  | Jan   | 300   |

```python
report = df.pivot_table(
    index="Region",
    columns="Month",
    values="Sales",
    aggfunc="sum",
    fill_value=0
)
```

**Output:**

| Region | Feb | Jan |
| ------ | --- | --- |
| North  | 200 | 100 |
| South  | 0   | 300 |

## 34. Scenario: Convert Wide Excel Data to Long Format

**Input:**

| ID | Jan | Feb |
| -- | --- | --- |
| 1  | 100 | 200 |

```python
result = df.melt(
    id_vars=["ID"],
    value_vars=["Jan", "Feb"],
    var_name="Month",
    value_name="Sales"
)
```

**Output:**

| ID                                                                                                                                                 | Month | Sales |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ----- |
| 1                                                                                                                                                  | Jan   | 100   |
| 1                                                                                                                                                  | Feb   | 200   |
| **Interview Point:** "`melt()` is useful when Excel data is arranged horizontally but downstream processing expects normalized row-based records." |       |       |

# PART 8 — LARGE DATASETS & PERFORMANCE

## 35. Scenario: Process a 5 GB CSV with Limited RAM

**Question:** How would you process a CSV larger than available memory?
**Answer:** "I would avoid loading the entire file. I would select only necessary columns, define efficient data types, read in chunks, perform transformations incrementally, and write results progressively. If joins or global operations exceed memory, I would consider a database, DuckDB, or distributed processing."

```python
import pandas as pd
total = 0
for chunk in pd.read_csv(
    "large.csv",
    usecols=["Amount", "Status"],
    chunksize=100000
):
    chunk["Amount"] = pd.to_numeric(
        chunk["Amount"], errors="coerce"
    )
    valid = chunk[
        (chunk["Status"] == "Success") &
        (chunk["Amount"].notna())
    ]
    total += valid["Amount"].sum()
print(total)
```

**Why this works:** Each chunk is processed separately, and only a running total is retained.

## 36. Scenario: Write Large CSV Output Incrementally

```python
import pandas as pd
from pathlib import Path
output = Path("processed.csv")
if output.exists():
    output.unlink()
first_chunk = True
for chunk in pd.read_csv("large.csv", chunksize=100000):
    chunk = chunk.dropna(subset=["TransactionID"])
    chunk.to_csv(
        output,
        mode="a",
        header=first_chunk,
        index=False
    )
    first_chunk = False
```

**Production Note:** Write to a temporary file first and publish it only after successful completion. Avoid exposing incomplete output.

## 37. Scenario: Optimize DataFrame Memory

```python
print(df.memory_usage(deep=True).sum())
df["Department"] = df["Department"].astype("category")
df["Age"] = pd.to_numeric(df["Age"], downcast="integer")
print(df.memory_usage(deep=True).sum())
```

**Interview Answer:** "I inspect memory usage, reduce unnecessary columns, choose appropriate numeric types, use categorical columns for repeated strings when beneficial, and avoid unnecessary DataFrame copies."

## 38. Scenario: Why Is `apply()` Sometimes Slow?

**Answer:** "`apply()` with a Python function can introduce Python-level overhead. For arithmetic, comparisons, and many string operations, vectorized Pandas or NumPy expressions are generally faster."
**Slower:**

```python
df["Tax"] = df["Amount"].apply(lambda x: x * 0.18)
```

**Usually faster:**

```python
df["Tax"] = df["Amount"] * 0.18
```

## 39. Scenario: Avoid Slow Row-by-Row Loops

**Less efficient:**

```python
for index, row in df.iterrows():
    df.loc[index, "Revenue"] = row["Price"] * row["Quantity"]
```

**Preferred:**

```python
df["Revenue"] = df["Price"] * df["Quantity"]
```

## 40. Scenario: Optimize Large Joins

**Question:** A merge is taking too long. What would you check?

| Check                                                                                                                                                                                                                                 | Reason                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Duplicate join keys                                                                                                                                                                                                                   | Many-to-many joins can multiply rows    |
| Data types                                                                                                                                                                                                                            | Mismatched keys can cause problems      |
| Unnecessary columns                                                                                                                                                                                                                   | Increase memory and processing          |
| Null keys                                                                                                                                                                                                                             | Can create unexpected matches           |
| Join type                                                                                                                                                                                                                             | Outer joins may produce larger outputs  |
| Input size                                                                                                                                                                                                                            | Large datasets may exceed memory        |
| Database indexes                                                                                                                                                                                                                      | Improve SQL-side joins                  |
| Execution location                                                                                                                                                                                                                    | Database join may be better than Pandas |
| **Interview Answer:** "I first check join cardinality, key uniqueness, null keys, and data types. Then I reduce unnecessary columns, evaluate whether the join should happen in the database, and measure memory and execution time." |                                         |
| **Important Pandas Behavior:** Unlike standard SQL joins, Pandas can match null join keys with each other. Handle null keys explicitly when necessary.                                                                                |                                         |

## 41. Scenario: `concat()` Inside a Loop Is Slow

**Avoid repeatedly concatenating:**

```python
result = pd.DataFrame()
for file in files:
    result = pd.concat([result, pd.read_csv(file)])
```

**Preferred:**

```python
frames = [pd.read_csv(file) for file in files]
result = pd.concat(frames, ignore_index=True)
```

**Reason:** Repeated concatenation can repeatedly copy growing datasets.
**Memory Note:** For very large inputs, avoid collecting all DataFrames in memory; use incremental processing.

## 42. Scenario: CSV vs Parquet

| CSV                                 | Parquet                             |
| ----------------------------------- | ----------------------------------- |
| Plain text                          | Binary columnar format              |
| Human-readable                      | Optimized for analytical processing |
| Larger files in many cases          | Often smaller due to compression    |
| Types must be inferred or specified | Stores schema information           |
| Common for data exchange            | Common for analytics and pipelines  |
| **Code:**                           |                                     |

```python
df.to_parquet("output.parquet", index=False)
df = pd.read_parquet("output.parquet")
```

**Interview Answer:** "I use CSV for interoperability and simple data exchange. Parquet is useful for larger analytical datasets because it supports columnar storage, compression, and efficient column selection."

# PART 9 — PRODUCTION ETL DESIGN

## 43. Batch Processing vs Streaming

| Batch                                 | Streaming                                     |
| ------------------------------------- | --------------------------------------------- |
| Process data at intervals             | Process events continuously or near real time |
| Daily Excel/CSV reports               | Live transaction/event processing             |
| Simpler scheduling and recovery       | Lower latency, more complex state handling    |
| Suitable for recurring file pipelines | Suitable for real-time pipelines              |

## 44. Full Load vs Incremental Load

| Full Load                         | Incremental Load                            |
| --------------------------------- | ------------------------------------------- |
| Process entire dataset            | Process only new/changed records            |
| Simpler logic                     | More efficient for large recurring datasets |
| More processing and data transfer | Requires change tracking                    |
| Useful for small datasets         | Useful for production-scale pipelines       |
| **Incremental Load Example:**     |                                             |

```sql
SELECT *
FROM transactions
WHERE updated_at > :last_successful_watermark
  AND updated_at <= :current_run_watermark;
```

**Interview Point:** "For incremental loading, I track a reliable watermark or change-data-capture mechanism and update the checkpoint only after successful processing."

## 45. What Is Idempotency?

**Definition:** Running the same pipeline multiple times with the same input should not create duplicate or incorrect results.
**Problem:** A job fails after inserting 500 records. On retry, it inserts those 500 records again.
**Solutions:**

* Use unique business keys.
* Use database UPSERT/MERGE operations.
* Track processed files or batches.
* Use atomic writes or transactions where supported.
* Update checkpoints only after successful completion.
  **Interview Answer:** "I design recurring pipelines to be rerunnable. For example, I use unique transaction IDs and UPSERT logic so retrying a failed batch doesn't duplicate records."

## 46. How Do You Handle Bad Records?

**Recommended Flow:**
`Input → Validate → Valid Records → Transform → Load`
`                 → Invalid Records → Rejection File/Table`
**Rejected record metadata:**

| Field                                                                                                                                                              | Purpose             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| SourceFile                                                                                                                                                         | Origin of record    |
| RowNumber                                                                                                                                                          | Original position   |
| TransactionID                                                                                                                                                      | Business identifier |
| ErrorReason                                                                                                                                                        | Why rejected        |
| ProcessingTime                                                                                                                                                     | When processed      |
| **Interview Answer:** "I separate invalid records into a rejection dataset with meaningful error reasons. This helps investigation and prevents silent data loss." |                     |

## 47. What Is Data Quality?

**Important Dimensions:**

| Dimension    | Meaning                             | Example                          |
| ------------ | ----------------------------------- | -------------------------------- |
| Completeness | Required data exists                | TransactionID is not null        |
| Uniqueness   | No unwanted duplicates              | Unique TransactionID             |
| Validity     | Correct formats/ranges              | Valid date and amount            |
| Consistency  | Values agree across systems         | Source and target amounts match  |
| Accuracy     | Data reflects actual business facts | Correct settlement amount        |
| Timeliness   | Data arrives when needed            | Daily file arrives before cutoff |

## 48. Logging in ETL

```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logging.info("ETL started")
try:
    df = pd.read_csv("input.csv")
    logging.info("Loaded %s records", len(df))
except Exception:
    logging.exception("ETL failed")
    raise
```

**Log:** Start/end time, file name, records read, valid/rejected counts, output location, errors, and processing duration.

## 49. Error Handling

| Error                                                                                                                                             | Handling                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| File missing                                                                                                                                      | Log and fail or follow defined skip policy  |
| Invalid schema                                                                                                                                    | Reject file with explanation                |
| Corrupt CSV/Excel                                                                                                                                 | Quarantine and investigate                  |
| Invalid data                                                                                                                                      | Reject affected rows                        |
| Database unavailable                                                                                                                              | Retry transient failures                    |
| API timeout                                                                                                                                       | Retry with backoff when safe                |
| Duplicate keys                                                                                                                                    | Apply business-key policy                   |
| Out-of-memory                                                                                                                                     | Chunk or move processing to suitable engine |
| **Interview Point:** "I distinguish transient technical failures from permanent data-quality failures. Retrying malformed input will not fix it." |                                             |

## 50. Retry Logic

```python
import time
def retry_operation(operation, attempts=3):
    for attempt in range(attempts):
        try:
            return operation()
        except (TimeoutError, ConnectionError):
            if attempt == attempts - 1:
                raise
            time.sleep(2 ** attempt)
```

**Interview Answer:** "I retry transient failures with limited attempts and exponential backoff. For database writes or API POST requests, I also consider idempotency so retries don't create duplicates."

## 51. ETL Monitoring

| Metric               | Purpose                 |
| -------------------- | ----------------------- |
| Job status           | Success/failure         |
| Duration             | Detect slow processing  |
| Rows extracted       | Input completeness      |
| Rows rejected        | Data-quality problems   |
| Rows loaded          | Output completeness     |
| Duplicate count      | Source anomalies        |
| Source-target totals | Reconciliation          |
| Last successful run  | Detect missed schedules |

## 52. Scheduling ETL

**Possible options:** Cron, Windows Task Scheduler, Airflow, cloud schedulers, or an existing enterprise orchestration platform.
**Interview Answer:** "For a simple recurring script, I can schedule it using Cron or Task Scheduler. For pipelines with dependencies, retries, monitoring, and multiple stages, I would consider an orchestrator such as Airflow."

# PART 10 — API TO PANDAS ETL

## 53. Scenario: Extract API Data and Save as CSV

```python
import requests
import pandas as pd
response = requests.get(
    "https://api.example.com/transactions",
    timeout=15
)
response.raise_for_status()
data = response.json()
df = pd.json_normalize(data)
df.to_csv("transactions.csv", index=False)
```

**Assumption:** The API returns a list of transaction objects. Real APIs may return nested response structures.

## 54. Scenario: API Pagination

**Question:** An API returns only 100 records per request. How do you extract all records?

```python
import requests
import pandas as pd
records = []
page = 1
while True:
    response = requests.get(
        "https://api.example.com/transactions",
        params={"page": page, "limit": 100},
        timeout=15
    )
    response.raise_for_status()
    batch = response.json()["data"]
    if not batch:
        break
    records.extend(batch)
    page += 1
df = pd.json_normalize(records)
```

**Interview Point:** "I check the API's pagination mechanism, which may use page numbers, offsets, or continuation tokens. For very large results, I process pages incrementally rather than retaining everything in memory."

## 55. API Error Handling

| Status | Meaning             | Action                      |
| ------ | ------------------- | --------------------------- |
| 200    | Success             | Process response            |
| 400    | Bad request         | Correct request             |
| 401    | Unauthorized        | Check authentication        |
| 403    | Forbidden           | Check permissions           |
| 404    | Not found           | Check resource              |
| 429    | Rate limited        | Respect Retry-After/backoff |
| 500    | Server error        | Retry if appropriate        |
| 503    | Service unavailable | Retry with backoff          |

# PART 11 — ORACLE / DATABASE LOADING

## 56. Scenario: Load Pandas Data into a Database

```python
from sqlalchemy import create_engine
engine = create_engine("oracle+oracledb://user:password@host:1521/?service_name=SERVICE")
df.to_sql(
    "TRANSACTIONS",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000
)
```

**Note:** Connection details are illustrative. Use environment variables or a secret manager for credentials, and use appropriate schema/table mappings in production.

## 57. Why Not Always Use Pandas for Everything?

**Answer:** "Pandas is excellent for in-memory transformation, but I wouldn't automatically extract millions of database rows just to perform a simple aggregation. If the database can efficiently filter, join, and aggregate the data, I would push those operations to SQL and transfer only the required result."
**Example:**

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;
```

## 58. SQL vs Pandas

| Operation          | SQL                     | Pandas                                       |
| ------------------ | ----------------------- | -------------------------------------------- |
| Filtering          | `WHERE`                 | Boolean filtering                            |
| Joining            | `JOIN`                  | `merge()`                                    |
| Grouping           | `GROUP BY`              | `groupby()`                                  |
| Aggregation        | `SUM`, `AVG`            | `sum()`, `mean()`                            |
| Sorting            | `ORDER BY`              | `sort_values()`                              |
| Deduplication      | `DISTINCT`              | `drop_duplicates()`                          |
| Conditional values | `CASE WHEN`             | `np.where()`, `np.select()`                  |
| Window functions   | `OVER(PARTITION BY...)` | `groupby().transform()`, `rank()`, `shift()` |

# PART 12 — UBER-STYLE PRACTICAL INTERVIEW SCENARIOS

## 59. Scenario 1: Transform an Unknown Excel File

**Question:** "I give you an Excel file containing 50,000 rows. How will you transform it?"
**Answer:**

1. Understand the required output and business rules.
2. Read the workbook using `pd.read_excel()`.
3. Inspect `shape`, `head()`, `info()`, and `dtypes`.
4. Validate required columns and expected types.
5. Standardize column names and text values.
6. Identify missing, duplicate, and invalid records.
7. Apply filtering, calculations, mappings, and date conversions.
8. Join reference datasets if needed.
9. Aggregate or reshape according to the requirement.
10. Validate row counts, keys, and totals.
11. Export to Excel, CSV, Parquet, or database.
12. Log processing results and rejected records.
    **Key Line:** "I don't begin transforming data blindly. I first understand the expected output and the rules governing invalid or missing records."

## 60. Scenario 2: Multiple Excel Files with Different Formats

**Question:** "You receive 20 Excel files from different teams. Column names and formats are inconsistent. What will you do?"
**Answer:** "I would define a standard target schema, create a mapping for each source format, read the files, normalize column names and data types, validate mandatory fields, and combine the standardized datasets. I would attach source-file information for traceability and generate a rejection report for files or rows that cannot be processed."
**Example Mapping:**

```python
mapping = {
    "Emp ID": "EmployeeID",
    "Employee_ID": "EmployeeID",
    "Employee Name": "EmployeeName",
    "EmpName": "EmployeeName"
}
df = df.rename(columns=mapping)
```

## 61. Scenario 3: Source and Target Counts Don't Match

**Question:** "Your source has 10,000 records, but the output has only 9,500. What will you check?"
**Answer:**

1. Were 500 records rejected because of validation?
2. Were duplicates removed?
3. Did filtering exclude some records?
4. Did an inner join remove unmatched keys?
5. Did an aggregation reduce row count?
6. Did a load operation fail partially?
7. Are all rejected and transformed records accounted for?
   **Important:** "A lower row count is not always an error. Aggregation and filtering can legitimately reduce rows. I compare actual results against expected transformation rules."

## 62. Scenario 4: Pipeline Is Taking Too Long

**Question:** "Your Pandas script used to take 5 minutes, but now takes 40 minutes. What will you do?"
**Answer:**

1. Measure time spent in reading, cleaning, joins, and writing.
2. Check whether input volume increased.
3. Inspect memory usage and data types.
4. Check join keys for duplicates and row multiplication.
5. Replace unnecessary loops with vectorized operations.
6. Load only required columns.
7. Consider chunk processing.
8. Push appropriate aggregations to SQL.
9. Benchmark improvements with representative data.
   **Key Line:** "I optimize based on measured bottlenecks rather than guessing."

## 63. Scenario 5: Duplicate Transactions After Rerunning ETL

**Question:** "Your pipeline failed and was restarted. Now the database has duplicate transactions. How do you prevent this?"
**Answer:** "I would use a stable transaction identifier, enforce uniqueness where possible, and use UPSERT/MERGE instead of unconditional inserts. I would also ensure checkpoints are committed only after successful processing and make retries idempotent."

## 64. Scenario 6: Financial Amount Mismatch

**Question:** "Two files have the same transaction IDs, but some amounts differ by 0.01. How will you investigate?"
**Answer:** "I would join the datasets using transaction IDs, compare amounts using the defined decimal precision and tolerance, and investigate rounding rules, currency precision, source transformations, and data-type conversion. For financial values, I would avoid relying on binary floating-point equality when exact decimal arithmetic is required."
**Python Decimal Example:**

```python
from decimal import Decimal, ROUND_HALF_UP
amount = Decimal("100.005")
rounded = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(rounded)
```

**Output:** `100.01`

## 65. Scenario 7: Large File Causes Memory Error

**Question:** "A 10 GB CSV causes your script to crash. How do you solve it?"
**Answer:** "I would use chunked reading, process only necessary columns, optimize data types, and write intermediate results incrementally. If the transformation requires a global sort or a large join, I would evaluate a database, DuckDB, or distributed engine rather than assuming chunking alone solves everything."

## 66. Scenario 8: Daily Automated Excel Report

**Question:** "Every morning, the team manually combines Excel reports. How would you automate this?"
**Answer:** "I would create a Python script that discovers the expected files, validates their structure, standardizes and combines the data, applies business rules, generates summary reports, writes the output, and logs the results. I would schedule it and implement failure alerts and rerun protection."
**Flow:**
`Daily Excel Files → Python → Schema Validation → Cleaning → Merge → Aggregation → Excel Report → Schedule/Monitor`

## 67. Scenario 9: Data from API + Excel

**Question:** "Customer details are in an API, but transaction data is in Excel. How would you combine them?"
**Answer:** "I would extract customer data from the API, normalize its JSON response, read transactions from Excel, standardize the join keys, merge on CustomerID, identify unmatched transactions, and validate the final dataset."
**Flow:**
`Customer API → JSON → DataFrame`
`Excel Transactions → DataFrame`
`Both DataFrames → Merge → Validate → Output`

## 68. Scenario 10: Explain Your ETL Design

**Question:** "How would you design a reliable Python ETL pipeline?"
**Answer:** "I would separate extraction, validation, transformation, and loading into reusable functions. I would keep business rules configurable, use structured logging, handle invalid records separately, support retries for transient failures, and make database writes idempotent. I would also add unit tests and reconciliation checks."

# PART 13 — REUSABLE ETL CODE TEMPLATE

## 69. Python ETL Script Structure

```python
from pathlib import Path
import logging
import pandas as pd
logging.basicConfig(level=logging.INFO)
REQUIRED = {"TransactionID", "Amount", "Status"}
def extract(path):
    return pd.read_csv(path)
def validate_schema(df):
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    return df
def transform(df):
    df = df.copy()
    df.columns = df.columns.str.strip()
    df = validate_schema(df)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df["Status"] = df["Status"].astype("string").str.strip()
    valid_mask = (
        df["TransactionID"].notna()
        & df["Amount"].notna()
        & df["Status"].eq("Success").fillna(False)
    )
    clean = df.loc[valid_mask].copy()
    rejected = df.loc[~valid_mask].copy()
    return clean, rejected
def load(clean, rejected, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    clean.to_csv(output_dir / "clean.csv", index=False)
    rejected.to_csv(output_dir / "excluded.csv", index=False)
def run_pipeline():
    try:
        logging.info("ETL started")
        raw = extract("transactions.csv")
        clean, rejected = transform(raw)
        load(clean, rejected, "output")
        logging.info(
            "ETL completed: input=%s clean=%s excluded=%s",
            len(raw), len(clean), len(rejected)
        )
    except Exception:
        logging.exception("ETL failed")
        raise
if __name__ == "__main__":
    run_pipeline()
```

**What this demonstrates:**

* Modular ETL design.
* Schema validation.
* Numeric conversion.
* Filtering and transformation.
* Separate output datasets.
* Logging and exception handling.
  **Production Improvements:** Distinguish rejected data from intentionally filtered records, add reason codes, use atomic output publication, implement idempotency, and add tests.

# PART 14 — COMMON INTERVIEW QUESTIONS & ANSWERS

## 70. Top 25 ETL Interview Questions

| Question                               | Short Interview Answer                                                |
| -------------------------------------- | --------------------------------------------------------------------- |
| 1. What is ETL?                        | Extract data, transform it, and load into a target system.            |
| 2. What is data transformation?        | Converting source data into the required structure and format.        |
| 3. ETL vs ELT?                         | ETL transforms before loading; ELT transforms after loading.          |
| 4. How do you handle nulls?            | Follow business rules: reject, fill, or retain.                       |
| 5. How do you remove duplicates?       | Identify business keys and use deduplication rules.                   |
| 6. How do you validate a file?         | Check schema, types, required fields, ranges, and uniqueness.         |
| 7. How do you process Excel?           | `pd.read_excel()` and Pandas transformations.                         |
| 8. How do you combine multiple files?  | Standardize schemas and use `pd.concat()`.                            |
| 9. How do you join datasets?           | `pd.merge()` using appropriate join keys and cardinality.             |
| 10. Inner vs left join?                | Inner keeps matches; left preserves all left rows.                    |
| 11. What is aggregation?               | Summarizing records using sum, count, average, etc.                   |
| 12. `agg()` vs `transform()`?          | Group summary vs row-aligned result.                                  |
| 13. How do you process large CSVs?     | Chunks, column selection, dtype optimization, incremental output.     |
| 14. Why use Parquet?                   | Compressed columnar storage and efficient analytical reads.           |
| 15. How do you optimize Pandas?        | Vectorization, efficient joins, data types, and profiling.            |
| 16. What is incremental loading?       | Processing new or changed records only.                               |
| 17. What is idempotency?               | Safe reruns without duplicate or incorrect effects.                   |
| 18. How do you handle failed records?  | Quarantine with error reasons and source metadata.                    |
| 19. How do you handle pipeline errors? | Logging, exception handling, retries, alerts, recovery.               |
| 20. What is reconciliation?            | Comparing source and target data for consistency.                     |
| 21. How do you automate daily reports? | Reusable Python scripts plus scheduling and monitoring.               |
| 22. How do you load data into Oracle?  | Database connector/SQLAlchemy, batching, transactions.                |
| 23. When use SQL instead of Pandas?    | When database-side processing reduces data transfer or memory use.    |
| 24. How do you test ETL?               | Unit tests, edge cases, schema checks, and reconciliation.            |
| 25. How do you handle API data?        | Requests, pagination, JSON normalization, validation, transformation. |

# PART 15 — IMPORTANT PYTHON/PANDAS OPERATIONS FOR ETL

## 71. Quick Function Reference

| Task                           | Function / Syntax            |
| ------------------------------ | ---------------------------- |
| Read CSV                       | `pd.read_csv()`              |
| Read Excel                     | `pd.read_excel()`            |
| Read Parquet                   | `pd.read_parquet()`          |
| Read SQL                       | `pd.read_sql()`              |
| Read JSON                      | `pd.read_json()`             |
| Flatten JSON                   | `pd.json_normalize()`        |
| Inspect data                   | `df.info()`                  |
| Check dimensions               | `df.shape`                   |
| Check nulls                    | `df.isna().sum()`            |
| Drop nulls                     | `df.dropna()`                |
| Fill nulls                     | `df.fillna()`                |
| Find duplicates                | `df.duplicated()`            |
| Remove duplicates              | `df.drop_duplicates()`       |
| Convert numbers                | `pd.to_numeric()`            |
| Convert dates                  | `pd.to_datetime()`           |
| Convert types                  | `df.astype()`                |
| Filter rows                    | `df.loc[]`, `df.query()`     |
| Rename columns                 | `df.rename()`                |
| Add columns                    | `df.assign()`                |
| Map values                     | `Series.map()`               |
| Conditional values             | `np.where()`                 |
| Join datasets                  | `pd.merge()`                 |
| Combine files                  | `pd.concat()`                |
| Group data                     | `df.groupby()`               |
| Aggregate                      | `df.agg()`                   |
| Row-aligned group calculations | `groupby().transform()`      |
| Pivot report                   | `df.pivot_table()`           |
| Wide to long                   | `df.melt()`                  |
| Sort data                      | `df.sort_values()`           |
| Export CSV                     | `df.to_csv()`                |
| Export Excel                   | `df.to_excel()`              |
| Export Parquet                 | `df.to_parquet()`            |
| Load database                  | `df.to_sql()`                |
| Read in chunks                 | `pd.read_csv(chunksize=...)` |
| Memory usage                   | `df.memory_usage(deep=True)` |

# PART 16 — WHAT TO SAY IN YOUR UBER INTERVIEW

## 72. If Interviewer Asks: "How Comfortable Are You With Data Transformation?"

**Suggested Answer:** "I'm comfortable working with Python for data processing and automation. I understand how to extract data from files or APIs, validate schemas, clean and transform records, join datasets, calculate aggregations, and generate outputs. I also understand the importance of error handling, logging, reconciliation, and performance when working with larger datasets."
**Important:** Adjust this answer to match what you have actually implemented.

## 73. If Interviewer Asks: "Have You Worked on ETL Pipelines?"

**Suggested Answer:** "My background includes Python backend development and processing structured financial messages. In my capital markets work, I dealt with transaction data, validation, exception handling, and reconciliation concepts. I've also worked on a CapitalMarket AI project involving SWIFT message parsing and investigation workflows. Those experiences are relevant to ETL because they involve extracting structured information, applying validation rules, transforming it, and making it available to downstream workflows."
**Important:** This describes transferable experience; it does not claim you built an enterprise-scale Pandas ETL platform.

## 74. If Interviewer Asks: "What If You Don't Know a Particular Transformation?"

**Suggested Answer:** "I would first clarify the expected input and output, break the transformation into smaller steps, test it on sample data, verify edge cases, and then optimize it if required. I'm comfortable learning unfamiliar libraries or functions when the business requirement is clear."

## 75. If Interviewer Asks: "How Would You Improve an Existing Manual Data Process?"

**Suggested Answer:** "I would document the manual steps, identify repetitive transformations, define input/output schemas, and automate them using Python and Pandas. Then I would add validation, logging, exception reporting, scheduling, and checks to ensure the automated output matches the existing business requirements."

# PART 17 — FINAL INTERVIEW REVISION

## 76. The 10 Most Important Scenarios

| Priority | Scenario                            | Must Know                                  |
| -------- | ----------------------------------- | ------------------------------------------ |
| 🔴 1     | Transform an unknown Excel/CSV file | Read → inspect → clean → validate → output |
| 🔴 2     | Handle missing and invalid data     | Nulls, duplicates, types, business rules   |
| 🔴 3     | Combine multiple files              | File iteration, schema mapping, concat     |
| 🔴 4     | Join two datasets                   | Merge, join types, unmatched rows          |
| 🔴 5     | Generate summary reports            | GroupBy, aggregation, pivot                |
| 🔴 6     | Process a very large CSV            | Chunking, memory, vectorization            |
| 🔴 7     | Investigate source-target mismatch  | Reconciliation, counts, totals             |
| 🟠 8     | Automate daily Excel reports        | Script, scheduling, logging                |
| 🟠 9     | Process API data                    | Requests, JSON, pagination                 |
| 🟠 10    | Design a reliable ETL pipeline      | Validation, retries, idempotency           |

## 77. One-Minute ETL Interview Answer

"When I receive a data transformation requirement, I first understand the source, expected output, and business rules. I inspect the data structure and validate mandatory columns, types, and business keys. Then I clean invalid records, handle missing values and duplicates according to defined rules, and apply transformations such as filtering, mapping, joins, calculations, and aggregations. After that, I validate the output using row counts, unique keys, and reconciliation checks. Finally, I export or load the data into the target system. For production pipelines, I also consider logging, exception handling, idempotency, scheduling, and performance optimization."

## 78. Final Preparation Checklist

| Topic                                                                                                                                                                          | Priority         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| Read and transform CSV/Excel                                                                                                                                                   | 🔴 Must Practice |
| Missing values and duplicates                                                                                                                                                  | 🔴 Must Practice |
| Multiple file processing                                                                                                                                                       | 🔴 Must Practice |
| GroupBy and aggregations                                                                                                                                                       | 🔴 Must Practice |
| Merge and reconciliation                                                                                                                                                       | 🔴 Must Practice |
| Pivot and melt                                                                                                                                                                 | 🔴 Must Practice |
| Large datasets and chunking                                                                                                                                                    | 🔴 Must Practice |
| ETL architecture explanation                                                                                                                                                   | 🔴 Must Practice |
| Data validation and rejection handling                                                                                                                                         | 🔴 Must Practice |
| Logging and exception handling                                                                                                                                                 | 🟠 Important     |
| API extraction and pagination                                                                                                                                                  | 🟠 Important     |
| Oracle loading basics                                                                                                                                                          | 🟠 Important     |
| Incremental loads and idempotency                                                                                                                                              | 🟠 Important     |
| Scheduling and monitoring                                                                                                                                                      | 🟠 Important     |
| Parquet                                                                                                                                                                        | 🟠 Important     |
| DuckDB/PySpark overview                                                                                                                                                        | 🟢 Nice to Have  |
| **FINAL RULE:** In every practical ETL question, explain WHAT you will do, WHY you will do it, HOW you will implement it in Python/Pandas, and HOW you will verify the result. |                  |
