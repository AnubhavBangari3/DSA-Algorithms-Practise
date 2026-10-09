# NUMPY — UBER PYTHON AUTOMATION INTERVIEW CHEATSHEET
**Role:** Python Automation / Data Transformation Engineer
**Focus:** NumPy, Pandas integration, data manipulation, vectorization, large datasets, ETL scenarios, exception handling, and practical coding.
**Interview Priority:** NumPy is important for numerical transformations and performance. Pandas remains the main tool for tabular Excel/CSV processing.
## PART 1 — EASY: NUMPY FUNDAMENTALS
### 1. What is NumPy?
NumPy (Numerical Python) is a Python library for efficient numerical computation using multidimensional arrays.
It provides fast array operations, mathematical functions, broadcasting, aggregations, and memory-efficient numerical processing.
**Interview Answer:** "NumPy provides efficient numerical arrays and vectorized operations. I use it for numerical transformations, conditional calculations, missing-value handling, and performance optimization alongside Pandas."
### 2. NumPy vs Python List vs Pandas
| Feature | Python List | NumPy Array | Pandas DataFrame |
|---|---|---|---|
| Structure | General-purpose sequence | Homogeneous multidimensional array | Labeled tabular data |
| Data types | Can mix types | Usually one dtype per array | Different dtypes per column |
| Numerical operations | Often require loops | Vectorized operations | Column-wise operations |
| Missing values | `None` | `np.nan`, masks, sentinels | `NaN`, `pd.NA`, `NaT` |
| Best use | General programming | Numerical computation | ETL, Excel, CSV, analytics |
**Interview Answer:** "NumPy is optimized for numerical array operations, while Pandas adds labeled columns, indexes, joins, grouping, and file-processing capabilities."
### 3. Import NumPy
```python
import numpy as np
print(np.__version__)
```
### 4. Creating Arrays
```python
import numpy as np
a = np.array([10, 20, 30])
b = np.array([[1, 2, 3], [4, 5, 6]])
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 2), 7)
sequence = np.arange(0, 10, 2)
evenly_spaced = np.linspace(0, 1, 5)
identity = np.eye(3)
print(a)
print(b)
```
| Function | Purpose |
|---|---|
| `np.array()` | Create array |
| `np.zeros()` | Fill array with zeros |
| `np.ones()` | Fill array with ones |
| `np.full()` | Fill array with specified value |
| `np.arange()` | Generate values at intervals |
| `np.linspace()` | Generate evenly spaced values |
| `np.eye()` | Identity matrix |
| `np.empty()` | Allocate uninitialized array |
### 5. Array Properties
```python
a = np.array([[10, 20, 30], [40, 50, 60]])
print(a.ndim)       # 2
print(a.shape)      # (2, 3)
print(a.size)       # 6
print(a.dtype)      # e.g. int64
print(a.itemsize)   # bytes per element
print(a.nbytes)     # total bytes of array elements
```
| Property | Meaning |
|---|---|
| `ndim` | Number of dimensions |
| `shape` | Size of each dimension |
| `size` | Total number of elements |
| `dtype` | Element data type |
| `itemsize` | Bytes per element |
| `nbytes` | Bytes occupied by array elements |
**Interview Question:** Difference between `shape` and `size`?
**Answer:** "`shape` describes dimensions; `size` gives the total number of elements."
### 6. NumPy Data Types
```python
a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.5], dtype=np.float64)
c = np.array([True, False], dtype=np.bool_)
print(a.dtype)
print(b.dtype)
print(c.dtype)
```
| Type | Use |
|---|---|
| `int8`, `int16`, `int32`, `int64` | Integers |
| `uint8`, `uint16`, `uint32`, `uint64` | Unsigned integers |
| `float32`, `float64` | Floating-point numbers |
| `bool_` | Boolean values |
| `datetime64` | Date/time values |
| `timedelta64` | Time differences |
| String dtypes | Text data |
**Important:** Choose dtypes based on valid value ranges and required numerical precision.
### 7. Type Conversion
```python
a = np.array([10.5, 20.8, 30.2])
b = a.astype(np.int32)
print(b)  # [10 20 30]
```
**Important:** Converting floats to integers truncates fractional parts. It does not round.
### 8. Indexing and Slicing
```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])       # 10
print(a[-1])      # 50
print(a[1:4])     # [20 30 40]
print(a[::2])     # [10 30 50]
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[0, 1])    # 2
print(b[:, 1])    # [2 5]
print(b[1, :])    # [4 5 6]
```
**Interview Question:** What does `a[:, 1]` mean?
**Answer:** "Select all rows and the second column."
### 9. Reshape, Flatten, Ravel
```python
a = np.arange(12)
b = a.reshape(3, 4)
print(b)
print(b.flatten())
print(b.ravel())
```
| Function | Meaning |
|---|---|
| `reshape()` | Change array shape without changing element count |
| `flatten()` | Return flattened copy |
| `ravel()` | Return flattened view when possible, otherwise copy |
**Interview Question:** `flatten()` vs `ravel()`?
**Answer:** "`flatten()` always copies, while `ravel()` avoids copying when possible."
### 10. Copy vs View
```python
a = np.array([10, 20, 30])
view = a[1:]
copy = a[1:].copy()
view[0] = 99
print(a)     # [10 99 30]
print(copy)  # [20 30]
```
**Interview Answer:** "Basic slicing usually returns a view sharing underlying memory, while `.copy()` creates independent data. Boolean and advanced indexing generally create copies."
## PART 2 — MEDIUM: NUMPY DATA MANIPULATION
### 11. Boolean Filtering
```python
amounts = np.array([100, -50, 200, 0, 500])
valid = amounts[amounts > 0]
print(valid)  # [100 200 500]
```
**Interview Scenario:** "How would you filter invalid transaction amounts?"
**Answer:** "I would create a Boolean mask using the business rule and use it to separate valid and invalid records."
### 12. Multiple Conditions
```python
amounts = np.array([100, 500, 1500, 3000])
filtered = amounts[(amounts >= 500) & (amounts <= 2000)]
print(filtered)  # [500 1500]
```
| Operator | Meaning |
|---|---|
| `&` | Element-wise AND |
| `\|` | Element-wise OR |
| `~` | Element-wise NOT |
**Important:** Use parentheses around individual comparisons.
### 13. `np.where()`
```python
amounts = np.array([100, -20, 500])
status = np.where(amounts > 0, "Valid", "Invalid")
print(status)
```
**Syntax:** `np.where(condition, value_if_true, value_if_false)`
**Interview Answer:** "`np.where()` is useful for vectorized conditional transformations without writing a Python loop."
### 14. `np.select()` — Multiple Conditions
```python
amounts = np.array([100, 800, 2500, 6000])
conditions = [
    amounts < 500,
    (amounts >= 500) & (amounts < 3000),
    amounts >= 3000
]
choices = ["Low", "Medium", "High"]
category = np.select(conditions, choices, default="Unknown")
print(category)
```
**Interview Question:** `np.where()` vs `np.select()`?
**Answer:** "`np.where()` is convenient for a single conditional choice; `np.select()` handles multiple ordered conditions."
### 15. Vectorization vs Python Loops
**Slow approach:**
```python
amounts = [100, 200, 300]
taxes = []
for amount in amounts:
    taxes.append(amount * 0.18)
```
**Vectorized approach:**
```python
amounts = np.array([100, 200, 300])
taxes = amounts * 0.18
print(taxes)
```
**Interview Answer:** "Vectorization applies operations to entire arrays using optimized NumPy routines, often reducing Python-level loop overhead."
**Important:** Vectorization is not always faster if it creates large intermediate arrays or uses object dtype.
### 16. Broadcasting
Broadcasting allows NumPy to perform element-wise operations on compatible shapes without manually duplicating smaller arrays.
```python
amounts = np.array([100, 200, 300])
fees = amounts + 10
print(fees)  # [110 210 310]
matrix = np.array([[1, 2, 3], [4, 5, 6]])
adjustment = np.array([10, 20, 30])
print(matrix + adjustment)
```
**Broadcasting Rule:** Compare shapes from the right. Dimensions must match or one must be 1.
**Interview Answer:** "Broadcasting lets NumPy apply compatible smaller arrays or scalar values across larger arrays efficiently."
### 17. Arithmetic Operations
```python
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
```
**Important:** Array arithmetic is element-wise by default.
### 18. Aggregation Functions
```python
a = np.array([10, 20, 30, 40, 50])
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))
print(np.var(a))
print(np.percentile(a, 90))
```
| Function | Meaning |
|---|---|
| `np.sum()` | Sum |
| `np.mean()` | Average |
| `np.median()` | Median |
| `np.min()` | Minimum |
| `np.max()` | Maximum |
| `np.std()` | Standard deviation |
| `np.var()` | Variance |
| `np.percentile()` | Percentile |
### 19. Axis Operations
```python
a = np.array([[10, 20, 30], [40, 50, 60]])
print(np.sum(a, axis=0))  # [50 70 90]
print(np.sum(a, axis=1))  # [60 150]
```
**Interview Answer:** "`axis=0` reduces rows and produces one result per column; `axis=1` reduces columns and produces one result per row."
### 20. Sorting
```python
a = np.array([50, 10, 30, 20])
print(np.sort(a))
print(np.argsort(a))
```
**Difference:** `sort()` returns sorted values; `argsort()` returns indices that would sort the array.
### 21. Unique Values and Counts
```python
a = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(a, return_counts=True)
print(values)  # [1 2 3]
print(counts)  # [1 2 3]
```
**Interview Scenario:** "How would you identify duplicate IDs?"
**Answer:** "I can use `np.unique(return_counts=True)` and select keys with counts greater than one."
### 22. Duplicate Detection
```python
ids = np.array([101, 102, 101, 103, 102])
values, counts = np.unique(ids, return_counts=True)
duplicates = values[counts > 1]
print(duplicates)  # [101 102]
```
**Important:** Identifying duplicates is not the same as deciding which record to retain.
### 23. Concatenate Arrays
```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate([a, b]))
```
**2D Example:**
```python
a = np.array([[1, 2]])
b = np.array([[3, 4]])
print(np.vstack([a, b]))
print(np.hstack([a, b]))
```
| Function | Meaning |
|---|---|
| `np.concatenate()` | Join arrays along an existing axis |
| `np.vstack()` | Stack vertically |
| `np.hstack()` | Stack horizontally |
| `np.stack()` | Join arrays along a new axis |
### 24. Split Arrays
```python
a = np.arange(10)
parts = np.array_split(a, 3)
print(parts)
```
**Interview Use:** Divide numerical data into manageable partitions for independent operations.
**Important:** Splitting an array already loaded in memory does not reduce the memory required to load it initially.
### 25. NumPy Set Operations
```python
a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5])
print(np.intersect1d(a, b))
print(np.union1d(a, b))
print(np.setdiff1d(a, b))
```
| Function | Meaning |
|---|---|
| `np.intersect1d()` | Values present in both arrays |
| `np.union1d()` | Unique values from either array |
| `np.setdiff1d()` | Values in first array but not second |
**Interview Scenario:** "Find transaction IDs present in source but missing in target."
```python
source_ids = np.array([101, 102, 103, 104])
target_ids = np.array([101, 103])
missing = np.setdiff1d(source_ids, target_ids)
print(missing)  # [102 104]
```
## PART 3 — NULL VALUES, INVALID DATA AND DATA QUALITY
### 26. Understanding NaN
`np.nan` represents a missing or undefined floating-point value.
```python
a = np.array([10.0, np.nan, 30.0])
print(np.isnan(a))
```
**Important:** `np.isnan()` is designed for supported numeric and datetime-like dtypes. For mixed object arrays or Pandas nullable types, use `pd.isna()`.
### 27. Detect Null Values
```python
a = np.array([100.0, np.nan, 300.0])
mask = np.isnan(a)
print(mask)
print(np.sum(mask))
```
**Interview Answer:** "I first identify missing values, calculate their frequency, and decide how to handle them based on field importance and business rules."
### 28. Remove NaN Values
```python
a = np.array([10.0, np.nan, 30.0])
clean = a[~np.isnan(a)]
print(clean)
```
**Important:** Removing values from a single column can destroy row alignment with related columns. For tabular datasets, filter entire rows using a shared mask.
### 29. Replace NaN Values
```python
a = np.array([10.0, np.nan, 30.0])
result = np.nan_to_num(a, nan=0.0)
print(result)
```
**Warning:** Never replace missing financial amounts with zero without an approved business rule.
### 30. Mean and Median Imputation
```python
a = np.array([10.0, np.nan, 30.0, 40.0])
mean_value = np.nanmean(a)
median_value = np.nanmedian(a)
filled = np.where(np.isnan(a), median_value, a)
print(filled)
```
**Interview Answer:** "I would use mean or median imputation only when statistically and operationally appropriate. Mandatory financial fields may instead require rejection or investigation."
### 31. NaN-Aware Aggregation
```python
a = np.array([10.0, np.nan, 30.0])
print(np.nansum(a))
print(np.nanmean(a))
print(np.nanmin(a))
print(np.nanmax(a))
```
| Function | Meaning |
|---|---|
| `np.nansum()` | Sum ignoring NaN |
| `np.nanmean()` | Mean ignoring NaN |
| `np.nanmedian()` | Median ignoring NaN |
| `np.nanstd()` | Standard deviation ignoring NaN |
### 32. Detect NaN and Infinity
```python
a = np.array([100.0, np.nan, np.inf, -np.inf, 200.0])
print(np.isnan(a))
print(np.isinf(a))
print(np.isfinite(a))
```
**Interview Answer:** "I use `np.isfinite()` to identify valid finite numeric values and reject or investigate NaN and infinity according to the business rules."
### 33. Handle Invalid Numerical Records
```python
amounts = np.array([100.0, -20.0, np.nan, np.inf, 500.0])
valid_mask = np.isfinite(amounts) & (amounts >= 0)
valid = amounts[valid_mask]
rejected = amounts[~valid_mask]
print("Valid:", valid)
print("Rejected:", rejected)
```
**Important:** Negative amounts may be valid for refunds, adjustments, or reversals. Confirm the business rule.
### 34. Invalid String-to-Number Conversion
NumPy does not provide Pandas-style `errors="coerce"` in `astype()`.
```python
import pandas as pd
values = ["100", "invalid", "250"]
numeric = pd.to_numeric(values, errors="coerce").to_numpy()
print(numeric)
```
**Interview Answer:** "For mixed strings and numbers in tabular data, I prefer Pandas conversion and then use NumPy for efficient numerical operations."
## PART 4 — PRIMARY KEYS, COMPOSITE KEYS AND RECONCILIATION
### 35. Check Primary Key Uniqueness
```python
ids = np.array([101, 102, 103, 103])
is_unique = np.unique(ids).size == ids.size
print(is_unique)  # False
```
**Interview Answer:** "I verify that a primary key has no missing values and no duplicates before relying on it for joins or loading into a constrained database table."
### 36. Find Duplicate Primary Keys
```python
ids = np.array([101, 102, 101, 104, 102])
keys, counts = np.unique(ids, return_counts=True)
duplicate_keys = keys[counts > 1]
print(duplicate_keys)
```
### 37. Validate Composite Keys
**Scenario:** Transaction identity depends on `TradeID` and `TradeDate`.
```python
trade_ids = np.array([101, 101, 102])
trade_dates = np.array(["2026-10-01", "2026-10-02", "2026-10-01"])
keys = np.column_stack([trade_ids.astype(str), trade_dates])
unique_keys = np.unique(keys, axis=0)
print("Unique:", len(unique_keys) == len(keys))
```
**Important:** For real tabular datasets, Pandas `duplicated(subset=["TradeID", "TradeDate"])` is usually clearer and better suited to mixed data types.
### 38. Source vs Target Reconciliation
```python
source = np.array([101, 102, 103, 104])
target = np.array([101, 103, 104])
missing = np.setdiff1d(source, target)
unexpected = np.setdiff1d(target, source)
print("Missing:", missing)
print("Unexpected:", unexpected)
```
**Important:** Set operations ignore duplicate multiplicity. Use key counts or joins when duplicate occurrences matter.
### 39. Amount Difference Validation
```python
source_amounts = np.array([100.00, 250.00, 500.00])
target_amounts = np.array([100.00, 249.99, 500.00])
difference = source_amounts - target_amounts
mismatch_mask = ~np.isclose(
    source_amounts,
    target_amounts,
    rtol=0,
    atol=0.005
)
print(difference)
print(mismatch_mask)
```
**Interview Answer:** "I align records using the correct business key, calculate differences, and apply an approved tolerance. For financial data, I avoid relying on default floating-point tolerance."
### 40. Why Floating-Point Precision Matters
```python
print(0.1 + 0.2 == 0.3)  # False
print(np.isclose(0.1 + 0.2, 0.3))
```
**Interview Answer:** "Binary floating-point values cannot represent every decimal amount exactly. For exact monetary calculations, I would consider Decimal or integer minor units, depending on system requirements."
## PART 5 — LARGE DATASETS AND PERFORMANCE
### 41. Processing More Than One Million Rows
**Interview Scenario:** "How would you process 1 million+ records?"
**Approach:**
1. Inspect file size and schema.
2. Read only required columns.
3. Choose efficient dtypes.
4. Apply vectorized transformations.
5. Process in chunks if memory is insufficient.
6. Validate row counts and rejected records.
7. Write incremental outputs.
8. Use Parquet or a database where appropriate.
**Interview Answer:** "I would avoid unnecessary full-memory copies, use appropriate dtypes and vectorized operations, and process the data incrementally if required."
### 42. Memory Usage
```python
a = np.arange(1_000_000, dtype=np.int64)
b = np.arange(1_000_000, dtype=np.int32)
print(a.nbytes / (1024 ** 2))
print(b.nbytes / (1024 ** 2))
```
**Explanation:** An `int32` array uses approximately half the element-storage memory of an `int64` array.
**Important:** Downcasting is safe only if values fit the target dtype.
### 43. dtype Optimization
```python
a = np.array([10, 20, 30], dtype=np.int64)
if a.min() >= np.iinfo(np.int32).min and a.max() <= np.iinfo(np.int32).max:
    optimized = a.astype(np.int32)
    print(optimized.nbytes)
```
**Interview Answer:** "I choose the smallest safe dtype that preserves required values and precision."
### 44. Chunk Processing with Pandas + NumPy
```python
import pandas as pd
import numpy as np

total_amount = 0.0
processed_rows = 0

for chunk in pd.read_csv(
    "transactions.csv",
    usecols=["Amount"],
    chunksize=100_000
):
    amounts = pd.to_numeric(
        chunk["Amount"], errors="coerce"
    ).to_numpy(dtype=np.float64)
    valid = amounts[np.isfinite(amounts)]
    total_amount += np.sum(valid)
    processed_rows += len(chunk)

print("Rows:", processed_rows)
print("Total:", total_amount)
```
**Important:** Floating-point chunk totals may accumulate rounding differences. For exact monetary totals, use an appropriate exact representation and aggregation strategy.
### 45. NumPy Memory Mapping
Memory mapping lets NumPy access supported binary array data on disk without loading the entire array into RAM.
```python
import numpy as np
arr = np.memmap(
    "numbers.dat",
    dtype=np.float32,
    mode="w+",
    shape=(1_000_000,)
)
arr[:] = np.arange(1_000_000, dtype=np.float32)
arr.flush()
```
**Interview Answer:** "For large binary numerical arrays, NumPy memory mapping can reduce the need to load the entire dataset into memory."
**Important:** `np.memmap` is not a direct CSV/Excel reader.
### 46. NumPy vs Pandas vs PySpark for Large Data
| Tool | Suitable Use |
|---|---|
| NumPy | Efficient in-memory numerical arrays |
| Pandas | In-memory tabular transformation and ETL |
| Pandas chunking | Incremental file processing |
| DuckDB | SQL analytics over files and tables |
| PySpark | Distributed processing across machines |
**Interview Answer:** "One million rows alone does not require Spark. I would evaluate file size, column types, memory requirements, transformations, and infrastructure before selecting the tool."
### 47. Performance Benchmarking
```python
import numpy as np
from time import perf_counter

amounts = np.arange(1_000_000, dtype=np.float64)
start = perf_counter()
result = amounts * 1.18
elapsed = perf_counter() - start
print(f"Elapsed: {elapsed:.6f} seconds")
```
**Best Practice:** Benchmark comparable implementations, account for memory usage, and test correctness before claiming an optimization.
### 48. Avoid Repeated Array Copies
```python
a = np.arange(1_000_000, dtype=np.float64)
a *= 1.05
```
**Explanation:** In-place operations can avoid allocating another full result array.
**Warning:** In-place modifications alter the original array and may affect shared views.
## PART 6 — NUMPY + PANDAS IN REAL ETL
### 49. DataFrame to NumPy
```python
import pandas as pd
df = pd.DataFrame({"Amount": [100, 200, 300]})
amounts = df["Amount"].to_numpy()
print(amounts)
```
### 50. NumPy to DataFrame
```python
import numpy as np
import pandas as pd
arr = np.array([[101, 100], [102, 200]])
df = pd.DataFrame(arr, columns=["TransactionID", "Amount"])
print(df)
```
### 51. Conditional Column with NumPy
```python
df["Category"] = np.where(
    df["Amount"] >= 1000,
    "High",
    "Normal"
)
```
### 52. Multiple Conditions in Pandas
```python
conditions = [
    df["Amount"] < 500,
    (df["Amount"] >= 500) & (df["Amount"] < 1000),
    df["Amount"] >= 1000
]
choices = ["Low", "Medium", "High"]
df["Category"] = np.select(conditions, choices, default="Unknown")
```
### 53. Handle Null Amounts in a DataFrame
```python
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
invalid_mask = df["Amount"].isna()
valid_df = df.loc[~invalid_mask].copy()
rejected_df = df.loc[invalid_mask].copy()
```
**Interview Answer:** "Pandas handles the tabular structure and missing-value validation, while NumPy helps with vectorized numerical calculations."
### 54. Large-File ETL Architecture
**Flow:** `CSV/Excel/API → Raw Staging → Schema Validation → Cleaning → NumPy/Pandas Transformations → Quality Checks → Parquet/Database → Monitoring`
**Important:** NumPy handles numerical operations; it does not replace database loading, orchestration, logging, or file-format libraries.
### 55. Why Use Parquet?
Parquet is a columnar file format that supports compression and efficient column selection.
**Example:**
```python
df.to_parquet("transactions.parquet", index=False)
df = pd.read_parquet("transactions.parquet")
```
**Requirement:** A supported Parquet engine such as PyArrow.
**Interview Answer:** "I would consider Parquet for repeatable analytical workloads because it supports efficient storage and column-oriented access."
## PART 7 — EXCEPTION HANDLING, LOGGING AND ALERTS
### 56. Handle Invalid Numerical Data
```python
import numpy as np

def validate_amounts(values):
    arr = np.asarray(values, dtype=np.float64)
    if not np.isfinite(arr).all():
        raise ValueError("Amounts contain NaN or infinity")
    return arr
```
**Interview Answer:** "I validate numerical inputs and raise meaningful exceptions when mandatory quality rules are violated."
### 57. Catch Exceptions
```python
try:
    amounts = validate_amounts([100, np.nan, 300])
except (ValueError, TypeError) as exc:
    print(f"Validation failed: {exc}")
```
**Important:** In production, use structured logging instead of relying only on `print()`.
### 58. Logging Example
```python
import logging
logging.basicConfig(level=logging.INFO)
try:
    amounts = validate_amounts([100, np.nan])
except ValueError:
    logging.exception("Numerical validation failed")
    raise
```
### 59. Sending Alerts
**Workflow:** `Validation Failure → Log Error → Raise Exception → Notification Service → Operations Team`
**Interview Answer:** "I would capture the exception, log the job ID and error category, send an alert through an approved notification service, and preserve the failure state for the scheduler."
**Possible Integrations:** Email API, Slack API, Teams workflow/webhook, or cloud monitoring.
**Best Practice:** Do not hardcode webhook URLs or API tokens.
### 60. Validation Threshold Alerts
```python
import numpy as np

amounts = np.array([100.0, np.nan, 200.0, np.inf])
invalid_count = np.count_nonzero(~np.isfinite(amounts))
invalid_rate = invalid_count / len(amounts) if len(amounts) else 0

if invalid_rate > 0.10:
    raise ValueError(
        f"Invalid numerical record rate: {invalid_rate:.1%}"
    )
```
**Interview Answer:** "I can define a configurable rejection threshold and fail or alert when the data-quality metric exceeds it."
## PART 8 — EASY CODING QUESTIONS
### 61. Find Maximum and Minimum
```python
a = np.array([10, 40, 20, 80])
print(np.max(a))
print(np.min(a))
```
### 62. Find Second-Largest Distinct Value
```python
a = np.array([10, 30, 20, 30, 50])
unique = np.unique(a)
second_largest = unique[-2] if len(unique) >= 2 else None
print(second_largest)
```
### 63. Reverse an Array
```python
a = np.array([1, 2, 3, 4])
print(a[::-1])
```
### 64. Find Even Numbers
```python
a = np.array([1, 2, 3, 4, 5, 6])
print(a[a % 2 == 0])
```
### 65. Count Values Above a Threshold
```python
a = np.array([100, 500, 1200, 2000])
print(np.count_nonzero(a > 1000))
```
### 66. Replace Negative Values with Zero
```python
a = np.array([100, -20, 50, -5])
print(np.where(a < 0, 0, a))
```
**Note:** This is a generic coding exercise, not a recommended financial-data cleaning rule.
### 67. Normalize Values
```python
a = np.array([10.0, 20.0, 30.0])
minimum = a.min()
maximum = a.max()
normalized = (
    (a - minimum) / (maximum - minimum)
    if maximum != minimum
    else np.zeros_like(a)
)
print(normalized)
```
### 68. Standardize Values
```python
a = np.array([10.0, 20.0, 30.0])
std = a.std()
standardized = (a - a.mean()) / std if std else np.zeros_like(a)
print(standardized)
```
## PART 9 — MEDIUM CODING QUESTIONS
### 69. Find Duplicate IDs
```python
ids = np.array([1, 2, 2, 3, 3, 3])
values, counts = np.unique(ids, return_counts=True)
print(values[counts > 1])
```
### 70. Find Missing IDs Between Datasets
```python
source = np.array([1, 2, 3, 4, 5])
target = np.array([1, 3, 5])
print(np.setdiff1d(source, target))
```
### 71. Categorize Transactions
```python
amounts = np.array([100, 700, 2500])
category = np.select(
    [
        amounts < 500,
        (amounts >= 500) & (amounts < 2000),
        amounts >= 2000
    ],
    ["Low", "Medium", "High"],
    default="Unknown"
)
print(category)
```
### 72. Detect Outliers Using IQR
```python
a = np.array([10, 12, 11, 13, 14, 100])
q1, q3 = np.percentile(a, [25, 75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = a[(a < lower) | (a > upper)]
print(outliers)
```
**Important:** Statistical outliers are not automatically invalid business records.
### 73. Aggregate by Group Without Pandas
```python
groups = np.array(["USD", "EUR", "USD", "EUR"])
amounts = np.array([100, 200, 300, 400])
unique_groups, inverse = np.unique(groups, return_inverse=True)
totals = np.bincount(inverse, weights=amounts)
print(dict(zip(unique_groups, totals)))
```
**Interview Answer:** "NumPy can perform grouped numerical aggregation, but Pandas `groupby()` is usually more readable for tabular ETL."
### 74. Compare Two Arrays with Tolerance
```python
expected = np.array([100.00, 200.00, 300.00])
actual = np.array([100.00, 200.01, 300.00])
mismatch = ~np.isclose(expected, actual, rtol=0, atol=0.005)
print(np.where(mismatch)[0])
```
### 75. Find Missing Integers in a Sequence
```python
a = np.array([1, 2, 4, 6])
expected = np.arange(a.min(), a.max() + 1)
print(np.setdiff1d(expected, a))
```
## PART 10 — HARD: SURYA'S INTERVIEW SCENARIOS
### 76. Scenario: More Than One Million Records
**Question:** "You receive a dataset containing 2 million transactions. How will you process it?"
**Answer:**
1. Inspect file format, size, schema, and business rules.
2. Select only necessary columns.
3. Validate dtypes and missing values.
4. Estimate memory requirements.
5. Use NumPy vectorization for numerical transformations.
6. Use Pandas chunks if the dataset is too large for available memory.
7. Write output incrementally.
8. Reconcile source, valid, and rejected counts.
9. Monitor processing duration and memory.
**Follow-up:** "Would you immediately use PySpark?"
**Answer:** "No. I would evaluate actual data size and transformation complexity first. Two million rows may be manageable with Pandas on an appropriately sized machine."
### 77. Scenario: Primary Key Duplicated
**Question:** "Your input has duplicate transaction IDs. How would you handle it?"
**Answer:**
1. Check key nullability and uniqueness.
2. Identify duplicate IDs.
3. Examine whether records are exact duplicates or conflicting versions.
4. Confirm the business rule.
5. Retain, reject, or consolidate records as required.
6. Log duplicate counts and affected keys.
7. Reconcile output.
**NumPy:**
```python
ids = np.array([101, 102, 101, 103])
keys, counts = np.unique(ids, return_counts=True)
print(keys[counts > 1])
```
### 78. Scenario: Primary Key Exists in Multiple Datasets
**Question:** "Both datasets contain TransactionID. How will you merge them?"
**Answer:** "I would check data types, missing keys, uniqueness, and expected join cardinality. I would use Pandas `merge()` on TransactionID with `validate=` where appropriate and inspect unmatched records."
```python
result = left_df.merge(
    right_df,
    on="TransactionID",
    how="left",
    validate="one_to_one",
    indicator=True,
    suffixes=("_source", "_target")
)
```
**Important:** `validate="one_to_one"` is correct only when both datasets must have unique TransactionID values.
### 79. Scenario: Handle Null Values
**Question:** "You have null values in Amount, Currency, and Description. What will you do?"
**Answer:** "I would not apply one rule to every column. I would identify mandatory fields, investigate null percentages, reject invalid mandatory amounts or currencies, and fill optional descriptions only if approved."
```python
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
rejected = df[df["Amount"].isna()].copy()
valid = df[df["Amount"].notna()].copy()
```
### 80. Scenario: Large CSV vs Excel
**Question:** "You receive a 5 GB Excel/CSV dataset. How will you handle it?"
**Answer:** "For CSV, I would use chunked reading, selective columns, and incremental processing. For Excel, I would consider read-only streaming with a suitable library or converting it into a more efficient processing format. I would use Parquet or database staging for repeated analytical operations."
**Important:** Pandas `read_excel()` does not provide the same `chunksize` argument as `read_csv()`.
### 81. Scenario: Staging Area
**Question:** "How will you process raw data before loading it into the final database?"
**Answer:**
**Flow:** `Source → Raw Staging → Schema Checks → Data Cleaning → Numerical Transformations → Reconciliation → Final Table → Monitoring`
**Explanation:** "I would preserve raw input for traceability, validate and transform in controlled stages, separate rejected records, and load approved records into final tables."
### 82. Scenario: Data Transformation Is Slow
**Question:** "A Python script uses loops to calculate fees for 2 million records. How will you optimize it?"
**Answer:** "I would profile the bottleneck, replace appropriate Python loops with NumPy vectorized operations, minimize copies, optimize dtypes, and benchmark both speed and output correctness."
```python
amounts = np.arange(2_000_000, dtype=np.float64)
fees = np.where(amounts > 1000, amounts * 0.02, amounts * 0.01)
```
### 83. Scenario: Pipeline Exception and Alert
**Question:** "Your ETL job fails due to invalid numerical data. How will you send an exception alert?"
**Answer:** "I would catch the exception at the appropriate boundary, log the failure with job metadata, send an alert through an approved email or messaging API, and re-raise the error so monitoring can mark the job failed. I would keep rejected records and avoid exposing sensitive data in alerts."
### 84. Scenario: Data Reconciliation
**Question:** "Source total is 10,000, but target total is 9,999.99. What will you do?"
**Answer:** "I would verify record alignment, missing records, duplicate keys, currency, decimal precision, rounding rules, and any approved tolerance. I would investigate the difference rather than silently correcting it."
### 85. Scenario: API + Excel + NumPy
**Question:** "An API provides transaction amounts, and Excel contains fee rates. How would you calculate fees?"
**Answer:** "I would validate both schemas, join on the appropriate business key, verify missing rates, and calculate fees using vectorized Pandas/NumPy operations. I would reject or investigate transactions without an applicable fee rule."
## PART 11 — TOP 30 NUMPY INTERVIEW QUESTIONS
| Question | Short Answer |
|---|---|
| 1. What is NumPy? | Numerical computing library with multidimensional arrays |
| 2. What is ndarray? | NumPy's N-dimensional array type |
| 3. NumPy vs list? | Homogeneous arrays and efficient numerical operations vs general-purpose sequence |
| 4. NumPy vs Pandas? | Numerical arrays vs labeled tabular data |
| 5. What is vectorization? | Array-level operations without explicit Python loops |
| 6. What is broadcasting? | Applying operations to compatible array shapes |
| 7. What is `dtype`? | Array element data type |
| 8. What is `shape`? | Dimensions of array |
| 9. What is `ndim`? | Number of axes |
| 10. What is `size`? | Number of elements |
| 11. What is `axis=0`? | Reduce across rows |
| 12. What is `axis=1`? | Reduce across columns |
| 13. `reshape` vs `resize`? | Return reshaped array vs resize an array in place or via `np.resize` with different semantics |
| 14. `flatten` vs `ravel`? | Always copy vs view when possible |
| 15. View vs copy? | Shared memory vs independent memory |
| 16. `np.where()`? | Conditional selection |
| 17. `np.select()`? | Multiple conditional selections |
| 18. `np.unique()`? | Unique values, optional counts |
| 19. `np.isnan()`? | Detect NaN values |
| 20. `np.isfinite()`? | Detect finite values |
| 21. `np.nanmean()`? | Mean ignoring NaN |
| 22. `np.nan_to_num()`? | Replace NaN/infinity with specified/default finite values |
| 23. `np.concatenate()`? | Combine arrays along existing axis |
| 24. `np.stack()`? | Combine arrays along new axis |
| 25. `np.argsort()`? | Indices that sort an array |
| 26. `np.setdiff1d()`? | Unique values in first array absent from second |
| 27. `np.isclose()`? | Compare numbers with configurable tolerance |
| 28. How optimize memory? | Choose safe dtypes, avoid copies, chunk where needed |
| 29. How handle 1M+ rows? | Estimate memory, vectorize, chunk or stage if required |
| 30. How verify NumPy ETL outputs? | Counts, totals, key validation, rejected records, regression tests |
## PART 12 — NUMPY FUNCTIONS QUICK REFERENCE
| Category | Important Functions |
|---|---|
| Array Creation | `array`, `zeros`, `ones`, `full`, `empty`, `arange`, `linspace`, `eye` |
| Array Properties | `shape`, `ndim`, `size`, `dtype`, `itemsize`, `nbytes` |
| Reshaping | `reshape`, `flatten`, `ravel`, `transpose`, `swapaxes` |
| Indexing | Slicing, Boolean masks, fancy indexing |
| Conditional | `where`, `select`, `clip` |
| Missing Values | `isnan`, `isfinite`, `isinf`, `nan_to_num` |
| Aggregation | `sum`, `mean`, `median`, `min`, `max`, `std`, `var`, `percentile` |
| NaN Aggregation | `nansum`, `nanmean`, `nanmedian`, `nanstd` |
| Sorting | `sort`, `argsort`, `partition` |
| Unique | `unique`, `bincount` |
| Combining | `concatenate`, `stack`, `vstack`, `hstack` |
| Splitting | `split`, `array_split` |
| Set Operations | `intersect1d`, `union1d`, `setdiff1d`, `isin` |
| Numerical Comparison | `isclose`, `allclose`, `equal` |
| Memory | `astype`, `memmap`, `ascontiguousarray` |
| Random | `default_rng`, `integers`, `random`, `choice` |
## PART 13 — FINAL UBER INTERVIEW REVISION
### Most Important Topics
| Priority | Topic | Expected Depth |
|---|---|---|
| 🔴 1 | NumPy arrays, dtypes, shape | Explain and code |
| 🔴 2 | Boolean indexing and filtering | Code |
| 🔴 3 | `np.where()` and `np.select()` | Code |
| 🔴 4 | Vectorization and broadcasting | Explain and optimize |
| 🔴 5 | Null/NaN and invalid data | Practical scenarios |
| 🔴 6 | Unique values and duplicate keys | Code |
| 🔴 7 | Aggregations and axis | Explain and code |
| 🔴 8 | NumPy + Pandas transformations | Practical scenarios |
| 🔴 9 | Large datasets and memory | Explain design |
| 🔴 10 | Source/target reconciliation | Practical scenarios |
| 🟠 11 | Copy vs view | Explain |
| 🟠 12 | Floating-point precision | Explain |
| 🟠 13 | Memory mapping | Conceptual |
| 🟠 14 | Exception handling and alerts | Explain workflow |
### One-Minute Interview Answer
"NumPy is a numerical computing library that provides efficient multidimensional arrays and vectorized operations. In Python data-processing workflows, I use NumPy alongside Pandas for conditional transformations, numerical calculations, missing-value detection, aggregations, and performance optimization. For large datasets, I would first assess memory requirements, choose appropriate dtypes, avoid unnecessary copies, and use chunk processing when needed. I would also validate primary keys, null values, duplicate records, and source-to-target totals. For financial or transaction data, I would pay particular attention to precision, rejected records, and business rules."
### Final Checklist
- [ ] Explain NumPy vs Pandas vs Python lists.
- [ ] Create arrays and explain dtypes, shape, size, ndim.
- [ ] Perform indexing, slicing, and Boolean filtering.
- [ ] Write `np.where()` and `np.select()` transformations.
- [ ] Explain vectorization and broadcasting.
- [ ] Handle NaN and infinity correctly.
- [ ] Identify duplicate and missing keys.
- [ ] Explain source-target reconciliation.
- [ ] Perform numerical aggregations.
- [ ] Optimize memory using safe dtypes.
- [ ] Explain processing 1M+ rows.
- [ ] Explain CSV chunking and Parquet usage.
- [ ] Explain exception handling and alerts.
- [ ] Solve practical NumPy coding scenarios.
**FINAL INTERVIEW RULE:** When the interviewer gives you a data scenario, explain the input schema, business rules, transformation logic, validation, output, and failure handling before jumping into code.


