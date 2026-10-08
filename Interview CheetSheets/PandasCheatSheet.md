# PANDAS INTERVIEW CHEATSHEET — EASY → MEDIUM → HARD

**Focus:** Python, Pandas, Data Cleaning, Transformation, ETL, Excel, CSV, APIs, Performance Optimization
**Interview Level:** 3–5 Years Experience
**Import:**

```python
import pandas as pd
import numpy as np
```

# PART 1: EASY — PANDAS FUNDAMENTALS

## 1. What is Pandas?

Pandas is a Python library used for reading, cleaning, transforming, analyzing, and manipulating structured data.
**Main Data Structures:**

* Series: One-dimensional labeled data.
* DataFrame: Two-dimensional tabular data containing rows and columns.

```python
s = pd.Series([10, 20, 30], name="numbers")
print(s)
# 0    10
# 1    20
# 2    30
```

```python
df = pd.DataFrame({
    "Name": ["Amit", "Riya", "John", "Sara", "Raj"],
    "Age": [25, 30, 28, 35, 30],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 80000, 65000]
})
print(df)
```

**Dataset used throughout the cheatsheet:**

| Name | Age | Department | Salary |
| ---- | --: | ---------- | -----: |
| Amit |  25 | IT         |  50000 |
| Riya |  30 | HR         |  60000 |
| John |  28 | IT         |  55000 |
| Sara |  35 | Finance    |  80000 |
| Raj  |  30 | HR         |  65000 |

## 2. Creating DataFrames

**From dictionary:**

```python
df = pd.DataFrame({"Name": ["A", "B"], "Salary": [100, 200]})
```

**From list of dictionaries:**

```python
data = [
    {"Name": "Amit", "Salary": 50000},
    {"Name": "Riya", "Salary": 60000}
]
df = pd.DataFrame(data)
```

**From list of lists:**

```python
df = pd.DataFrame(
    [["Amit", 25], ["Riya", 30]],
    columns=["Name", "Age"]
)
```

**From Series:**

```python
s = pd.Series([100, 200, 300], name="Salary")
df = s.to_frame()
```

## 3. Reading Files

```python
df = pd.read_csv("employees.csv")
df = pd.read_excel("employees.xlsx")
df = pd.read_excel("employees.xlsx", sheet_name="Sheet1")
df = pd.read_parquet("employees.parquet")
df = pd.read_json("employees.json")
```

**Read selected columns:**

```python
df = pd.read_csv("employees.csv", usecols=["Name", "Salary"])
```

**Read only first 100 rows:**

```python
df = pd.read_csv("employees.csv", nrows=100)
```

**Read with specified data types:**

```python
df = pd.read_csv("employees.csv", dtype={"EmployeeID": "string"})
```

**Read dates automatically:**

```python
df = pd.read_csv("employees.csv", parse_dates=["JoiningDate"])
```

**Read Excel with multiple sheets:**

```python
sheets = pd.read_excel("employees.xlsx", sheet_name=None)
# Returns dictionary: {"Sheet1": DataFrame, "Sheet2": DataFrame}
```

## 4. Writing Files

```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_parquet("output.parquet", index=False)
df.to_json("output.json", orient="records")
```

**Interview Tip:** `index=False` prevents Pandas from writing the DataFrame index as an extra column.

## 5. Inspecting Data

```python
df.head()                  # First 5 rows
df.head(10)                # First 10 rows
df.tail()                  # Last 5 rows
df.shape                   # (5, 4)
df.columns                 # Column names
df.index                   # Row index
df.dtypes                  # Data types
df.info()                  # Columns, types, non-null counts
df.describe()              # Numeric statistics
df.describe(include="all") # All columns
df.sample(2)               # Random 2 rows
df.size                    # Total cells = 20
df.ndim                    # Number of dimensions = 2
df.empty                   # True if DataFrame has zero rows or columns
```

**Interview Question: Difference between `shape`, `size`, and `len()`?**

```python
df.shape   # (5, 4) -> Rows and columns
df.size    # 20 -> Total elements
len(df)    # 5 -> Number of rows
```

## 6. Selecting Columns

```python
df["Name"]                     # Single column -> Series
df[["Name"]]                   # Single column -> DataFrame
df[["Name", "Salary"]]         # Multiple columns
df.Name                        # Attribute access (less reliable)
```

**Interview Tip:** Prefer `df["Name"]` because it works with spaces and avoids conflicts with DataFrame methods.

## 7. Selecting Rows — loc vs iloc

**loc = Label-based selection.**
**iloc = Integer-position-based selection.**

```python
df.loc[0]                      # Row with index label 0
df.iloc[0]                     # First row by position
df.loc[0:2]                    # Labels 0, 1, 2 (inclusive)
df.iloc[0:2]                   # Positions 0, 1 (exclusive end)
df.loc[0, "Name"]              # Amit
df.iloc[0, 0]                  # Amit
df.loc[:, ["Name", "Salary"]]   # Selected columns
df.iloc[:, 0:2]                # First two columns
```

**Important:** After filtering, row labels may differ from row positions.

```python
filtered = df[df["Salary"] > 55000]
print(filtered.index.tolist())
# [1, 3, 4]
print(filtered.iloc[0]["Name"])
# Riya
print(filtered.loc[1, "Name"])
# Riya
```

## 8. Filtering Rows

**Single condition:**

```python
df[df["Salary"] > 60000]
# Sara, Raj
```

**Multiple conditions — AND:**

```python
df[(df["Age"] > 25) & (df["Salary"] > 60000)]
# Sara, Raj
```

**Multiple conditions — OR:**

```python
df[(df["Department"] == "IT") | (df["Salary"] > 70000)]
# Amit, John, Sara
```

**NOT condition:**

```python
df[~(df["Department"] == "IT")]
# Riya, Sara, Raj
```

**Using isin():**

```python
df[df["Department"].isin(["IT", "HR"])]
```

**Using between():**

```python
df[df["Salary"].between(55000, 65000)]
# John, Riya, Raj
```

**Using query():**

```python
df.query("Salary > 60000 and Age >= 30")
# Sara, Raj
```

**Interview Tip:** Use `&`, `|`, and `~` for element-wise boolean conditions. Wrap each comparison in parentheses.

## 9. Sorting

```python
df.sort_values("Salary")                         # Ascending
df.sort_values("Salary", ascending=False)        # Descending
df.sort_values(["Department", "Salary"])          # Multiple columns
df.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
)
df.sort_index()                                  # Sort by index
```

**Top 3 highest salaries:**

```python
df.nlargest(3, "Salary")
# Sara 80000, Raj 65000, Riya 60000
```

**Bottom 2 salaries:**

```python
df.nsmallest(2, "Salary")
# Amit 50000, John 55000
```

## 10. Adding Columns

```python
df["Bonus"] = df["Salary"] * 0.10
df["AnnualSalary"] = df["Salary"] * 12
df["Senior"] = df["Age"] >= 30
```

**Using assign():**

