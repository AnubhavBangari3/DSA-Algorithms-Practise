
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