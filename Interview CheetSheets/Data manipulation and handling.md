
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



### Q6. You have an Excel file containing employee data. Some rows have missing salaries and duplicate employee IDs. How would you clean the data?
**Answer:** I would read the Excel file using Pandas, check missing values and duplicates, and clean them according to business requirements.
```python
import pandas as pd
df = pd.read_excel("employees.xlsx")
print(df.isnull().sum())
print(df[df.duplicated("EmployeeID", keep=False)])
df = df.dropna(subset=["EmployeeID"])
df = df.drop_duplicates(subset=["EmployeeID"], keep="first")
```
**Explanation:** `isnull().sum()` identifies missing values. `dropna()` removes records without an employee ID. `drop_duplicates()` keeps one record per employee.
**Follow-up:** What about missing salaries? → I would check the business requirement before filling or removing them. I would not automatically replace missing salaries with zero.
### Q7. You have two Excel files: one contains employee IDs and salaries, and the other contains employee IDs and departments. How would you combine them?
**Answer:** I would use Pandas `merge()` with EmployeeID as the common key.
```python
employees = pd.read_excel("employees.xlsx")
departments = pd.read_excel("departments.xlsx")
result = pd.merge(
    employees,
    departments,
    on="EmployeeID",
    how="left"
)
```
**Explanation:** A left join keeps all employees and adds department details wherever EmployeeID matches.
**Follow-up:** What if EmployeeID does not match? → Department will be NaN. I can identify these rows using `result[result["Department"].isna()]`, assuming Department is populated in the reference file.
### Q8. You have sales data with EmployeeID, Department, and SalesAmount. How would you calculate total sales and average sales for each department?
**Answer:** I would use `groupby()` with `agg()` to calculate multiple summaries.
```python
result = df.groupby("Department")["SalesAmount"].agg(
    ["sum", "mean", "count"]
).reset_index()
result.columns = [
    "Department", "TotalSales", "AverageSales", "Count"
]
```
**Explanation:** `groupby()` groups employees by department. `sum` calculates total sales, `mean` calculates average sales, and `count` counts non-null sales values.
**Follow-up:** What if I want only departments with sales above 50,000? →
```python
result = result[result["TotalSales"] > 50000]
```
### Q9. You receive multiple Excel files every day. How would you combine them into one DataFrame?
**Answer:** I would use `glob` to identify Excel files, read them using Pandas, and combine them using `concat()`.
```python
import glob
import pandas as pd
files = glob.glob("data/*.xlsx")
dfs = [pd.read_excel(file) for file in files]
combined = pd.concat(dfs, ignore_index=True)
combined.to_excel("combined.xlsx", index=False)
```
**Explanation:** `glob()` finds the files, `read_excel()` reads each file, and `concat()` combines their rows.
**Follow-up:** What if column names differ? → I would standardize column names using `rename()` before concatenation. Otherwise, Pandas may create separate columns.
### Q10. You have a DataFrame with Amount and TransactionType. How would you create a new column that marks transactions as High Value or Normal?
**Answer:** I would use NumPy `where()` for conditional data transformation instead of writing a loop.
```python
import numpy as np
df["Category"] = np.where(
    df["Amount"] >= 10000,
    "High Value",
    "Normal"
)
```
**Explanation:** `np.where()` checks the condition for every row. Amounts of 10,000 or above are marked High Value; the remaining amounts are marked Normal.
**Follow-up:** Why use NumPy instead of a for loop? → NumPy supports vectorized operations, which are generally faster and easier to maintain for large datasets.