```python
df = df.assign(
    Bonus=df["Salary"] * 0.10,
    AnnualSalary=df["Salary"] * 12
)
```

**Conditional column:**

```python
df["Category"] = np.where(
    df["Salary"] >= 60000,
    "High",
    "Low"
)
```

**Multiple conditions:**

```python
conditions = [
    df["Salary"] >= 70000,
    df["Salary"] >= 55000
]
choices = ["High", "Medium"]
df["Category"] = np.select(conditions, choices, default="Low")
```

## 11. Updating Values

**Increase IT salaries by 10%:**

```python
df.loc[df["Department"] == "IT", "Salary"] *= 1.10
```

**Update a specific employee:**

```python
df.loc[df["Name"] == "Amit", "Salary"] = 70000
```

**Replace values:**

```python
df["Department"] = df["Department"].replace({
    "IT": "Technology",
    "HR": "Human Resources"
})
```

**Important:** Use `.loc` for conditional updates to avoid chained-assignment problems.

## 12. Renaming Columns

```python
df = df.rename(columns={
    "Name": "EmployeeName",
    "Salary": "MonthlySalary"
})
```

**Rename all columns:**

```python
df.columns = ["Name", "Age", "Department", "Salary"]
```

**Convert column names to lowercase:**

```python
df.columns = df.columns.str.lower()
```

**Remove spaces from column names:**

```python
df.columns = df.columns.str.strip().str.replace(" ", "_")
```

## 13. Dropping Rows and Columns

```python
df.drop(columns=["Age"])
df.drop(columns=["Age", "Department"])
df.drop(index=[0, 1])
```

**Permanent reassignment:**

```python
df = df.drop(columns=["Age"])
```

**Interview Tip:** Most Pandas operations return a new DataFrame unless reassigned or explicitly modified.

## 14. Missing Values — isna(), fillna(), dropna()

**Example:**

```python
data = pd.DataFrame({
    "Name": ["Amit", "Riya", "John", "Sara"],
    "Salary": [50000, None, 60000, None],
    "Department": ["IT", "HR", None, "Finance"]
})
```

**Find missing values:**

```python
data.isna()
data.isnull()                  # Same as isna()
data.isna().sum()              # Missing count per column
data.isna().sum().sum()        # Total missing cells
data.isna().mean() * 100       # Missing percentage per column
```

**Remove rows containing missing values:**

```python
data.dropna()
```

**Remove rows only when all values are missing:**

```python
data.dropna(how="all")
```

**Remove rows where Salary is missing:**

```python
data.dropna(subset=["Salary"])
```

**Fill with fixed value:**

```python
data["Salary"] = data["Salary"].fillna(0)
```

**Fill with mean:**

```python
data["Salary"] = data["Salary"].fillna(data["Salary"].mean())
# Missing salary -> 55000
```

**Fill with median:**

```python
data["Salary"] = data["Salary"].fillna(data["Salary"].median())
```

**Fill categorical missing values:**

```python
data["Department"] = data["Department"].fillna("Unknown")
```

**Forward fill:**

```python
data["Salary"] = data["Salary"].ffill()
```

**Backward fill:**

```python
data["Salary"] = data["Salary"].bfill()
```

**Interview Question: Mean vs Median?**

* Mean: Useful when numeric data has no extreme outliers.
* Median: Often more robust when outliers exist.
* Zero: Use only when zero has a valid business meaning.
* Forward fill: Useful for ordered data where previous values should carry forward.

## 15. Duplicate Records

```python
data = pd.DataFrame({
    "ID": [1, 2, 2, 3, 3],
    "Name": ["A", "B", "B", "C", "C"]
})
```

**Find duplicates:**

```python
data.duplicated()
# False, False, True, False, True
```

**Count duplicates:**

```python
data.duplicated().sum()
# 2
```

**Remove duplicates:**

```python
data = data.drop_duplicates()
```

**Remove duplicates based on ID:**

```python
data = data.drop_duplicates(subset=["ID"])
```

**Keep latest occurrence:**

```python
data = data.drop_duplicates(subset=["ID"], keep="last")
```

**Remove all duplicate groups:**

```python
data = data.drop_duplicates(subset=["ID"], keep=False)
```

**Important:** `keep=False` removes every row whose selected key appears more than once.

## 16. Data Type Conversion

```python
df["Age"] = df["Age"].astype("int64")
df["Salary"] = df["Salary"].astype("float64")
df["Name"] = df["Name"].astype("string")
```

**Convert invalid numeric values to NaN:**

```python
data = pd.DataFrame({"Amount": ["100", "200", "invalid"]})
data["Amount"] = pd.to_numeric(data["Amount"], errors="coerce")
# 100.0, 200.0, NaN
```

**Nullable integer:**

```python
data["Amount"] = data["Amount"].astype("Int64")
```

**Convert to datetime:**

```python
df["JoiningDate"] = pd.to_datetime(df["JoiningDate"], errors="coerce")
```

**Interview Tip:** `errors="coerce"` converts invalid numeric/date values to missing values rather than raising an exception.

## 17. Basic Statistics

```python
df["Salary"].sum()        # 310000
df["Salary"].mean()       # 62000
df["Salary"].median()     # 60000
df["Salary"].min()        # 50000
df["Salary"].max()        # 80000
df["Salary"].count()      # 5 non-null values
df["Salary"].std()        # Sample standard deviation
df["Salary"].var()        # Sample variance
df["Salary"].quantile(.5) # Median
df["Salary"].idxmax()     # Index of maximum salary
```

**Unique values:**

```python
df["Department"].unique()
# ['IT', 'HR', 'Finance']
df["Department"].nunique()
# 3
df["Department"].value_counts()
# IT 2, HR 2, Finance 1
```

**Difference between count() and size:**

```python
df["Salary"].count()  # Counts non-null values
df["Salary"].size     # Counts all elements
```

## 18. String Operations

```python
df["Name"].str.lower()
df["Name"].str.upper()
df["Name"].str.len()
df["Name"].str.strip()
df["Name"].str.startswith("A")
df["Name"].str.endswith("a")
df["Name"].str.contains("a", case=False, na=False)
df["Name"].str.replace("a", "X", regex=False)
```

**Extract email domain:**

```python
emails = pd.Series(["a@gmail.com", "b@yahoo.com"])
domains = emails.str.split("@").str[-1]
# gmail.com, yahoo.com
```

**Extract numbers:**

```python
s = pd.Series(["Order-101", "Order-205"])
print(s.str.extract(r"(\d+)"))
# 101, 205
```

**Split full name:**

```python
names = pd.Series(["Amit Sharma", "Riya Singh"])
parts = names.str.split(" ", n=1, expand=True)
parts.columns = ["FirstName", "LastName"]
```

## 19. Index Operations

```python
df = df.set_index("Name")
df = df.reset_index()
df = df.reset_index(drop=True)
```

**Check whether index is unique:**

```python
df.index.is_unique
```

**Interview Tip:** A Pandas index is a label, not necessarily a row number.

# PART 2: MEDIUM — DATA TRANSFORMATION