# NUMPY PART 2 — REMAINING TOPICS AND UBER INTERVIEW SCENARIOS
**Focus:** Advanced data manipulation, missing-key detection, numerical validation, transaction processing, performance optimization, and practical coding.
**Priority:** Easy → Medium → Hard.
## PART 14 — REMAINING IMPORTANT NUMPY FUNCTIONS
### 86. np.isin() — Check Whether Values Exist in Another Dataset
**Definition:** `np.isin()` checks whether each element of an array exists in a reference array and returns a Boolean mask.
**Syntax:** `np.isin(elements, test_elements)`
**Example:**
```python
import numpy as np
source_ids = np.array([101, 102, 103, 104, 105])
reference_ids = np.array([101, 103, 105])
exists = np.isin(source_ids, reference_ids)
missing_ids = source_ids[~exists]
print(exists)
print(missing_ids)  # [102 104]
```
**Uber Scenario:** "You have 1 million transactions. How would you identify IDs missing from the master database?"
**Answer:** "I would validate key types, use `np.isin()` for an in-memory membership check when appropriate, and isolate unmatched records. For very large database tables, I would prefer an indexed SQL anti-join or a scalable join strategy rather than loading all keys into NumPy."
### 87. np.clip() — Restrict Values to a Range
**Definition:** `np.clip()` restricts values to a minimum and maximum boundary.
**Syntax:** `np.clip(array, min_value, max_value)`
```python
amounts = np.array([100, 500, 1500, 5000])
capped = np.clip(amounts, 200, 2000)
print(capped)  # [200 500 1500 2000]
```
**Uber Scenario:** "A business rule requires a calculated score between 0 and 100."
```python
scores = np.array([-10, 45, 105, 80])
result = np.clip(scores, 0, 100)
print(result)  # [0 45 100 80]
```
**Important:** Do not silently clip original financial amounts unless the business rule explicitly requires it.
### 88. Advanced Boolean Masking — Multiple Validation Rules
**Definition:** Boolean masking filters or modifies records using one or more conditions.
```python
amounts = np.array([100.0, -20.0, np.nan, 500.0, np.inf])
valid_mask = np.isfinite(amounts) & (amounts >= 0)
valid = amounts[valid_mask]
rejected = amounts[~valid_mask]
print("Valid:", valid)
print("Rejected:", rejected)
```
**Uber Scenario:** "How would you reject records with missing amounts, invalid numerical values, or values outside an approved range?"
```python
amounts = np.array([100.0, np.nan, 500.0, 20000.0, -10.0])
valid_mask = np.isfinite(amounts) & (amounts >= 0) & (amounts <= 10000)
print(amounts[valid_mask])
print(amounts[~valid_mask])
```
**Interview Answer:** "I would create a validation mask based on approved business rules, separate valid and rejected records, and preserve the original record identifiers and rejection reasons."
### 89. np.any() and np.all() — Data Validation
**Definition:** `np.any()` checks whether at least one condition is true. `np.all()` checks whether every condition is true.
```python
amounts = np.array([100, 200, -50, 400])
print(np.any(amounts < 0))  # True
print(np.all(amounts >= 0))  # False
```
**Multiple-Column Validation:**
```python
data = np.array([
    [100.0, 10.0],
    [200.0, np.nan],
    [300.0, 30.0]
])
invalid_rows = np.any(~np.isfinite(data), axis=1)
print(invalid_rows)  # [False True False]
```
**Uber Scenario:** "How would you identify rows where any mandatory numerical column contains NaN or infinity?"
**Answer:** "I would use `np.isfinite()` to build a validity mask and `np.any(..., axis=1)` to identify rows containing at least one invalid value."
### 90. np.searchsorted() — Threshold-Based Classification
**Definition:** `np.searchsorted()` finds insertion positions in a sorted array.
**Syntax:** `np.searchsorted(sorted_array, values, side="left")`
```python
thresholds = np.array([500, 1000, 5000])
amounts = np.array([100, 500, 750, 2000, 6000])
bucket_index = np.searchsorted(thresholds, amounts, side="right")
labels = np.array(["Low", "Medium", "High", "Very High"])
categories = labels[bucket_index]
print(categories)
```
**Output:** `['Low' 'Medium' 'Medium' 'High' 'Very High']`
**Uber Scenario:** "Classify millions of transactions into amount bands."
**Answer:** "For fixed, ordered thresholds, I can use `np.searchsorted()` to efficiently assign numerical values to categories."
**Important:** The threshold array must be sorted. `side="right"` places values equal to a threshold in the higher bucket.
### 91. np.diff() — Consecutive Differences
**Definition:** `np.diff()` calculates the difference between consecutive array elements.
```python
balances = np.array([1000, 1200, 1150, 1500])
changes = np.diff(balances)
print(changes)  # [200 -50 350]
```
**Uber Scenario:** "How would you detect sudden changes in daily balances?"
```python
balances = np.array([1000, 1050, 1100, 5000, 5100])
changes = np.diff(balances)
alert_positions = np.where(np.abs(changes) > 1000)[0] + 1
print(alert_positions)  # [3]
```
**Interview Answer:** "I would sort records chronologically, calculate consecutive differences, and flag changes exceeding a configured threshold."
### 92. np.cumsum() — Running Totals
**Definition:** `np.cumsum()` calculates cumulative sums.
```python
transactions = np.array([100, -20, 50, -10])
running_balance = np.cumsum(transactions)
print(running_balance)  # [100 80 130 120]
```
**Uber Scenario:** "Calculate a customer's running account balance."
```python
opening_balance = 1000
transactions = np.array([200, -100, 50])
balances = opening_balance + np.cumsum(transactions)
print(balances)  # [1200 1100 1150]
```
**Important:** Records must be sorted in the required business order. For multiple customers, calculate running totals separately per customer.
### 93. np.round(), np.floor(), np.ceil()
| Function | Purpose | Example |
|---|---|---|
| `np.round()` | Round to specified decimals | `np.round(12.345, 2)` |
| `np.floor()` | Round toward negative infinity | `np.floor(12.9)` |
| `np.ceil()` | Round toward positive infinity | `np.ceil(12.1)` |
```python
values = np.array([12.345, 15.789, -2.7])
print(np.round(values, 2))
print(np.floor(values))
print(np.ceil(values))
```
**Uber Scenario:** "You need to round transaction amounts to two decimals."
**Answer:** "I would first confirm the business rounding rule. NumPy uses floating-point arithmetic and round-to-even behavior for halfway cases; for exact financial rounding requirements, I would use Decimal or integer minor units."
### 94. np.argmax() and np.argmin()
**Definition:** Return the index of the maximum or minimum value.
```python
amounts = np.array([100, 500, 300, 800])
print(np.argmax(amounts))  # 3
print(np.argmin(amounts))  # 0
print(amounts[np.argmax(amounts)])  # 800
```
**Uber Scenario:** "Find the position of the highest transaction amount."
**Important:** These functions return the first matching position when multiple values share the extreme value.
### 95. np.take() and np.put()
**Definition:** `np.take()` selects values by indices. `np.put()` modifies elements at specified flattened indices.
```python
a = np.array([10, 20, 30, 40])
print(np.take(a, [0, 2]))  # [10 30]
np.put(a, [1, 3], [99, 88])
print(a)  # [10 99 30 88]
```
**Interview Use:** Index-based selection and controlled array updates.
### 96. np.repeat() and np.tile()
**Definition:** `repeat()` repeats individual elements. `tile()` repeats an entire array pattern.
```python
a = np.array([1, 2, 3])
print(np.repeat(a, 2))  # [1 1 2 2 3 3]
print(np.tile(a, 2))    # [1 2 3 1 2 3]
```
**Interview Use:** Generate repeated test values or structured numerical patterns.
**Important:** Both may allocate additional memory. Broadcasting is often preferable when actual repetition is unnecessary.
### 97. np.save(), np.load(), np.savez()
**Definition:** Save and load NumPy arrays in NumPy's binary formats.
```python
a = np.array([100, 200, 300])
np.save("amounts.npy", a)
loaded = np.load("amounts.npy", allow_pickle=False)
print(loaded)
np.savez("batch.npz", ids=np.array([1, 2]), amounts=a[:2])
with np.load("batch.npz", allow_pickle=False) as data:
    print(data["ids"])
```
| Format | Purpose |
|---|---|
| `.npy` | Store one NumPy array |
| `.npz` | Store multiple named arrays |
| Parquet | Store analytical tabular data |
**Uber Scenario:** "When would you use `.npy` instead of Parquet?"
**Answer:** "I would use `.npy` for NumPy-specific numerical arrays and Parquet for tabular analytical datasets that need columnar storage and interoperability."
### 98. np.datetime64() — Date Calculations
**Definition:** NumPy supports date and time values using `datetime64`.
```python
dates = np.array(
    ["2026-10-01", "2026-10-03", "2026-10-06"],
    dtype="datetime64[D]"
)
days_between = np.diff(dates).astype("timedelta64[D]")
print(days_between)  # [2 3] days
```
**Uber Scenario:** "Calculate the number of days between consecutive transaction dates."
**Answer:** "I would normalize the date format, sort chronologically, and calculate differences using datetime-aware types."
**Important:** For timezone-aware timestamps and messy source date formats, Pandas is generally more convenient.
### 99. Advanced Broadcasting — Row and Column Adjustments
**Definition:** Broadcasting allows compatible arrays of different shapes to participate in element-wise operations.
```python
amounts = np.array([
    [100, 200, 300],
    [400, 500, 600]
], dtype=float)
column_rates = np.array([0.01, 0.02, 0.03])
fees = amounts * column_rates
print(fees)
```
**Apply a Different Rate to Each Row:**
```python
row_rates = np.array([0.01, 0.05]).reshape(-1, 1)
fees = amounts * row_rates
print(fees)
```
**Uber Scenario:** "Apply different adjustment rates across columns and customer groups."
**Answer:** "I would align the rate array with the intended row or column axis and use broadcasting to avoid explicit Python loops."
### 100. Integer Overflow and Safe Conversion
**Definition:** Integer overflow occurs when a calculation exceeds the representable range of a fixed-width integer dtype.
```python
a = np.array([120], dtype=np.int8)
print(np.iinfo(np.int8).max)  # 127
print(a + np.array([20], dtype=np.int8))  # Overflow/wraparound
```
**Safe Approach:**
```python
a = np.array([120], dtype=np.int8)
result = a.astype(np.int64) + 20
print(result)  # [140]
```
**Uber Scenario:** "A dataset contains very large transaction amounts. How will you avoid numerical overflow?"
**Answer:** "I would inspect expected value ranges, choose safe dtypes, and validate conversions before performing calculations."
## PART 15 — ADDITIONAL UBER CODING SCENARIOS
### 101. Scenario: Find Transactions Missing from Master Data
**Question:** "You have transaction IDs and master IDs. Identify unmatched transactions."
```python
transaction_ids = np.array([101, 102, 103, 104, 105])
master_ids = np.array([101, 103, 105])
missing_mask = ~np.isin(transaction_ids, master_ids)
print(transaction_ids[missing_mask])  # [102 104]
```
**Approach:** Validate key types → check nulls → compare membership → flag unmatched IDs → log rejection count.
### 102. Scenario: Calculate Fees Based on Amount Slabs
**Question:** "Apply a 1% fee below 1000, 2% from 1000 to below 5000, and 3% for 5000 or above."
```python
amounts = np.array([500, 2000, 7000], dtype=float)
rates = np.select(
    [
        amounts < 1000,
        (amounts >= 1000) & (amounts < 5000),
        amounts >= 5000
    ],
    [0.01, 0.02, 0.03],
    default=np.nan
)
fees = amounts * rates
print(fees)  # [5. 40. 210.]
```
**Follow-up:** "What if Amount is missing?"
**Answer:** "I would validate missing and non-finite values before calculation and separate invalid records."
### 103. Scenario: Identify Rows with Invalid Mandatory Values
**Question:** "You have Amount, Tax, and Fee columns. Reject rows containing NaN or infinity."
```python
data = np.array([
    [100, 10, 2],
    [200, np.nan, 4],
    [300, 30, np.inf],
    [400, 40, 8]
], dtype=float)
valid_mask = np.all(np.isfinite(data), axis=1)
valid_rows = data[valid_mask]
rejected_rows = data[~valid_mask]
print(valid_rows)
print(rejected_rows)
```
**Approach:** Validate all mandatory columns → preserve row IDs → isolate rejected records → record reasons.
### 104. Scenario: Compare Source and Target Amounts
**Question:** "Two systems contain transaction amounts. Identify mismatches beyond 0.01."
```python
source = np.array([100.00, 200.00, 300.00])
target = np.array([100.00, 200.02, 299.99])
difference = np.abs(source - target)
mismatch = difference > 0.01 + 1e-9
print(mismatch)  # [False True False]
```
**Important:** This example assumes arrays have already been aligned by transaction ID. In production, align records using keys first and use an approved exact-decimal comparison strategy for financial reconciliation.
### 105. Scenario: Calculate Running Balances
**Question:** "Calculate running balances from transaction changes."
```python
opening_balance = 1000
transactions = np.array([200, -50, -100, 300])
balances = opening_balance + np.cumsum(transactions)
print(balances)  # [1200 1150 1050 1350]
```
**Follow-up:** "What if there are multiple customers?"
**Answer:** "I would group by customer and sort by transaction timestamp. Pandas `groupby().cumsum()` is more suitable for this tabular use case."
### 106. Scenario: Detect Sudden Balance Changes
**Question:** "Alert when a balance changes by more than 1000 between consecutive records."
```python
balances = np.array([1000, 1100, 1200, 4000, 4100])
changes = np.diff(balances)
alert_mask = np.abs(changes) > 1000
alert_indices = np.where(alert_mask)[0] + 1
print(alert_indices)  # [3]
```
**Approach:** Sort by timestamp → calculate differences → compare threshold → log and alert.
### 107. Scenario: Apply Business Thresholds
**Question:** "A calculated risk score must remain between 0 and 100."
```python
scores = np.array([-20, 30, 80, 150])
adjusted_scores = np.clip(scores, 0, 100)
print(adjusted_scores)  # [0 30 80 100]
```
**Follow-up:** "Should we always clip invalid values?"
**Answer:** "No. I would only clip calculated outputs when required by the business rule. Invalid source values should usually be flagged for investigation."
### 108. Scenario: Classify One Million Records
**Question:** "How would you classify transactions into Low, Medium, High, and Critical?"
```python
rng = np.random.default_rng(42)
amounts = rng.integers(0, 10000, size=1_000_000)
thresholds = np.array([1000, 5000, 8000])
labels = np.array(["Low", "Medium", "High", "Critical"])
indices = np.searchsorted(thresholds, amounts, side="right")
categories = labels[indices]
print(categories[:10])
```
**Interview Answer:** "I would use vectorized classification, verify boundary values, and benchmark memory and execution time."
### 109. Scenario: Validate Data Before Downcasting
**Question:** "How will you safely convert int64 values to int32 to save memory?"
```python
values = np.array([100, 200, 300], dtype=np.int64)
limits = np.iinfo(np.int32)
if values.min() >= limits.min and values.max() <= limits.max:
    optimized = values.astype(np.int32)
else:
    optimized = values
print(optimized.dtype)
```
**Approach:** Inspect min/max → check target dtype limits → convert → verify results.
### 110. Scenario: Handle One Million Rows with Multiple Conditions
**Question:** "Flag invalid amounts, missing values, and unusually large values without Python loops."
```python
rng = np.random.default_rng(42)
amounts = rng.normal(1000, 300, 1_000_000)
amounts[100] = np.nan
amounts[200] = -100
amounts[300] = 100000
invalid = ~np.isfinite(amounts)
negative = np.isfinite(amounts) & (amounts < 0)
unusual = np.isfinite(amounts) & (amounts > 10000)
flagged = invalid | negative | unusual
print("Flagged records:", np.count_nonzero(flagged))
```
**Interview Answer:** "I would build vectorized Boolean masks for each validation rule, combine them, and produce a rejected-record report with reason codes."
## PART 16 — HARD INTERVIEW FOLLOW-UP QUESTIONS
### 111. Why is NumPy generally faster than Python loops?
**Answer:** "NumPy performs many numerical operations in optimized compiled code and reduces Python-level loop overhead. However, performance depends on dtype, array layout, intermediate allocations, and the operation."
### 112. Can NumPy process a 10 GB CSV directly without loading it fully?
**Answer:** "NumPy is not the best general-purpose tool for streaming large CSV files. I would use Pandas chunking or another streaming reader, perform NumPy operations on each chunk, and write results incrementally."
### 113. Is NumPy always more memory-efficient than Pandas?
**Answer:** "Not necessarily. NumPy is efficient for homogeneous numerical arrays, but converting mixed tabular data to NumPy may create object arrays or copies. Pandas also provides efficient column-specific dtypes."
### 114. What happens when broadcasting shapes are incompatible?
**Answer:** "NumPy raises a ValueError because the dimensions cannot be broadcast together."
### 115. Why might vectorization consume more memory?
**Answer:** "Vectorized expressions may create temporary arrays. I would inspect intermediate allocations, use safe in-place operations where appropriate, and process chunks if necessary."
### 116. How do you handle exact monetary calculations?
**Answer:** "I would use Decimal or integer minor units according to business precision requirements, rather than assuming float64 is exact for decimal currency values."
### 117. How would you validate one million transaction IDs?
**Answer:** "I would check nulls, uniqueness, type consistency, duplicates, and reference-data membership. For large datasets, I would consider SQL constraints and indexed joins rather than loading everything into arrays."
### 118. What if NumPy calculations return NaN unexpectedly?
**Answer:** "I would inspect input data, invalid operations, division by zero, dtype conversions, and missing-value propagation. I would validate finite outputs and log affected records."
### 119. How would you test a NumPy transformation?
**Answer:** "I would test normal values, nulls, boundary values, negative values, overflow cases, empty arrays, and expected output shapes using pytest and NumPy testing assertions."
```python
import numpy as np
def calculate_fee(amounts):
    return np.asarray(amounts) * 0.02
np.testing.assert_allclose(
    calculate_fee([100, 200]),
    [2, 4]
)
```
### 120. How would you explain a complete NumPy ETL workflow?
**Answer:** "I would read the source through Pandas or a database connector, validate schema and business keys, use NumPy for efficient numerical transformations, separate invalid records, reconcile source and target totals, write approved output, and log metrics and failures."
## PART 17 — QUICK REVISION TABLE
| Function | Interview Use |
|---|---|
| `np.isin()` | Check key membership |
| `np.clip()` | Enforce approved numerical bounds |
| `np.any()` | Detect at least one failed condition |
| `np.all()` | Verify every required condition |
| `np.searchsorted()` | Threshold-based classification |
| `np.diff()` | Consecutive differences |
| `np.cumsum()` | Running totals |
| `np.round()` | Numerical rounding |
| `np.floor()` | Round downward |
| `np.ceil()` | Round upward |
| `np.argmax()` | Position of maximum |
| `np.argmin()` | Position of minimum |
| `np.take()` | Index-based selection |
| `np.put()` | Index-based updates |
| `np.repeat()` | Repeat individual values |
| `np.tile()` | Repeat array patterns |
| `np.save()` | Save NumPy array |
| `np.load()` | Load NumPy array |
| `np.savez()` | Save multiple arrays |
| `np.datetime64()` | Date/time arrays |
| `np.iinfo()` | Integer dtype limits |
| `np.finfo()` | Floating-point dtype information |
## PART 18 — FINAL UBER NUMPY PREPARATION CHECKLIST
- [ ] Explain NumPy arrays, dimensions, dtypes, and memory.
- [ ] Explain NumPy vs Pandas.
- [ ] Write Boolean filtering and conditional transformations.
- [ ] Use `np.where()` and `np.select()`.
- [ ] Handle null, NaN, infinity, and invalid values.
- [ ] Validate duplicate and missing primary keys.
- [ ] Use `np.isin()` for membership checks.
- [ ] Use `np.any()` and `np.all()` for validation.
- [ ] Use `np.diff()` and `np.cumsum()` for numerical scenarios.
- [ ] Use `np.searchsorted()` for threshold-based classification.
- [ ] Explain vectorization and broadcasting.
- [ ] Explain copy vs view and memory optimization.
- [ ] Explain safe dtype conversion and numerical overflow.
- [ ] Explain floating-point precision in financial data.
- [ ] Explain 1M+ record processing.
- [ ] Explain chunking, staging, and Parquet integration.
- [ ] Explain error handling, logging, and alerts.
- [ ] Solve practical NumPy + Pandas coding scenarios.
**FINAL INTERVIEW STRATEGY:** For every data transformation scenario, explain the business requirement, source schema, key validation, null handling, transformation logic, performance considerations, output validation, and exception handling. Then write the code.