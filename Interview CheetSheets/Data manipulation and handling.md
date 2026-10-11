
**Focus:** Pandas + NumPy | Data Manipulation | 3–5 Years Experience
### Q1. You have millions of transaction records. How would you calculate monthly total amount, transaction count, and average amount for each customer?


**Answer:** I would convert the transaction date into datetime, group by customer and month, and calculate multiple aggregations using `groupby().agg()`. This avoids manually iterating through records.
```python
df["Date"] = pd.to_datetime(df["Date"])
result = (df.groupby(["CustomerID", pd.Grouper(key="Date", freq="MS")])
          .agg(TotalAmount=("Amount", "sum"),
               TransactionCount=("Amount", "size"),
               AverageAmount=("Amount", "mean"))
          .reset_index())
```
**Explanation:** `pd.Grouper()` groups transactions by calendar month. `agg()` calculates sum, count, and average in one operation. `size` counts all rows, including missing Amount values, while `mean` ignores missing values.
**Follow-up:** What if Amount contains strings? → Convert using `pd.to_numeric(errors="coerce")` and validate invalid records before aggregation.


### Q2. You merge transaction data with customer master data, but the number of rows increases unexpectedly. Why, and how would you fix it?

**Answer:** The customer master may contain duplicate `CustomerID` values, creating one-to-many or many-to-many matches. I would check duplicate keys and enforce the expected relationship before merging.
```python
duplicates = customers[customers.duplicated("CustomerID", keep=False)]
if not duplicates.empty:
    raise ValueError("Duplicate customer IDs in master")
result = transactions.merge(
    customers, on="CustomerID", how="left",
    validate="many_to_one", indicator=True
)
unmatched = result[result["_merge"] == "left_only"]
```

**Explanation:** `validate="many_to_one"` ensures each transaction matches at most one master record. `indicator=True` helps identify unmatched transactions.
**Follow-up:** Would you simply drop duplicates? → No. I would first investigate whether they are accidental duplicates or legitimate historical versions.


### Q3. You receive transaction data with null amounts, negative amounts, and duplicate transaction IDs. How would you clean it without losing important information?


**Answer:** I would create separate validation rules, retain rejected records for audit, and process only valid transactions. Negative amounts may represent refunds, so I would not reject them without checking business rules.
```python

df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
missing = df["TransactionID"].isna() | df["Amount"].isna()
duplicates = df.duplicated("TransactionID", keep=False)
invalid = missing | duplicates
rejected = df.loc[invalid].copy()
valid = df.loc[~invalid].copy()
```
**Explanation:** `to_numeric()` converts values safely. `duplicated(keep=False)` identifies every occurrence of a duplicate key. Rejected records are retained for investigation.
**Follow-up:** What if two records have the same ID but different timestamps? → Check whether the ID is truly unique or whether a composite key/versioning rule is required.


### Q4. You need a report showing department-wise transaction totals for each month, with months as columns. How would you create it?

**Answer:** I would use `pivot_table()` to aggregate amounts by department and month.
```python
df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M").astype(str)
report = df.pivot_table(
    index="Department", columns="Month",
    values="Amount", aggfunc="sum", fill_value=0
)
report = report.reset_index()
```
**Explanation:** `index` defines rows, `columns` defines month-wise columns, and `aggfunc="sum"` calculates totals. `fill_value=0` fills missing department-month combinations in the report.
**Follow-up:** `pivot()` vs `pivot_table()`? → `pivot()` requires unique row-column combinations; `pivot_table()` can aggregate duplicates.


### Q5. You need to apply different fee rates to one million transactions based on amount and customer type. How would you do it efficiently?


**Answer:** I would use vectorized NumPy conditions rather than Python loops or row-wise `apply()`.
**Business rules:** VIP customers pay 1%; regular customers with Amount ≥ 5000 pay 2%; other regular customers pay 3%.
```python
import numpy as np
conditions = [
    df["CustomerType"].eq("VIP"),
    df["Amount"].ge(5000) & df["CustomerType"].eq("Regular"),
    df["CustomerType"].eq("Regular")
]
rates = np.select(conditions, [0.01, 0.02, 0.03], default=np.nan)
df["Fee"] = df["Amount"] * rates
```
**Explanation:** `np.select()` evaluates conditions in order and selects the first matching rate. Vectorization is generally faster than Python row loops for large numerical datasets.
**Follow-up:** What if CustomerType is unknown? → The rate becomes NaN, so I would flag those records rather than silently applying an incorrect fee.
**Key Interview Tip:** For every scenario, explain: business rule → validation → transformation → output → edge cases.



### Q6. You receive 50 Excel files every day from different departments. Some files have different column names, missing values, and duplicate records. How would you build an automated ETL pipeline?


**Answer:** I would create a reusable pipeline to read all files, standardize column names, validate required fields, remove exact duplicates, combine the data, and save the processed output. Invalid records would be logged separately.