## 20. GroupBy — Most Important Interview Topic

**Group employees by department:**

```python
df.groupby("Department")["Salary"].sum()
# Finance 80000
# HR     125000
# IT     105000
```

**Average salary by department:**

```python
df.groupby("Department")["Salary"].mean()
# Finance 80000
# HR      62500
# IT      52500
```

**Multiple aggregations:**

```python
result = df.groupby("Department").agg(
    EmployeeCount=("Name", "count"),
    TotalSalary=("Salary", "sum"),
    AvgSalary=("Salary", "mean"),
    MaxSalary=("Salary", "max")
).reset_index()
```

**Expected output:**

| Department                     | EmployeeCount | TotalSalary | AvgSalary | MaxSalary |
| ------------------------------ | ------------: | ----------: | --------: | --------: |
| Finance                        |             1 |       80000 |     80000 |     80000 |
| HR                             |             2 |      125000 |     62500 |     65000 |
| IT                             |             2 |      105000 |     52500 |     55000 |
| **Group by multiple columns:** |               |             |           |           |

```python
df.groupby(["Department", "Age"])["Salary"].sum()
```

**Count employees by department:**

```python
df.groupby("Department").size()
```

**GroupBy with missing keys:**

```python
df.groupby("Department", dropna=False)["Salary"].sum()
```

**Interview Tip:** By default, `groupby()` excludes rows with missing grouping keys.

## 21. GroupBy — agg() vs transform() vs apply()

**agg(): Returns summarized results, usually fewer rows.**

```python
df.groupby("Department")["Salary"].agg("mean")
```

**transform(): Returns results aligned with original rows.**

```python
df["DeptAvgSalary"] = df.groupby("Department")["Salary"].transform("mean")
```

**Expected result:**

| Name                                                 | Department | Salary | DeptAvgSalary |
| ---------------------------------------------------- | ---------- | -----: | ------------: |
| Amit                                                 | IT         |  50000 |         52500 |
| Riya                                                 | HR         |  60000 |         62500 |
| John                                                 | IT         |  55000 |         52500 |
| Sara                                                 | Finance    |  80000 |         80000 |
| Raj                                                  | HR         |  65000 |         62500 |
| **Find employees earning above department average:** |            |        |               |

```python
avg = df.groupby("Department")["Salary"].transform("mean")
result = df[df["Salary"] > avg]
# John, Raj
```

**apply(): Executes custom logic on groups.**

```python
result = df.groupby("Department").apply(
    lambda group: group.nlargest(1, "Salary"),
    include_groups=False
)
```

**Note:** `include_groups=False` is supported in newer Pandas 2.x versions; its behavior and availability depend on the installed version.
**Interview Answer:**

* `agg()` → Summarize groups.
* `transform()` → Calculate group-level values while preserving original row alignment.
* `apply()` → Flexible custom operations, generally slower than built-in operations.

## 22. Merge — SQL-Style Joins

**Employees table:**

```python
employees = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Riya", "John"],
    "DeptID": [10, 20, 30]
})
```

**Departments table:**

```python
departments = pd.DataFrame({
    "DeptID": [10, 20, 40],
    "Department": ["IT", "HR", "Finance"]
})
```

**INNER JOIN:**

```python
pd.merge(employees, departments, on="DeptID", how="inner")
# Amit IT
# Riya HR
```

**LEFT JOIN:**

```python
pd.merge(employees, departments, on="DeptID", how="left")
# Amit IT
# Riya HR
# John NaN
```

**RIGHT JOIN:**

```python
pd.merge(employees, departments, on="DeptID", how="right")
# Amit IT
# Riya HR
# NaN Finance
```

**OUTER JOIN:**

```python
pd.merge(employees, departments, on="DeptID", how="outer")
# All matching and non-matching records
```

**Join on different column names:**

```python
pd.merge(
    employees,
    departments.rename(columns={"DeptID": "DepartmentID"}),
    left_on="DeptID",
    right_on="DepartmentID",
    how="left"
)
```

**Find unmatched records:**

```python
merged = employees.merge(
    departments,
    on="DeptID",
    how="left",
    indicator=True
)
unmatched = merged[merged["_merge"] == "left_only"]
# John, DeptID 30
```

**Validate merge cardinality:**

```python
employees.merge(
    departments,
    on="DeptID",
    how="left",
    validate="many_to_one"
)
```

**Interview Tip:** Always check duplicate join keys. Duplicate keys on both sides can unexpectedly multiply rows.

## 23. Merge vs Join vs Concat

**merge():** SQL-style joins using column/index keys.

```python
pd.merge(df1, df2, on="ID", how="inner")
```

**join():** Convenient index-based joining.

```python
df1.join(df2, how="left", lsuffix="_left", rsuffix="_right")
```

**concat():** Stack DataFrames vertically or horizontally.

```python
pd.concat([df1, df2], ignore_index=True) # Stack rows
pd.concat([df1, df2], axis=1)            # Combine columns by index
```

**Interview Question: When would you use concat instead of merge?**
Use `concat()` when combining monthly files with the same structure. Use `merge()` when connecting related tables using keys.

## 24. map() vs apply() vs applymap()

**map(): Element-wise transformation on a Series.**

```python
df["DepartmentCode"] = df["Department"].map({
    "IT": 1,
    "HR": 2,
    "Finance": 3
})
```

**Series.map() with lambda:**

```python
df["SalaryInThousands"] = df["Salary"].map(lambda x: x / 1000)
```

**Series.apply(): Custom function on Series elements.**

```python
df["SalaryCategory"] = df["Salary"].apply(
    lambda x: "High" if x >= 60000 else "Low"
)
```

**DataFrame.apply(): Operate across rows or columns.**

```python
df["Description"] = df.apply(
    lambda row: f"{row['Name']} works in {row['Department']}",
    axis=1
)
```

**DataFrame.map(): Element-wise DataFrame operation (Pandas 2.1+).**

```python
numeric = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
result = numeric.map(lambda x: x * 2)
```

**Interview Tip:** `DataFrame.applymap()` was deprecated in Pandas 2.1. Use `DataFrame.map()` in modern Pandas.
**Performance Preference:** Vectorized operations > built-in Pandas operations > Python row-wise `apply()` in many common numerical workloads. Benchmark when performance matters.

## 25. Pivot Tables

**Sales dataset:**

```python
sales = pd.DataFrame({
    "Region": ["North", "North", "South", "South", "North"],
    "Product": ["A", "B", "A", "B", "A"],
    "Sales": [100, 200, 150, 250, 300]
})
```

**Pivot total sales:**

```python
result = pd.pivot_table(
    sales,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)
```

**Output:**

| Region                    |   A |   B |
| ------------------------- | --: | --: |
| North                     | 400 | 200 |
| South                     | 150 | 250 |
| **Pivot vs Pivot Table:** |     |     |

```python
sales.pivot_table(index="Region", columns="Product", values="Sales", aggfunc="sum")
```

`pivot()` requires unique index/column combinations. `pivot_table()` can aggregate duplicate combinations.

## 26. Melt — Wide to Long

```python
wide = pd.DataFrame({
    "Name": ["Amit", "Riya"],
    "Jan": [100, 200],
    "Feb": [150, 250]
})
long = wide.melt(
    id_vars="Name",
    var_name="Month",
    value_name="Sales"
)
```

**Output:**

| Name                                                                                                                    | Month | Sales |
| ----------------------------------------------------------------------------------------------------------------------- | ----- | ----: |
| Amit                                                                                                                    | Jan   |   100 |
| Riya                                                                                                                    | Jan   |   200 |
| Amit                                                                                                                    | Feb   |   150 |
| Riya                                                                                                                    | Feb   |   250 |
| **Interview Tip:** `melt()` converts columns into rows. Pivot operations typically convert row categories into columns. |       |       |

## 27. Stack and Unstack

```python
pivot = sales.pivot_table(
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum"
)
stacked = pivot.stack()
restored = stacked.unstack()
```

**Concept:**

* `stack()` moves a column level into the row index.
* `unstack()` moves an index level into columns.

## 28. Datetime Operations

```python
orders = pd.DataFrame({
    "OrderID": [1, 2, 3],
    "OrderDate": ["2026-01-10", "2026-02-15", "2026-02-20"],
    "Amount": [1000, 2000, 1500]
})
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["Year"] = orders["OrderDate"].dt.year
orders["Month"] = orders["OrderDate"].dt.month
orders["Day"] = orders["OrderDate"].dt.day
orders["DayName"] = orders["OrderDate"].dt.day_name()
orders["Quarter"] = orders["OrderDate"].dt.quarter
orders["Weekday"] = orders["OrderDate"].dt.weekday
```

**Filter by date:**

```python
orders[orders["OrderDate"] >= "2026-02-01"]
```

**Calculate days since order:**

```python
orders["DaysOld"] = (
    pd.Timestamp("2026-03-01") - orders["OrderDate"]
).dt.days
```

**Monthly aggregation:**

```python
monthly = orders.groupby(
    orders["OrderDate"].dt.to_period("M")
)["Amount"].sum()
# 2026-01 1000
# 2026-02 3500
```

**Resampling:**

```python
monthly = orders.set_index("OrderDate").resample("MS")["Amount"].sum()
```

## 29. Time Zones

```python
timestamps = pd.Series(["2026-01-10 12:00:00"])
dates = pd.to_datetime(timestamps)
utc_dates = dates.dt.tz_localize("UTC")
india_dates = utc_dates.dt.tz_convert("Asia/Kolkata")
# 2026-01-10 17:30:00+05:30
```

**Interview Question: tz_localize vs tz_convert?**

* `tz_localize()` assigns a timezone to timezone-naive timestamps.
* `tz_convert()` converts already timezone-aware timestamps into another timezone.

## 30. Conditional Transformations

**Create salary bands:**

```python
df["SalaryBand"] = pd.cut(
    df["Salary"],
    bins=[0, 55000, 70000, float("inf")],
    labels=["Low", "Medium", "High"]
)
```

**Quantile-based bins:**

```python
df["SalaryQuartile"] = pd.qcut(
    df["Salary"],
    q=4,
    labels=False
)
```

**Interview Tip:** `cut()` uses fixed value ranges; `qcut()` uses quantiles to create approximately equal-sized groups.

## 31. Rank Employees

```python
df["SalaryRank"] = df["Salary"].rank(ascending=False, method="dense")
```

**Rank within department:**

```python
df["DeptRank"] = df.groupby("Department")["Salary"].rank(
    ascending=False,
    method="dense"
)
```

**Find highest-paid employee per department:**

```python
result = df[df["DeptRank"] == 1]
# John (IT), Raj (HR), Sara (Finance)
```

**Interview Tip:** `rank(method="dense")` assigns the same rank to ties without skipping subsequent rank numbers.

## 32. Shift, Diff, and Percentage Change

```python
revenue = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Revenue": [100, 120, 90, 150]
})
revenue["Previous"] = revenue["Revenue"].shift(1)
revenue["Difference"] = revenue["Revenue"].diff()
revenue["GrowthPct"] = revenue["Revenue"].pct_change() * 100
```

**Output:**

| Month | Revenue | Previous | Difference | GrowthPct |
| ----- | ------: | -------: | ---------: | --------: |
| Jan   |     100 |      NaN |        NaN |       NaN |
| Feb   |     120 |      100 |         20 |     20.00 |
| Mar   |      90 |      120 |        -30 |    -25.00 |
| Apr   |     150 |       90 |         60 |     66.67 |

## 33. Rolling Calculations

```python
revenue["RollingAvg"] = revenue["Revenue"].rolling(window=2).mean()
# NaN, 110, 105, 120
```

**Expanding cumulative average:**

```python
revenue["CumulativeAvg"] = revenue["Revenue"].expanding().mean()
```

**Cumulative sum:**

```python
revenue["CumulativeRevenue"] = revenue["Revenue"].cumsum()
# 100, 220, 310, 460
```

## 34. Explode — List to Rows

```python
data = pd.DataFrame({
    "Name": ["Amit", "Riya"],
    "Skills": [["Python", "SQL"], ["Excel", "Pandas"]]
})
result = data.explode("Skills", ignore_index=True)
```

**Output:**

| Name | Skills |
| ---- | ------ |
| Amit | Python |
| Amit | SQL    |
| Riya | Excel  |
| Riya | Pandas |

## 35. Cross Tabulation

```python
pd.crosstab(df["Department"], df["Age"] >= 30)
```

**Use Case:** Count employees by department and age category.

## 36. Data Validation

**Check required columns:**

```python
required = {"Name", "Age", "Salary"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")
```

**Validate salary values:**

```python
invalid = df[df["Salary"] < 0]
```

**Validate unique IDs:**

```python
if df["EmployeeID"].duplicated().any():
    raise ValueError("Duplicate employee IDs found")
```

**Validate allowed categories:**

```python
allowed = {"IT", "HR", "Finance"}
invalid = df[~df["Department"].isin(allowed)]
```

**Validate missing values:**

```python
if df["Salary"].isna().any():
    raise ValueError("Salary contains missing values")
```

**Interview Tip:** Data validation should happen before business transformations and again before writing final output.

# PART 3: HARD — ADVANCED PANDAS + ETL

## 37. Find Second-Highest Salary

```python
second = df["Salary"].drop_duplicates().nlargest(2).iloc[-1]
print(second)
# 65000
```

**Handle insufficient distinct salaries:**

```python
unique_salaries = df["Salary"].dropna().drop_duplicates().nlargest(2)
second = unique_salaries.iloc[-1] if len(unique_salaries) >= 2 else None
```

## 38. Find Top 2 Salaries Per Department

```python
result = (
    df.sort_values("Salary", ascending=False)
      .groupby("Department")
      .head(2)
)
```

**Alternative using rank (includes ties):**