```python
from pathlib import Path
import pandas as pd
frames = []
for file in Path("input").glob("*.xlsx"):
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip().str.lower()
    df = df.rename(columns={"customer_id": "customerid"})
    if not {"customerid", "amount"}.issubset(df.columns):
        print(f"Invalid schema: {file.name}")
        continue
    df["source_file"] = file.name
    frames.append(df)
if not frames:
    raise ValueError("No valid input files")
result = pd.concat(frames, ignore_index=True)
result = result.drop_duplicates()
result.to_parquet("processed.parquet", index=False)
```
**Explanation:** `glob()` finds Excel files, `rename()` standardizes columns, `concat()` combines DataFrames, and Parquet provides efficient storage. In production, I would also validate data types and business keys before loading.
**Follow-up:** What if one file fails? → Log the filename and error, quarantine that file, and continue processing other files if business rules allow.


### Q7. You have a 5 GB CSV file that cannot fit into memory. How would you process it using Pandas?


**Answer:** I would read the file in chunks, select only required columns, optimize data types, and aggregate each chunk instead of loading the complete file.


```python
totals = {}
for chunk in pd.read_csv(
    "transactions.csv",
    usecols=["Department", "Amount"],
    dtype={"Department": "category", "Amount": "float64"},
    chunksize=100_000
):
    summary = chunk.groupby("Department", observed=True)["Amount"].sum()
    for dept, amount in summary.items():
        totals[dept] = totals.get(dept, 0) + amount
result = pd.Series(totals, name="TotalAmount")
```
**Explanation:** `chunksize` processes 100,000 rows at a time. Each chunk is aggregated, so memory usage stays relatively low. Only department totals are stored.
**Follow-up:** What if the dataset is too large even for chunk-based joins? → Consider DuckDB, database-side processing, or PySpark depending on infrastructure and data size.


### Q8. You have two datasets: system transactions and bank transactions. How would you identify missing transactions and amount mismatches?


**Answer:** I would validate transaction IDs, perform an outer join, and classify records as missing from either system or having mismatched amounts.
```python
result = system.merge(
    bank, on="TransactionID", how="outer",
    suffixes=("_system", "_bank"),
    indicator=True, validate="one_to_one"
)
result["Status"] = np.select(
    [
        result["_merge"].eq("left_only"),
        result["_merge"].eq("right_only"),
        result["Amount_system"].ne(result["Amount_bank"])
    ],
    ["Missing in Bank", "Missing in System", "Amount Mismatch"],
    default="Matched"
)
exceptions = result[result["Status"] != "Matched"]
```
**Explanation:** An outer join retains records from both sources. `_merge` identifies missing transactions, while amount comparison identifies mismatches. `validate="one_to_one"` prevents duplicate IDs from silently multiplying rows.
**Follow-up:** What if amounts differ by ₹0.01 due to rounding? → Apply an agreed tolerance, such as `abs(system_amount - bank_amount) <= 0.01`, instead of exact comparison.


### Q9. Your dataset contains multiple updates for the same customer. How would you retain only the latest record for each customer?


**Answer:** I would convert timestamps to datetime, sort records by update time, and keep the latest record per customer.


```python
df["UpdatedAt"] = pd.to_datetime(df["UpdatedAt"], errors="coerce")
latest = (
    df.sort_values("UpdatedAt")
      .drop_duplicates(subset=["CustomerID"], keep="last")
)
```
**Explanation:** Sorting places newer updates after older ones. `drop_duplicates(keep="last")` retains the latest record for each customer.
**Follow-up:** What if two records have identical timestamps? → Define a deterministic tie-breaker, such as version number or ingestion sequence, before deduplication. Missing timestamps should be handled explicitly.


### Q10. Your automated ETL pipeline processes one million records daily. What would you do if some records fail validation or the database becomes unavailable?


**Answer:** I would separate row-level validation failures from pipeline-level failures. Invalid records should go to a rejection file, while database failures should trigger logging, retry mechanisms, and alerts.
```python
import logging
import time
logging.basicConfig(level=logging.INFO)
def load_with_retry(df, load_func, retries=3):
    for attempt in range(retries):
        try:
            load_func(df)
            return
        except (ConnectionError, TimeoutError) as error:
            logging.warning(f"Attempt {attempt + 1}: {error}")
            if attempt == retries - 1:
                logging.exception("Database load failed")
                raise
            time.sleep(2 ** attempt)
```
**Explanation:** The pipeline retries temporary connection failures using exponential backoff. If all retries fail, it raises the error so the scheduler or monitoring system can alert the team.
**Follow-up:** What if retrying inserts duplicate records? → Use idempotent loads, unique transaction keys, and database upserts or transactional staging.
**Interview Tip:** For a 1-hour Uber interview, expect follow-up questions on why you chose a particular approach, how you validate results, and how your solution handles large datasets or production failures.