```python
ranks = df.groupby("Department")["Salary"].rank(
    method="dense",
    ascending=False
)
result = df[ranks <= 2]
```

**Important:** `head(2)` returns at most two rows per department; dense ranking can return more rows when salaries are tied.

## 39. Remove Duplicates and Keep Latest Record

```python
records = pd.DataFrame({
    "ID": [1, 1, 2, 2],
    "UpdatedAt": [
        "2026-01-01", "2026-02-01",
        "2026-01-10", "2026-03-01"
    ],
    "Value": [100, 200, 300, 400]
})
records["UpdatedAt"] = pd.to_datetime(records["UpdatedAt"])
latest = (
    records.sort_values("UpdatedAt")
           .drop_duplicates(subset=["ID"], keep="last")
)
```

**Output:**

| ID | UpdatedAt  | Value |
| -- | ---------- | ----: |
| 1  | 2026-02-01 |   200 |
| 2  | 2026-03-01 |   400 |

## 40. Find Customers Who Never Ordered

```python
customers = pd.DataFrame({
    "CustomerID": [1, 2, 3, 4]
})
orders = pd.DataFrame({
    "CustomerID": [1, 1, 3],
    "Amount": [100, 200, 300]
})
result = customers[
    ~customers["CustomerID"].isin(orders["CustomerID"])
]
# CustomerID 2, 4
```

**Alternative using merge indicator:**

```python
merged = customers.merge(
    orders[["CustomerID"]].drop_duplicates(),
    on="CustomerID",
    how="left",
    indicator=True
)
result = merged[merged["_merge"] == "left_only"]
```

## 41. Find Duplicate Transactions

```python
transactions = pd.DataFrame({
    "TransactionID": [101, 102, 102, 103, 103],
    "Amount": [500, 600, 600, 700, 700]
})
duplicates = transactions[
    transactions.duplicated(subset=["TransactionID"], keep=False)
]
```

**Output:** Both records for TransactionID 102 and both records for 103.

## 42. Conditional GroupBy Aggregation

```python
orders = pd.DataFrame({
    "Customer": ["A", "A", "B", "B"],
    "Status": ["Success", "Failed", "Success", "Failed"],
    "Amount": [100, 200, 300, 400]
})
result = orders.groupby("Customer").agg(
    TotalAmount=("Amount", "sum"),
    SuccessfulAmount=(
        "Amount",
        lambda x: x[orders.loc[x.index, "Status"] == "Success"].sum()
    ),
    FailedCount=(
        "Status",
        lambda x: (x == "Failed").sum()
    )
)
```

**Output:**

| Customer                                     | TotalAmount | SuccessfulAmount | FailedCount |
| -------------------------------------------- | ----------: | ---------------: | ----------: |
| A                                            |         300 |              100 |           1 |
| B                                            |         700 |              300 |           1 |
| **Cleaner alternative using helper column:** |             |                  |             |

```python
orders["SuccessfulAmount"] = orders["Amount"].where(
    orders["Status"] == "Success", 0
)
result = orders.groupby("Customer").agg(
    TotalAmount=("Amount", "sum"),
    SuccessfulAmount=("SuccessfulAmount", "sum"),
    FailedCount=("Status", lambda s: s.eq("Failed").sum())
)
```

## 43. GroupBy with Multiple Conditions

**Question:** Find departments with average salary above 55000 and at least two employees.

```python
summary = df.groupby("Department").agg(
    AvgSalary=("Salary", "mean"),
    Count=("Name", "count")
)
result = summary[
    (summary["AvgSalary"] > 55000) &
    (summary["Count"] >= 2)
]
# HR
```

## 44. Calculate Percentage Contribution

```python
df["SalaryContributionPct"] = (
    df["Salary"] / df["Salary"].sum() * 100
)
```

**Within department:**

```python
dept_total = df.groupby("Department")["Salary"].transform("sum")
df["DeptContributionPct"] = df["Salary"] / dept_total * 100
```

## 45. Detect Outliers Using IQR

```python
q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]
```

**Interview Tip:** IQR is less sensitive to extreme values than mean/std-based approaches.

## 46. Normalize Numeric Data

**Min-Max Scaling:**

```python
minimum = df["Salary"].min()
maximum = df["Salary"].max()
if maximum != minimum:
    df["NormalizedSalary"] = (df["Salary"] - minimum) / (maximum - minimum)
else:
    df["NormalizedSalary"] = 0.0
```

**Z-score:**

```python
std = df["Salary"].std()
df["ZScore"] = (
    (df["Salary"] - df["Salary"].mean()) / std
    if pd.notna(std) and std != 0
    else 0.0
)
```

## 47. Process Multiple CSV Files

```python
from pathlib import Path
files = sorted(Path("data").glob("*.csv"))
if not files:
    raise FileNotFoundError("No CSV files found")
frames = [pd.read_csv(file) for file in files]
combined = pd.concat(frames, ignore_index=True)
combined.to_csv("combined.csv", index=False)
```

**Interview Scenario:** You receive 12 monthly sales files and must generate one annual report.
**Approach:** Read → validate schemas → combine → clean → aggregate → export.

## 48. Process Large CSV in Chunks

```python
total_sales = 0
for chunk in pd.read_csv("large_sales.csv", chunksize=100000):
    chunk["Amount"] = pd.to_numeric(chunk["Amount"], errors="coerce")
    total_sales += chunk["Amount"].sum()
print(total_sales)
```

**Why chunks?** Avoid loading the entire file into memory.
**Chunked filtering and writing:**

```python
first_chunk = True
for chunk in pd.read_csv("large_sales.csv", chunksize=100000):
    filtered = chunk[chunk["Amount"] > 1000]
    filtered.to_csv(
        "filtered_sales.csv",
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )
    first_chunk = False
```

## 49. Optimize DataFrame Memory

**Check memory usage:**

```python
df.memory_usage(deep=True)
df.info(memory_usage="deep")
```

**Downcast numeric columns:**

```python
df["Age"] = pd.to_numeric(df["Age"], downcast="integer")
df["Salary"] = pd.to_numeric(df["Salary"], downcast="float")
```

**Convert repeated strings to category:**

```python
df["Department"] = df["Department"].astype("category")
```

**Read only required columns:**

```python
df = pd.read_csv("large.csv", usecols=["ID", "Amount"])
```

**Interview Tip:** Use `category` for repeated low-cardinality strings. Avoid unnecessary copies and row-wise Python loops.

## 50. Vectorization vs Iteration

**Slow approach:**

```python
for index, row in df.iterrows():
    df.loc[index, "Bonus"] = row["Salary"] * 0.10
```

**Better approach:**

```python
df["Bonus"] = df["Salary"] * 0.10
```

**Interview Answer:** Vectorization delegates operations to optimized Pandas/NumPy implementations and often avoids Python-level loops.

## 51. API Response to Pandas DataFrame

```python
import requests
url = "https://api.example.com/employees"
response = requests.get(url, timeout=10)
response.raise_for_status()
data = response.json()
df = pd.DataFrame(data)
```

**Nested JSON:**

```python
data = [
    {"id": 1, "user": {"name": "Amit", "city": "Delhi"}},
    {"id": 2, "user": {"name": "Riya", "city": "Mumbai"}}
]
df = pd.json_normalize(data)
# Columns: id, user.name, user.city
```

**Interview Tip:** Verify API response structure before constructing the DataFrame. Some APIs return records inside a key such as `"data"` or `"results"`.

## 52. API Pagination

```python
import requests
all_records = []
for page in range(1, 6):
    response = requests.get(
        "https://api.example.com/orders",
        params={"page": page, "limit": 100},
        timeout=10
    )
    response.raise_for_status()
    payload = response.json()
    records = payload.get("results", [])
    if not records:
        break
    all_records.extend(records)
df = pd.DataFrame(all_records)
```

**Interview Tip:** Pagination implementations differ. Some use page numbers, others use offsets or cursor tokens.

## 53. Excel Processing — Multiple Sheets

```python
sheets = pd.read_excel("sales.xlsx", sheet_name=None)
frames = []
for sheet_name, sheet_df in sheets.items():
    sheet_df["SourceSheet"] = sheet_name
    frames.append(sheet_df)
combined = pd.concat(frames, ignore_index=True)
combined.to_excel("combined.xlsx", index=False)
```

**Interview Scenario:** Each Excel sheet contains sales for a different region. Combine them and preserve the region/source information.

## 54. Excel Data Cleaning

```python
df = pd.read_excel("employees.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["department"] = df["department"].astype("string").str.strip().str.upper()
df = df.dropna(subset=["salary"])
df.to_excel("cleaned_employees.xlsx", index=False)
```

## 55. End-to-End ETL Pipeline

**Scenario:** Receive a CSV containing sales transactions. Clean the data, validate amounts, remove duplicates, aggregate sales by region, and export results.

```python
import pandas as pd
def run_etl(input_file, output_file):
    # EXTRACT
    df = pd.read_csv(input_file)
    # VALIDATE SCHEMA
    required = {"TransactionID", "Region", "Amount"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    # CLEAN
    df.columns = df.columns.str.strip()
    df["Region"] = df["Region"].astype("string").str.strip().str.upper()
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    # VALIDATE RECORDS
    df = df.dropna(subset=["TransactionID", "Region", "Amount"])
    df = df[df["Amount"] > 0]
    # REMOVE DUPLICATES
    df = df.drop_duplicates(subset=["TransactionID"])
    # TRANSFORM
    summary = df.groupby("Region", as_index=False).agg(
        TotalSales=("Amount", "sum"),
        TransactionCount=("TransactionID", "count"),
        AverageSale=("Amount", "mean")
    )
    # LOAD
    summary.to_csv(output_file, index=False)
    return summary
result = run_etl("sales.csv", "sales_summary.csv")
print(result)
```

**Important Production Improvement:** Normalize column names before validating them, otherwise a column such as `" Amount "` will incorrectly fail schema validation.
**Correct order:**

```python
df = pd.read_csv(input_file)
df.columns = df.columns.str.strip()
missing = required - set(df.columns)
```

**Interview Explanation:** Extract → validate schema → standardize → clean → validate records → deduplicate → aggregate → load.

## 56. Handle Bad Data Without Losing Records

**Scenario:** Some transactions contain invalid amounts. Business wants rejected records in a separate file.

```python
df = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Amount": ["100", "invalid", "-50", "200"]
})
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
valid = df[df["Amount"].notna() & (df["Amount"] > 0)].copy()
rejected = df[df["Amount"].isna() | (df["Amount"] <= 0)].copy()
valid.to_csv("valid.csv", index=False)
rejected.to_csv("rejected.csv", index=False)
```

**Interview Tip:** In production ETL, quarantining invalid records is often safer than silently deleting them.

## 57. Reconcile Two Datasets

**Scenario:** Compare source transactions against processed transactions.

```python
source = pd.DataFrame({
    "ID": [1, 2, 3],
    "Amount": [100, 200, 300]
})
target = pd.DataFrame({
    "ID": [1, 2, 4],
    "Amount": [100, 250, 400]
})
comparison = source.merge(
    target,
    on="ID",
    how="outer",
    suffixes=("_source", "_target"),
    indicator=True,
    validate="one_to_one"
)
comparison["AmountMismatch"] = (
    comparison["_merge"].eq("both") &
    comparison["Amount_source"].ne(comparison["Amount_target"])
)
```

**Interpretation:**

* ID 1 → Matched.
* ID 2 → Amount mismatch.
* ID 3 → Missing in target.
* ID 4 → Missing in source.
  **Practical Connection:** Similar reconciliation logic is useful when comparing financial transactions, settlement records, or transformed datasets.

## 58. Identify Missing Dates

```python
dates = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-05"])
expected = pd.date_range(dates.min(), dates.max(), freq="D")
missing = expected.difference(pd.DatetimeIndex(dates))
print(missing)
# 2026-01-02, 2026-01-04
```

## 59. Compare Two DataFrames

**When rows and columns align:**

```python
old = pd.DataFrame({"Amount": [100, 200]}, index=[1, 2])
new = pd.DataFrame({"Amount": [100, 250]}, index=[1, 2])
changes = old.compare(new)
```

**Important:** `DataFrame.compare()` requires identically labeled rows and columns.

## 60. Advanced Join — Merge As Of

**Scenario:** Match each transaction to the latest available price at or before its timestamp.

```python
trades = pd.DataFrame({
    "Time": pd.to_datetime(["2026-01-01 10:05", "2026-01-01 10:15"]),
    "Quantity": [10, 20]
})
prices = pd.DataFrame({
    "Time": pd.to_datetime(["2026-01-01 10:00", "2026-01-01 10:10"]),
    "Price": [100, 105]
})
result = pd.merge_asof(
    trades.sort_values("Time"),
    prices.sort_values("Time"),
    on="Time",
    direction="backward"
)
```

**Output:**

| Time                                                                                                                                                           | Quantity | Price |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------: | ----: |
| 10:05                                                                                                                                                          |       10 |   100 |
| 10:15                                                                                                                                                          |       20 |   105 |
| **Interview Tip:** `merge_asof()` is useful for time-series data, financial transactions, and event-to-price matching. Inputs must be sorted by the merge key. |          |       |

## 61. Advanced Window — Rolling Average Per Group

```python
data = pd.DataFrame({
    "Customer": ["A", "A", "A", "B", "B"],
    "Date": pd.to_datetime([
        "2026-01-01", "2026-01-02", "2026-01-03",
        "2026-01-01", "2026-01-02"
    ]),
    "Amount": [100, 200, 300, 400, 500]
})
data = data.sort_values(["Customer", "Date"])
data["RollingAvg"] = (
    data.groupby("Customer")["Amount"]
        .transform(lambda s: s.rolling(2, min_periods=1).mean())
)
```

**Output:**

| Customer | Amount | RollingAvg |
| -------- | -----: | ---------: |
| A        |    100 |        100 |
| A        |    200 |        150 |
| A        |    300 |        250 |
| B        |    400 |        400 |
| B        |    500 |        450 |

## 62. Cumulative Sum Per Group

```python
data["CumulativeAmount"] = data.groupby("Customer")["Amount"].cumsum()
```

**Output:**

| Customer | Amount | CumulativeAmount |
| -------- | -----: | ---------------: |
| A        |    100 |              100 |
| A        |    200 |              300 |
| A        |    300 |              600 |
| B        |    400 |              400 |
| B        |    500 |              900 |

## 63. Detect Consecutive Events

**Scenario:** Identify consecutive failed transactions.

```python
events = pd.DataFrame({
    "Status": ["Success", "Failed", "Failed", "Success", "Failed"]
})
events["Failure"] = events["Status"].eq("Failed")
events["Group"] = events["Failure"].ne(events["Failure"].shift()).cumsum()
events["ConsecutiveFailures"] = (
    events.groupby("Group")["Failure"].cumsum()
)
```

**Output:**

| Status  | ConsecutiveFailures |
| ------- | ------------------: |
| Success |                   0 |
| Failed  |                   1 |
| Failed  |                   2 |
| Success |                   0 |
| Failed  |                   1 |

## 64. DataFrame Performance Optimization

**Problem:** Processing millions of records takes too long.
**Recommended approach:**

1. Read only required columns with `usecols`.
2. Specify appropriate data types with `dtype`.
3. Use vectorized operations instead of row loops.
4. Filter unnecessary records early.
5. Use categorical data types for repetitive strings.
6. Process CSV files in chunks when necessary.
7. Use Parquet for efficient repeated analytical reads.
8. Avoid repeated `pd.concat()` inside loops.
9. Reduce expensive custom `apply()` operations.
10. Profile bottlenecks before optimizing.
    **Bad approach:**

```python
result = pd.DataFrame()
for file in files:
    result = pd.concat([result, pd.read_csv(file)])
```

**Better approach:**

```python
frames = [pd.read_csv(file) for file in files]
result = pd.concat(frames, ignore_index=True)
```

**Important:** The second approach still loads all files into memory. For very large datasets, use streaming/chunked processing or a database/query engine.

## 65. CSV vs Excel vs Parquet

| Feature                                                                                                                                                   | CSV              | Excel                     | Parquet                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------- | ---------------------------- |
| Format                                                                                                                                                    | Plain text       | Spreadsheet               | Binary columnar              |
| Data types                                                                                                                                                | Limited metadata | Spreadsheet types         | Preserves schema/types       |
| Multiple sheets                                                                                                                                           | No               | Yes                       | No                           |
| Compression                                                                                                                                               | External         | Built-in file compression | Efficient column compression |
| Analytics performance                                                                                                                                     | Often slower     | Often slower              | Often faster                 |
| Best use                                                                                                                                                  | Data exchange    | Business reports          | Large analytical datasets    |
| **Interview Answer:** Parquet is commonly preferred for analytical pipelines because it is columnar, compressed, and supports efficient column selection. |                  |                           |                              |

## 66. Handling Large Data — Interview Scenario

**Question:** You have a 10 GB CSV file but only 4 GB RAM. How would you process it?
**Answer:**

1. Identify required columns and data types.
2. Read the file using `chunksize`.
3. Validate and transform each chunk.
4. Perform incremental aggregations.
5. Write results incrementally instead of collecting everything in memory.
6. For complex joins/global operations, consider databases, DuckDB, or PySpark.
   **Example:**

```python
totals = {}
for chunk in pd.read_csv(
    "large.csv",
    usecols=["Region", "Amount"],
    chunksize=100000
):
    chunk["Amount"] = pd.to_numeric(chunk["Amount"], errors="coerce")
    grouped = chunk.groupby("Region")["Amount"].sum()
    for region, amount in grouped.items():
        totals[region] = totals.get(region, 0) + amount
result = pd.DataFrame(
    list(totals.items()),
    columns=["Region", "TotalAmount"]
)
```

**Limitation:** The dictionary still grows with the number of unique regions. This approach works well when group cardinality is manageable.

# PART 4: MOST ASKED PANDAS INTERVIEW QUESTIONS

## 67. Quick Concept Questions

**Q1. What is the difference between Series and DataFrame?**
Series is one-dimensional; DataFrame is two-dimensional.


**Q2. What is the difference between loc and iloc?**
`loc` uses labels; `iloc` uses integer positions.


**Q3. What is the difference between merge and concat?**
`merge` combines data using keys; `concat` stacks or aligns DataFrames along an axis.


**Q4. What is the difference between apply and map?**
`Series.map()` performs element-wise transformations; `DataFrame.apply()` applies functions across rows or columns.


**Q5. What is the difference between agg and transform?**
`agg` summarizes; `transform` returns values aligned with the original rows.


**Q6. What is the difference between count and size?**
`count()` excludes missing values; `size` includes them.


**Q7. What is the difference between pivot and pivot_table?**
`pivot` requires unique combinations; `pivot_table` supports aggregation.



**Q8. What is the difference between fillna and dropna?**
`fillna` replaces missing values; `dropna` removes rows/columns according to missing-value rules.


**Q9. How do you find duplicates?**

```python
df[df.duplicated(keep=False)]
```

**Q10. How do you remove duplicates based on specific columns?**

```python
df.drop_duplicates(subset=["ID"], keep="last")
```

**Q11. How do you get the top 5 rows by salary?**

```python
df.nlargest(5, "Salary")
```

**Q12. How do you find the average salary per department?**

```python
df.groupby("Department")["Salary"].mean()
```

**Q13. How do you handle invalid numeric values?**

```python
pd.to_numeric(df["Amount"], errors="coerce")
```

**Q14. How do you find rows with missing values?**

```python
df[df.isna().any(axis=1)]
```

**Q15. How do you calculate the percentage of missing values?**

```python
df.isna().mean() * 100
```

**Q16. How do you find unique values?**

```python
df["Department"].unique()
```

**Q17. How do you count unique values?**

```python
df["Department"].nunique()
```

**Q18. How do you find the most frequent value?**

```python
df["Department"].mode()
```

**Q19. How do you combine monthly CSV files?**

```python
pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
```

**Q20. How do you process millions of records efficiently?**
Use appropriate data types, vectorization, column selection, chunking, and efficient storage formats.

# PART 5: UBER-STYLE PRACTICAL INTERVIEW SCENARIOS

## 68. Scenario 1 — Clean an Employee Excel File

**Question:** An Excel file has duplicate employees, missing salaries, inconsistent department names, and invalid ages. How would you clean it?

```python
df = pd.read_excel("employees.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
required = {"employee_id", "department", "salary", "age"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing columns: {missing}")
df["department"] = df["department"].astype("string").str.strip().str.upper()
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df = df.drop_duplicates(subset=["employee_id"], keep="last")
df = df.dropna(subset=["employee_id", "salary", "age"])
df = df[(df["age"] >= 18) & (df["age"] <= 65)]
df = df[df["salary"] > 0]
df.to_excel("cleaned_employees.xlsx", index=False)
```

**What interviewer checks:** Schema validation, cleaning, missing values, duplicates, business rules, output.

## 69. Scenario 2 — Join Employee and Department Files

**Question:** You receive employees.csv and departments.csv. Generate a report with employee name, department name, and salary.

```python
employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")
result = employees.merge(
    departments,
    on="DeptID",
    how="left",
    validate="many_to_one"
)
result = result[["Name", "Department", "Salary"]]
result.to_csv("employee_report.csv", index=False)
```

**Important:** Validate department keys to prevent accidental row multiplication.

## 70. Scenario 3 — Monthly Sales Report

**Question:** Generate monthly total sales, average order value, and order count.

```python
orders = pd.read_csv("orders.csv", parse_dates=["OrderDate"])
orders["Amount"] = pd.to_numeric(orders["Amount"], errors="coerce")
orders = orders.dropna(subset=["OrderDate", "Amount"])
orders["Month"] = orders["OrderDate"].dt.to_period("M")
report = orders.groupby("Month").agg(
    TotalSales=("Amount", "sum"),
    AverageOrderValue=("Amount", "mean"),
    OrderCount=("Amount", "size")
).reset_index()
report["Month"] = report["Month"].astype(str)
report.to_csv("monthly_report.csv", index=False)
```

## 71. Scenario 4 — Reconcile Source and Target Files

**Question:** Compare two transaction files and identify missing or mismatched records.

```python
source = pd.read_csv("source.csv")
target = pd.read_csv("target.csv")
source["Amount"] = pd.to_numeric(source["Amount"], errors="coerce")
target["Amount"] = pd.to_numeric(target["Amount"], errors="coerce")
merged = source.merge(
    target,
    on="TransactionID",
    how="outer",
    suffixes=("_source", "_target"),
    indicator=True,
    validate="one_to_one"
)
merged["Mismatch"] = (
    merged["_merge"].eq("both") &
    merged["Amount_source"].ne(merged["Amount_target"])
)
issues = merged[
    merged["_merge"].ne("both") | merged["Mismatch"]
]
issues.to_csv("reconciliation_issues.csv", index=False)
```

**Production Note:** Define a policy for missing amounts and floating-point tolerances before comparing financial values.

## 72. Scenario 5 — Transform API Data into Excel

**Question:** Fetch JSON data from an API, flatten nested fields, clean it, and generate an Excel report.

```python
import requests
import pandas as pd
response = requests.get("https://api.example.com/orders", timeout=10)
response.raise_for_status()
payload = response.json()
df = pd.json_normalize(payload["results"])
df.columns = df.columns.str.replace(".", "_", regex=False)
df = df.drop_duplicates()
df.to_excel("api_report.xlsx", index=False)
```

**What interviewer checks:** API integration, JSON parsing, nested data transformation, deduplication, export.

# PART 6: FINAL 2-MINUTE REVISION

| Task                  | Pandas Syntax                                                       |
| --------------------- | ------------------------------------------------------------------- |
| Read CSV              | `pd.read_csv("file.csv")`                                           |
| Read Excel            | `pd.read_excel("file.xlsx")`                                        |
| Read Parquet          | `pd.read_parquet("file.parquet")`                                   |
| First 5 rows          | `df.head()`                                                         |
| Dataset dimensions    | `df.shape`                                                          |
| Data types            | `df.dtypes`                                                         |
| Missing counts        | `df.isna().sum()`                                                   |
| Fill missing          | `df["A"].fillna(0)`                                                 |
| Drop missing          | `df.dropna()`                                                       |
| Remove duplicates     | `df.drop_duplicates()`                                              |
| Select column         | `df["A"]`                                                           |
| Select columns        | `df[["A", "B"]]`                                                    |
| Filter rows           | `df[df["A"] > 10]`                                                  |
| Sort rows             | `df.sort_values("A")`                                               |
| Top 5                 | `df.nlargest(5, "A")`                                               |
| Rename column         | `df.rename(columns={"A": "B"})`                                     |
| Convert numeric       | `pd.to_numeric(df["A"], errors="coerce")`                           |
| Convert date          | `pd.to_datetime(df["Date"])`                                        |
| GroupBy sum           | `df.groupby("A")["B"].sum()`                                        |
| GroupBy mean          | `df.groupby("A")["B"].mean()`                                       |
| Multiple aggregations | `df.groupby("A").agg(Total=("B", "sum"))`                           |
| Group transformation  | `df.groupby("A")["B"].transform("mean")`                            |
| Inner join            | `df1.merge(df2, on="ID", how="inner")`                              |
| Left join             | `df1.merge(df2, on="ID", how="left")`                               |
| Stack rows            | `pd.concat([df1, df2], ignore_index=True)`                          |
| Map values            | `df["A"].map(mapping)`                                              |
| Apply function        | `df["A"].apply(function)`                                           |
| Pivot table           | `df.pivot_table(index="A", columns="B", values="C", aggfunc="sum")` |
| Melt                  | `df.melt(id_vars="ID")`                                             |
| Unique values         | `df["A"].unique()`                                                  |
| Value counts          | `df["A"].value_counts()`                                            |
| Rank                  | `df["A"].rank()`                                                    |
| Previous value        | `df["A"].shift(1)`                                                  |
| Difference            | `df["A"].diff()`                                                    |
| Percentage change     | `df["A"].pct_change()`                                              |
| Rolling average       | `df["A"].rolling(3).mean()`                                         |
| Cumulative sum        | `df["A"].cumsum()`                                                  |
| Explode lists         | `df.explode("A")`                                                   |
| Memory usage          | `df.memory_usage(deep=True)`                                        |
| CSV chunks            | `pd.read_csv("file.csv", chunksize=100000)`                         |
| Export CSV            | `df.to_csv("output.csv", index=False)`                              |
| Export Excel          | `df.to_excel("output.xlsx", index=False)`                           |
| Export Parquet        | `df.to_parquet("output.parquet", index=False)`                      |

# FINAL INTERVIEW TAKEAWAYS

1. **Pandas fundamentals:** Know DataFrames, filtering, selection, missing values, duplicates, and type conversions.
2. **Transformations:** Master `groupby`, `agg`, `transform`, `merge`, `concat`, `apply`, `map`, and pivoting.
3. **File handling:** Be comfortable with CSV, Excel, JSON, and Parquet.
4. **ETL:** Explain the complete flow: extract → validate → clean → transform → aggregate → load.
5. **Performance:** Understand vectorization, memory usage, chunk processing, and data types.
6. **Data quality:** Never silently discard important invalid records without considering business requirements.
7. **Joins:** Understand join types, duplicate keys, unmatched records, and merge validation.
8. **Interview scenarios:** Practice explaining how you would transform an unfamiliar dataset step by step.
9. **Real-world thinking:** Discuss edge cases, missing values, duplicates, scalability, and error handling.
10. **Most important:** Be able to write Pandas code and explain why you chose each operation.
