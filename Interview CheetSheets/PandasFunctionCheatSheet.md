# PANDAS FUNCTIONS & SYNTAX CHEATSHEET

**Level:** EASY → MEDIUM → HARD
**Focus:** Python, Pandas, Data Transformation, ETL, Data Cleaning, Excel, CSV, APIs, Performance
**Import:** `import pandas as pd` and `import numpy as np`
**Example columns:** `Name`, `Age`, `Salary`, `Department`, `Date`, `ID`, `Amount`, `Status`
**Assumption:** `df` is a DataFrame containing the relevant columns. `df1` and `df2` are separate DataFrames. Examples are independent unless stated otherwise.

# PART 1: EASY — FUNDAMENTAL FUNCTIONS

## 1. DataFrame & Series Creation

| Function / Syntax             | Purpose                   | Example                                           |
| ----------------------------- | ------------------------- | ------------------------------------------------- |
| `pd.DataFrame()`              | Create DataFrame          | `pd.DataFrame({"A":[1,2],"B":[3,4]})`             |
| `pd.Series()`                 | Create Series             | `pd.Series([10,20,30])`                           |
| `pd.DataFrame.from_dict()`    | Create from dictionary    | `pd.DataFrame.from_dict({"A":[1,2]})`             |
| `pd.DataFrame.from_records()` | Create from records       | `pd.DataFrame.from_records([{"A":1},{"A":2}])`    |
| `pd.date_range()`             | Generate date range       | `pd.date_range("2026-01-01", periods=5)`          |
| `pd.period_range()`           | Generate periods          | `pd.period_range("2026-01", periods=3, freq="M")` |
| `pd.Index()`                  | Create index              | `pd.Index(["A","B","C"])`                         |
| `pd.MultiIndex.from_tuples()` | Create hierarchical index | `pd.MultiIndex.from_tuples([("IT",1),("HR",2)])`  |
| `pd.concat()`                 | Combine Series/DataFrames | `pd.concat([df1,df2])`                            |
| `pd.get_dummies()`            | One-hot encoding          | `pd.get_dummies(df["Department"])`                |

## 2. Reading Data

| Function / Syntax                | Purpose                       | Example                                             |
| -------------------------------- | ----------------------------- | --------------------------------------------------- |
| `pd.read_csv()`                  | Read CSV                      | `pd.read_csv("data.csv")`                           |
| `pd.read_excel()`                | Read Excel                    | `pd.read_excel("data.xlsx")`                        |
| `pd.read_json()`                 | Read JSON                     | `pd.read_json("data.json")`                         |
| `pd.read_parquet()`              | Read Parquet                  | `pd.read_parquet("data.parquet")`                   |
| `pd.read_sql()`                  | Read SQL query/table          | `pd.read_sql("SELECT * FROM employees",conn)`       |
| `pd.read_sql_query()`            | Read SQL query                | `pd.read_sql_query("SELECT * FROM employees",conn)` |
| `pd.read_sql_table()`            | Read SQL table                | `pd.read_sql_table("employees",engine)`             |
| `pd.read_html()`                 | Read HTML tables              | `pd.read_html("https://example.com")`               |
| `pd.read_xml()`                  | Read XML                      | `pd.read_xml("data.xml")`                           |
| `pd.read_pickle()`               | Read serialized Pandas object | `pd.read_pickle("data.pkl")`                        |
| `pd.read_feather()`              | Read Feather                  | `pd.read_feather("data.feather")`                   |
| `pd.read_csv(usecols=)`          | Read selected columns         | `pd.read_csv("data.csv",usecols=["ID","Amount"])`   |
| `pd.read_csv(nrows=)`            | Read limited rows             | `pd.read_csv("data.csv",nrows=100)`                 |
| `pd.read_csv(dtype=)`            | Specify data types            | `pd.read_csv("data.csv",dtype={"ID":"string"})`     |
| `pd.read_csv(parse_dates=)`      | Parse dates                   | `pd.read_csv("data.csv",parse_dates=["Date"])`      |
| `pd.read_csv(chunksize=)`        | Read in chunks                | `pd.read_csv("data.csv",chunksize=100000)`          |
| `pd.read_excel(sheet_name=)`     | Read specific sheet           | `pd.read_excel("data.xlsx",sheet_name="Sheet1")`    |
| `pd.read_excel(sheet_name=None)` | Read all sheets               | `pd.read_excel("data.xlsx",sheet_name=None)`        |
| `pd.ExcelFile()`                 | Inspect Excel workbook        | `pd.ExcelFile("data.xlsx").sheet_names`             |

## 3. Writing / Exporting Data

| Function / Syntax   | Purpose                     | Example                                                                  |
| ------------------- | --------------------------- | ------------------------------------------------------------------------ |
| `df.to_csv()`       | Export CSV                  | `df.to_csv("out.csv",index=False)`                                       |
| `df.to_excel()`     | Export Excel                | `df.to_excel("out.xlsx",index=False)`                                    |
| `df.to_json()`      | Export JSON                 | `df.to_json("out.json",orient="records")`                                |
| `df.to_parquet()`   | Export Parquet              | `df.to_parquet("out.parquet",index=False)`                               |
| `df.to_sql()`       | Write to SQL table          | `df.to_sql("employees",engine,if_exists="append",index=False)`           |
| `df.to_dict()`      | Convert to dictionary       | `df.to_dict(orient="records")`                                           |
| `df.to_numpy()`     | Convert to NumPy array      | `df.to_numpy()`                                                          |
| `df.to_records()`   | Convert to record array     | `df.to_records(index=False)`                                             |
| `df.to_pickle()`    | Serialize DataFrame         | `df.to_pickle("data.pkl")`                                               |
| `df.to_html()`      | Export HTML table           | `df.to_html("table.html")`                                               |
| `df.to_markdown()`  | Export Markdown table       | `df.to_markdown(index=False)`                                            |
| `df.to_clipboard()` | Copy to clipboard           | `df.to_clipboard(index=False)`                                           |
| `pd.ExcelWriter()`  | Write multiple Excel sheets | `with pd.ExcelWriter("out.xlsx") as w: df.to_excel(w,sheet_name="Data")` |

## 4. Data Inspection

| Function / Syntax                 | Purpose               | Example                           |
| --------------------------------- | --------------------- | --------------------------------- |
| `df.head()`                       | First 5 rows          | `df.head()`                       |
| `df.tail()`                       | Last 5 rows           | `df.tail()`                       |
| `df.sample()`                     | Random sample         | `df.sample(5)`                    |
| `df.shape`                        | Rows and columns      | `df.shape`                        |
| `df.size`                         | Total elements        | `df.size`                         |
| `df.ndim`                         | Number of dimensions  | `df.ndim`                         |
| `df.columns`                      | Column labels         | `df.columns`                      |
| `df.index`                        | Row labels            | `df.index`                        |
| `df.dtypes`                       | Column data types     | `df.dtypes`                       |
| `df.info()`                       | DataFrame summary     | `df.info()`                       |
| `df.describe()`                   | Numeric statistics    | `df.describe()`                   |
| `df.describe(include="all")`      | All-column statistics | `df.describe(include="all")`      |
| `df.memory_usage()`               | Memory per column     | `df.memory_usage(deep=True)`      |
| `df.empty`                        | Check empty DataFrame | `df.empty`                        |
| `len(df)`                         | Number of rows        | `len(df)`                         |
| `df.count()`                      | Non-null counts       | `df.count()`                      |
| `df.nunique()`                    | Unique counts         | `df.nunique()`                    |
| `df["Department"].unique()`       | Unique values         | `df["Department"].unique()`       |
| `df["Department"].value_counts()` | Frequency counts      | `df["Department"].value_counts()` |

## 5. Selection & Indexing

| Function / Syntax    | Purpose                        | Example                                  |
| -------------------- | ------------------------------ | ---------------------------------------- |
| `df["A"]`            | Select Series                  | `df["Salary"]`                           |
| `df[["A","B"]]`      | Select DataFrame columns       | `df[["Name","Salary"]]`                  |
| `df.loc[]`           | Label-based selection          | `df.loc[0:3,["Name","Salary"]]`          |
| `df.iloc[]`          | Position-based selection       | `df.iloc[0:3,0:2]`                       |
| `df.at[]`            | Access scalar by label         | `df.at[0,"Salary"]`                      |
| `df.iat[]`           | Access scalar by position      | `df.iat[0,2]`                            |
| `df.set_index()`     | Set index column               | `df.set_index("ID")`                     |
| `df.reset_index()`   | Reset index                    | `df.reset_index(drop=True)`              |
| `df.reindex()`       | Align to new index             | `df.reindex([0,1,2,3])`                  |
| `df.select_dtypes()` | Select by data type            | `df.select_dtypes(include="number")`     |
| `df.filter()`        | Select labels matching pattern | `df.filter(regex="Salary")`              |
| `df.xs()`            | Select cross-section           | `df.xs("IT",level="Department")`         |
| `df.get()`           | Get column with default        | `df.get("Bonus",pd.Series(dtype=float))` |

## 6. Filtering

| Function / Syntax | Purpose                      | Example                                    |
| ----------------- | ---------------------------- | ------------------------------------------ |
| `df[condition]`   | Filter rows                  | `df[df["Salary"]>50000]`                   |
| `&`               | AND condition                | `df[(df["Age"]>25)&(df["Salary"]>50000)]`  |
| `\|`              | OR condition                 | `df[(df["Age"]>30)\|(df["Salary"]>70000)]` |
| `~`               | NOT condition                | `df[~df["Department"].eq("IT")]`           |
| `.isin()`         | Match multiple values        | `df[df["Department"].isin(["IT","HR"])]`   |
| `.between()`      | Range filtering              | `df[df["Salary"].between(50000,70000)]`    |
| `.query()`        | Expression-based filtering   | `df.query("Salary>50000 and Age>25")`      |
| `.eq()`           | Equal comparison             | `df[df["Status"].eq("Success")]`           |
| `.ne()`           | Not equal                    | `df[df["Status"].ne("Failed")]`            |
| `.gt()`           | Greater than                 | `df[df["Salary"].gt(50000)]`               |
| `.ge()`           | Greater/equal                | `df[df["Salary"].ge(50000)]`               |
| `.lt()`           | Less than                    | `df[df["Salary"].lt(50000)]`               |
| `.le()`           | Less/equal                   | `df[df["Salary"].le(50000)]`               |
| `.where()`        | Keep matching; otherwise NaN | `df["Salary"].where(df["Salary"]>50000)`   |
| `.mask()`         | Replace matching with NaN    | `df["Salary"].mask(df["Salary"]<0)`        |

## 7. Sorting

| Function / Syntax   | Purpose          | Example                                    |
| ------------------- | ---------------- | ------------------------------------------ |
| `df.sort_values()`  | Sort by column   | `df.sort_values("Salary")`                 |
| `ascending=False`   | Descending sort  | `df.sort_values("Salary",ascending=False)` |
| `df.sort_index()`   | Sort by index    | `df.sort_index()`                          |
| `df.nlargest()`     | Top N values     | `df.nlargest(5,"Salary")`                  |
| `df.nsmallest()`    | Bottom N values  | `df.nsmallest(5,"Salary")`                 |
| `df["A"].argsort()` | Sorted positions | `df["Salary"].argsort()`                   |
| `df["A"].rank()`    | Rank values      | `df["Salary"].rank(ascending=False)`       |

## 8. Adding, Updating & Removing Columns

| Function / Syntax | Purpose                  | Example                               |
| ----------------- | ------------------------ | ------------------------------------- |
| `df["New"]=...`   | Add column               | `df["Bonus"]=df["Salary"]*0.1`        |
| `df.assign()`     | Add derived columns      | `df.assign(Bonus=df["Salary"]*0.1)`   |
| `df.insert()`     | Insert at position       | `df.insert(0,"Flag",1)`               |
| `df.rename()`     | Rename columns           | `df.rename(columns={"Salary":"Pay"})` |
| `df.drop()`       | Drop columns/rows        | `df.drop(columns=["Age"])`            |
| `df.pop()`        | Remove and return column | `df.pop("Age")`                       |
| `df.replace()`    | Replace values           | `df.replace({"IT":"Technology"})`     |
| `df.update()`     | Update matching cells    | `df.update(other_df)`                 |
| `df.add_prefix()` | Prefix column labels     | `df.add_prefix("emp_")`               |
| `df.add_suffix()` | Suffix column labels     | `df.add_suffix("_new")`               |
| `df.copy()`       | Copy DataFrame           | `df2=df.copy()`                       |

## 9. Missing Values

| Function / Syntax      | Purpose                            | Example                        |
| ---------------------- | ---------------------------------- | ------------------------------ |
| `df.isna()`            | Detect missing values              | `df.isna()`                    |
| `df.isnull()`          | Alias of isna                      | `df.isnull()`                  |
| `df.notna()`           | Detect non-missing                 | `df.notna()`                   |
| `df.notnull()`         | Alias of notna                     | `df.notnull()`                 |
| `df.isna().sum()`      | Count missing per column           | `df.isna().sum()`              |
| `df.isna().mean()`     | Missing fraction                   | `df.isna().mean()`             |
| `df.dropna()`          | Drop rows with missing values      | `df.dropna()`                  |
| `df.dropna(how="all")` | Drop fully missing rows            | `df.dropna(how="all")`         |
| `df.dropna(subset=)`   | Drop by required columns           | `df.dropna(subset=["Salary"])` |
| `df.fillna()`          | Fill missing values                | `df["Salary"].fillna(0)`       |
| `df.ffill()`           | Forward fill                       | `df.ffill()`                   |
| `df.bfill()`           | Backward fill                      | `df.bfill()`                   |
| `df.interpolate()`     | Interpolate missing numeric values | `df["Salary"].interpolate()`   |
| `df.combine_first()`   | Fill from another DataFrame        | `df.combine_first(other_df)`   |

## 10. Duplicates

| Function / Syntax           | Purpose                          | Example                             |
| --------------------------- | -------------------------------- | ----------------------------------- |
| `df.duplicated()`           | Identify duplicate rows          | `df.duplicated()`                   |
| `df.duplicated(keep=False)` | Mark all duplicate occurrences   | `df.duplicated(keep=False)`         |
| `df.drop_duplicates()`      | Remove duplicate rows            | `df.drop_duplicates()`              |
| `subset=["ID"]`             | Deduplicate by ID                | `df.drop_duplicates(subset=["ID"])` |
| `keep="first"`              | Keep first occurrence            | `df.drop_duplicates(keep="first")`  |
| `keep="last"`               | Keep last occurrence             | `df.drop_duplicates(keep="last")`   |
| `keep=False`                | Remove all duplicate occurrences | `df.drop_duplicates(keep=False)`    |
| `df.index.duplicated()`     | Find duplicate index labels      | `df.index.duplicated()`             |

## 11. Data Type Conversion

| Function / Syntax          | Purpose                   | Example                                       |
| -------------------------- | ------------------------- | --------------------------------------------- |
| `df.astype()`              | Convert dtype             | `df["Age"].astype("int64")`                   |
| `pd.to_numeric()`          | Convert to numeric        | `pd.to_numeric(df["Amount"],errors="coerce")` |
| `pd.to_datetime()`         | Convert to datetime       | `pd.to_datetime(df["Date"],errors="coerce")`  |
| `pd.to_timedelta()`        | Convert to time duration  | `pd.to_timedelta(["1 days","2 days"])`        |
| `df.convert_dtypes()`      | Infer nullable dtypes     | `df.convert_dtypes()`                         |
| `df.infer_objects()`       | Infer object column types | `df.infer_objects()`                          |
| `.astype("category")`      | Convert to category       | `df["Department"].astype("category")`         |
| `.astype("string")`        | Convert to string dtype   | `df["Name"].astype("string")`                 |
| `.astype("Int64")`         | Nullable integer          | `df["Age"].astype("Int64")`                   |
| `pd.to_numeric(downcast=)` | Reduce numeric storage    | `pd.to_numeric(df["Age"],downcast="integer")` |

# PART 2: MEDIUM — DATA MANIPULATION & TRANSFORMATION

## 12. Mathematical & Statistical Functions

| Function / Syntax | Purpose                 | Example                                           |
| ----------------- | ----------------------- | ------------------------------------------------- |
| `.sum()`          | Sum                     | `df["Salary"].sum()`                              |
| `.mean()`         | Average                 | `df["Salary"].mean()`                             |
| `.median()`       | Median                  | `df["Salary"].median()`                           |
| `.mode()`         | Most frequent values    | `df["Salary"].mode()`                             |
| `.min()`          | Minimum                 | `df["Salary"].min()`                              |
| `.max()`          | Maximum                 | `df["Salary"].max()`                              |
| `.std()`          | Standard deviation      | `df["Salary"].std()`                              |
| `.var()`          | Variance                | `df["Salary"].var()`                              |
| `.quantile()`     | Percentile/quantile     | `df["Salary"].quantile(0.75)`                     |
| `.prod()`         | Product                 | `df["Amount"].prod()`                             |
| `.abs()`          | Absolute value          | `df["Amount"].abs()`                              |
| `.round()`        | Round values            | `df["Salary"].round(2)`                           |
| `.clip()`         | Limit values to range   | `df["Salary"].clip(30000,100000)`                 |
| `.idxmax()`       | Index of maximum        | `df["Salary"].idxmax()`                           |
| `.idxmin()`       | Index of minimum        | `df["Salary"].idxmin()`                           |
| `.skew()`         | Skewness                | `df["Salary"].skew()`                             |
| `.kurt()`         | Kurtosis                | `df["Salary"].kurt()`                             |
| `.corr()`         | Correlation             | `df[["Age","Salary"]].corr()`                     |
| `.cov()`          | Covariance              | `df[["Age","Salary"]].cov()`                      |
| `.sem()`          | Standard error          | `df["Salary"].sem()`                              |
| `.mad()`          | Mean absolute deviation | `(df["Salary"]-df["Salary"].mean()).abs().mean()` |

## 13. GroupBy & Aggregation

| Function / Syntax        | Purpose                         | Example                                                              |
| ------------------------ | ------------------------------- | -------------------------------------------------------------------- |
| `df.groupby()`           | Group records                   | `df.groupby("Department")`                                           |
| `.groupby().sum()`       | Group sum                       | `df.groupby("Department")["Salary"].sum()`                           |
| `.groupby().mean()`      | Group average                   | `df.groupby("Department")["Salary"].mean()`                          |
| `.groupby().count()`     | Non-null count per group        | `df.groupby("Department")["Salary"].count()`                         |
| `.groupby().size()`      | Total rows per group            | `df.groupby("Department").size()`                                    |
| `.groupby().min()`       | Group minimum                   | `df.groupby("Department")["Salary"].min()`                           |
| `.groupby().max()`       | Group maximum                   | `df.groupby("Department")["Salary"].max()`                           |
| `.groupby().nunique()`   | Distinct count per group        | `df.groupby("Department")["ID"].nunique()`                           |
| `.groupby().agg()`       | Multiple aggregations           | `df.groupby("Department").agg(Total=("Salary","sum"))`               |
| `.groupby().transform()` | Preserve original row alignment | `df.groupby("Department")["Salary"].transform("mean")`               |
| `.groupby().apply()`     | Custom group function           | `df.groupby("Department")["Salary"].apply(lambda s:s.max()-s.min())` |
| `.groupby().filter()`    | Filter entire groups            | `df.groupby("Department").filter(lambda g:len(g)>2)`                 |
| `.groupby().head()`      | First N per group               | `df.groupby("Department").head(2)`                                   |
| `.groupby().tail()`      | Last N per group                | `df.groupby("Department").tail(2)`                                   |
| `.groupby().first()`     | First non-null per column       | `df.groupby("Department").first()`                                   |
| `.groupby().last()`      | Last non-null per column        | `df.groupby("Department").last()`                                    |
| `.groupby().nth()`       | Nth row per group               | `df.groupby("Department").nth(0)`                                    |
| `.groupby().cumcount()`  | Row number within group         | `df.groupby("Department").cumcount()+1`                              |
| `.groupby().cumsum()`    | Cumulative group sum            | `df.groupby("Department")["Salary"].cumsum()`                        |
| `.groupby().rank()`      | Rank within group               | `df.groupby("Department")["Salary"].rank()`                          |
| `.groupby().shift()`     | Previous/next value in group    | `df.groupby("Department")["Salary"].shift(1)`                        |
| `as_index=False`         | Keep group keys as columns      | `df.groupby("Department",as_index=False)["Salary"].sum()`            |
| `dropna=False`           | Include missing grouping keys   | `df.groupby("Department",dropna=False)["Salary"].sum()`              |

## 14. Merge, Join & Concat

| Function / Syntax        | Purpose                         | Example                                             |
| ------------------------ | ------------------------------- | --------------------------------------------------- |
| `pd.merge()`             | Join on keys                    | `pd.merge(df1,df2,on="ID")`                         |
| `how="inner"`            | Matching keys only              | `df1.merge(df2,on="ID",how="inner")`                |
| `how="left"`             | All left rows plus matches      | `df1.merge(df2,on="ID",how="left")`                 |
| `how="right"`            | All right rows plus matches     | `df1.merge(df2,on="ID",how="right")`                |
| `how="outer"`            | All keys from both sides        | `df1.merge(df2,on="ID",how="outer")`                |
| `how="cross"`            | Cartesian product               | `df1.merge(df2,how="cross")`                        |
| `left_on/right_on`       | Different join key names        | `df1.merge(df2,left_on="ID",right_on="EmpID")`      |
| `left_index/right_index` | Join using indexes              | `df1.merge(df2,left_index=True,right_index=True)`   |
| `suffixes=`              | Resolve overlapping names       | `df1.merge(df2,on="ID",suffixes=("_x","_y"))`       |
| `indicator=True`         | Identify match origin           | `df1.merge(df2,on="ID",how="outer",indicator=True)` |
| `validate="one_to_one"`  | Check unique keys on both sides | `df1.merge(df2,on="ID",validate="one_to_one")`      |
| `validate="many_to_one"` | Check right-side key uniqueness | `df1.merge(df2,on="ID",validate="many_to_one")`     |
| `df.join()`              | Join using index by default     | `df1.join(df2,lsuffix="_l",rsuffix="_r")`           |
| `pd.concat(axis=0)`      | Stack rows                      | `pd.concat([df1,df2],ignore_index=True)`            |
| `pd.concat(axis=1)`      | Combine columns by index        | `pd.concat([df1,df2],axis=1)`                       |
| `pd.concat(keys=)`       | Hierarchical source labels      | `pd.concat([df1,df2],keys=["Jan","Feb"])`           |
| `pd.merge_asof()`        | Nearest ordered-key join        | `pd.merge_asof(left_sorted,right_sorted,on="Date")` |
| `pd.merge_ordered()`     | Merge ordered/time-series data  | `pd.merge_ordered(df1,df2,on="Date")`               |

## 15. Apply, Map & Replace

| Function / Syntax         | Purpose                        | Example                                                                              |
| ------------------------- | ------------------------------ | ------------------------------------------------------------------------------------ |
| `Series.map()`            | Map values                     | `df["Department"].map({"IT":1,"HR":2})`                                              |
| `Series.apply()`          | Apply function per value       | `df["Salary"].apply(lambda x:x*2)`                                                   |
| `DataFrame.apply(axis=0)` | Apply to columns               | `df[["Age","Salary"]].apply("sum",axis=0)`                                           |
| `DataFrame.apply(axis=1)` | Apply to rows                  | `df.apply(lambda r:r["Salary"]*12,axis=1)`                                           |
| `DataFrame.map()`         | Element-wise DataFrame mapping | `df[["Age","Salary"]].map(lambda x:x*2)`                                             |
| `Series.replace()`        | Replace mapped values          | `df["Department"].replace({"IT":"Tech"})`                                            |
| `np.where()`              | Conditional assignment         | `np.where(df["Salary"]>50000,"High","Low")`                                          |
| `np.select()`             | Multiple conditions            | `np.select([df["Salary"]>70000,df["Salary"]>50000],["High","Medium"],default="Low")` |
| `.where()`                | Replace nonmatching with NaN   | `df["Salary"].where(df["Salary"]>0)`                                                 |
| `.mask()`                 | Replace matching with NaN      | `df["Salary"].mask(df["Salary"]<0)`                                                  |
| `.pipe()`                 | Chain custom functions         | `df.pipe(lambda x:x.dropna())`                                                       |

## 16. String Functions

| Function / Syntax   | Purpose                           | Example                                            |
| ------------------- | --------------------------------- | -------------------------------------------------- |
| `.str.lower()`      | Lowercase                         | `df["Name"].str.lower()`                           |
| `.str.upper()`      | Uppercase                         | `df["Name"].str.upper()`                           |
| `.str.title()`      | Title case                        | `df["Name"].str.title()`                           |
| `.str.capitalize()` | Capitalize first character        | `df["Name"].str.capitalize()`                      |
| `.str.strip()`      | Trim both sides                   | `df["Name"].str.strip()`                           |
| `.str.lstrip()`     | Trim left                         | `df["Name"].str.lstrip()`                          |
| `.str.rstrip()`     | Trim right                        | `df["Name"].str.rstrip()`                          |
| `.str.len()`        | String length                     | `df["Name"].str.len()`                             |
| `.str.contains()`   | Substring/regex match             | `df["Name"].str.contains("a",case=False,na=False)` |
| `.str.startswith()` | Starts with                       | `df["Name"].str.startswith("A")`                   |
| `.str.endswith()`   | Ends with                         | `df["Name"].str.endswith("a")`                     |
| `.str.replace()`    | Replace substring                 | `df["Name"].str.replace("a","x",regex=False)`      |
| `.str.split()`      | Split text                        | `df["Name"].str.split(" ")`                        |
| `.str.rsplit()`     | Split from right                  | `df["Name"].str.rsplit(" ",n=1)`                   |
| `.str.extract()`    | Extract regex group               | `df["Name"].str.extract(r"(\d+)")`                 |
| `.str.extractall()` | Extract all regex matches         | `df["Name"].str.extractall(r"(\d+)")`              |
| `.str.findall()`    | Find all matches                  | `df["Name"].str.findall(r"\d+")`                   |
| `.str.match()`      | Regex match from start            | `df["Name"].str.match(r"^A")`                      |
| `.str.fullmatch()`  | Match entire string               | `df["Name"].str.fullmatch(r"[A-Za-z]+")`           |
| `.str.slice()`      | Slice characters                  | `df["Name"].str.slice(0,3)`                        |
| `.str.get()`        | Get element/character             | `df["Name"].str.get(0)`                            |
| `.str.cat()`        | Concatenate strings               | `df["Name"].str.cat(sep=",")`                      |
| `.str.pad()`        | Pad strings                       | `df["Name"].str.pad(10,fillchar="0")`              |
| `.str.zfill()`      | Zero-pad strings                  | `df["ID"].astype(str).str.zfill(5)`                |
| `.str.count()`      | Count substring/regex occurrences | `df["Name"].str.count("a")`                        |
| `.str.isnumeric()`  | Check numeric strings             | `df["Name"].str.isnumeric()`                       |
| `.str.isalpha()`    | Check alphabetic strings          | `df["Name"].str.isalpha()`                         |

## 17. Datetime Functions

| Function / Syntax    | Purpose                | Example                                               |
| -------------------- | ---------------------- | ----------------------------------------------------- |
| `pd.to_datetime()`   | Parse dates            | `pd.to_datetime(df["Date"],errors="coerce")`          |
| `pd.Timestamp()`     | Create timestamp       | `pd.Timestamp("2026-01-01")`                          |
| `pd.Timedelta()`     | Create duration        | `pd.Timedelta(days=7)`                                |
| `pd.date_range()`    | Generate dates         | `pd.date_range("2026-01-01",periods=10,freq="D")`     |
| `.dt.year`           | Extract year           | `df["Date"].dt.year`                                  |
| `.dt.month`          | Extract month          | `df["Date"].dt.month`                                 |
| `.dt.day`            | Extract day            | `df["Date"].dt.day`                                   |
| `.dt.hour`           | Extract hour           | `df["Date"].dt.hour`                                  |
| `.dt.minute`         | Extract minute         | `df["Date"].dt.minute`                                |
| `.dt.second`         | Extract second         | `df["Date"].dt.second`                                |
| `.dt.day_name()`     | Day name               | `df["Date"].dt.day_name()`                            |
| `.dt.month_name()`   | Month name             | `df["Date"].dt.month_name()`                          |
| `.dt.dayofweek`      | Weekday number         | `df["Date"].dt.dayofweek`                             |
| `.dt.dayofyear`      | Day of year            | `df["Date"].dt.dayofyear`                             |
| `.dt.quarter`        | Quarter                | `df["Date"].dt.quarter`                               |
| `.dt.is_month_end`   | Check month end        | `df["Date"].dt.is_month_end`                          |
| `.dt.is_month_start` | Check month start      | `df["Date"].dt.is_month_start`                        |
| `.dt.strftime()`     | Format dates           | `df["Date"].dt.strftime("%Y-%m-%d")`                  |
| `.dt.to_period()`    | Convert to period      | `df["Date"].dt.to_period("M")`                        |
| `.dt.normalize()`    | Remove time component  | `df["Date"].dt.normalize()`                           |
| `.dt.floor()`        | Round down time        | `df["Date"].dt.floor("h")`                            |
| `.dt.ceil()`         | Round up time          | `df["Date"].dt.ceil("h")`                             |
| `.dt.round()`        | Round timestamp        | `df["Date"].dt.round("h")`                            |
| `.dt.tz_localize()`  | Assign timezone        | `df["Date"].dt.tz_localize("UTC")`                    |
| `.dt.tz_convert()`   | Convert timezone       | `df["Date"].dt.tz_convert("Asia/Kolkata")`            |
| `.resample()`        | Time-based aggregation | `df.set_index("Date").resample("MS")["Amount"].sum()` |

## 18. Pivot & Reshaping

| Function / Syntax   | Purpose                             | Example                                                             |
| ------------------- | ----------------------------------- | ------------------------------------------------------------------- |
| `df.pivot()`        | Long to wide; unique pairs required | `df.pivot(index="ID",columns="Department",values="Salary")`         |
| `df.pivot_table()`  | Pivot with aggregation              | `df.pivot_table(index="Department",values="Salary",aggfunc="mean")` |
| `df.melt()`         | Wide to long                        | `df.melt(id_vars="ID",value_vars=["Jan","Feb"])`                    |
| `df.stack()`        | Columns to index level              | `df.stack()`                                                        |
| `df.unstack()`      | Index level to columns              | `df.unstack()`                                                      |
| `df.explode()`      | Expand list elements into rows      | `df.explode("Skills")`                                              |
| `df.transpose()`    | Swap rows and columns               | `df.transpose()`                                                    |
| `df.T`              | Transpose shorthand                 | `df.T`                                                              |
| `pd.crosstab()`     | Frequency cross-tabulation          | `pd.crosstab(df["Department"],df["Status"])`                        |
| `pd.cut()`          | Fixed-width/value bins              | `pd.cut(df["Age"],bins=[0,18,30,60])`                               |
| `pd.qcut()`         | Quantile bins                       | `pd.qcut(df["Salary"],q=4,duplicates="drop")`                       |
| `pd.wide_to_long()` | Reshape repeated column patterns    | `pd.wide_to_long(df,stubnames="Sales",i="ID",j="Year",sep="_")`     |

# PART 3: HARD — ADVANCED ANALYTICS & ETL

## 19. Window, Ranking & Cumulative Functions

| Function / Syntax       | Purpose                       | Example                                                    |
| ----------------------- | ----------------------------- | ---------------------------------------------------------- |
| `.rank()`               | Rank values                   | `df["Salary"].rank(ascending=False)`                       |
| `.rank(method="dense")` | Dense rank                    | `df["Salary"].rank(method="dense")`                        |
| `.rank(method="min")`   | Competition-style rank        | `df["Salary"].rank(method="min")`                          |
| `.shift(1)`             | Previous row value            | `df["Amount"].shift(1)`                                    |
| `.shift(-1)`            | Next row value                | `df["Amount"].shift(-1)`                                   |
| `.diff()`               | Difference from previous      | `df["Amount"].diff()`                                      |
| `.pct_change()`         | Fractional change             | `df["Amount"].pct_change()*100`                            |
| `.cumsum()`             | Cumulative sum                | `df["Amount"].cumsum()`                                    |
| `.cumprod()`            | Cumulative product            | `df["Amount"].cumprod()`                                   |
| `.cummax()`             | Cumulative maximum            | `df["Amount"].cummax()`                                    |
| `.cummin()`             | Cumulative minimum            | `df["Amount"].cummin()`                                    |
| `.rolling()`            | Moving window                 | `df["Amount"].rolling(3).mean()`                           |
| `.expanding()`          | Expanding window              | `df["Amount"].expanding().mean()`                          |
| `.ewm()`                | Exponentially weighted window | `df["Amount"].ewm(span=3).mean()`                          |
| `.groupby().shift()`    | Previous value per group      | `df.groupby("Department")["Salary"].shift()`               |
| `.groupby().cumsum()`   | Cumulative sum per group      | `df.groupby("Department")["Salary"].cumsum()`              |
| `.groupby().rank()`     | Rank within group             | `df.groupby("Department")["Salary"].rank(ascending=False)` |
| `.groupby().cumcount()` | Row sequence per group        | `df.groupby("Department").cumcount()+1`                    |

## 20. Advanced Data Validation

| Function / Syntax                 | Purpose                           | Example                                             |
| --------------------------------- | --------------------------------- | --------------------------------------------------- |
| `df.equals()`                     | Compare entire DataFrames         | `df1.equals(df2)`                                   |
| `df.compare()`                    | Show differences (aligned labels) | `df1.compare(df2)`                                  |
| `pd.testing.assert_frame_equal()` | Assert DataFrame equality         | `pd.testing.assert_frame_equal(df1,df2)`            |
| `df.index.is_unique`              | Check unique index                | `df.index.is_unique`                                |
| `df["ID"].is_unique`              | Check unique IDs                  | `df["ID"].is_unique`                                |
| `df.isna().any()`                 | Any missing values by column      | `df.isna().any()`                                   |
| `df.isna().all()`                 | Entirely missing columns          | `df.isna().all()`                                   |
| `df.duplicated().sum()`           | Count duplicates                  | `df.duplicated().sum()`                             |
| `df["Amount"].between()`          | Validate numeric range            | `df["Amount"].between(0,100000)`                    |
| `df["Status"].isin()`             | Validate categories               | `df["Status"].isin(["Success","Failed"])`           |
| `df["Date"].notna()`              | Validate parsed dates             | `df["Date"].notna()`                                |
| `df["Amount"].ge(0)`              | Check non-negative values         | `df["Amount"].ge(0)`                                |
| `df["ID"].nunique()`              | Distinct key count                | `df["ID"].nunique()`                                |
| `df.merge(indicator=True)`        | Reconciliation match status       | `df1.merge(df2,on="ID",how="outer",indicator=True)` |
| `df.merge(validate=)`             | Validate join cardinality         | `df1.merge(df2,on="ID",validate="one_to_one")`      |

## 21. Performance & Memory Optimization

| Function / Syntax              | Purpose                              | Example                                                    |
| ------------------------------ | ------------------------------------ | ---------------------------------------------------------- |
| `df.memory_usage(deep=True)`   | Detailed memory consumption          | `df.memory_usage(deep=True)`                               |
| `df.info(memory_usage="deep")` | Detailed DataFrame memory summary    | `df.info(memory_usage="deep")`                             |
| `pd.to_numeric(downcast=)`     | Reduce numeric dtype size            | `pd.to_numeric(df["Age"],downcast="integer")`              |
| `.astype("category")`          | Optimize repeated categories         | `df["Department"].astype("category")`                      |
| `pd.read_csv(usecols=)`        | Load selected columns                | `pd.read_csv("large.csv",usecols=["ID","Amount"])`         |
| `pd.read_csv(dtype=)`          | Specify memory-efficient types       | `pd.read_csv("large.csv",dtype={"ID":"int32"})`            |
| `pd.read_csv(chunksize=)`      | Stream CSV chunks                    | `pd.read_csv("large.csv",chunksize=100000)`                |
| `pd.read_parquet(columns=)`    | Read selected Parquet columns        | `pd.read_parquet("large.parquet",columns=["ID","Amount"])` |
| `df.eval()`                    | Evaluate column expressions          | `df.eval("Bonus=Salary*0.1")`                              |
| `df.query()`                   | Expression-based filtering           | `df.query("Salary>50000")`                                 |
| `df.copy(deep=True)`           | Explicit deep copy                   | `df.copy(deep=True)`                                       |
| `pd.concat()`                  | Efficiently combine collected frames | `pd.concat(frames,ignore_index=True)`                      |
| `df.itertuples()`              | Iterate rows as tuples               | `for row in df.itertuples(index=False): print(row)`        |
| `df.iterrows()`                | Iterate rows as Series               | `for idx,row in df.iterrows(): print(idx)`                 |
| `df.to_numpy()`                | Access underlying values as array    | `df[["Age","Salary"]].to_numpy()`                          |

## 22. Advanced ETL Operations

| Function / Syntax     | Purpose                     | Example                                                           |
| --------------------- | --------------------------- | ----------------------------------------------------------------- |
| `pd.json_normalize()` | Flatten nested JSON         | `pd.json_normalize([{"user":{"name":"A"}}])`                      |
| `pd.concat()`         | Combine monthly files       | `pd.concat([pd.read_csv(f) for f in files],ignore_index=True)`    |
| `pd.merge()`          | Join reference/master data  | `transactions.merge(customers,on="CustomerID",how="left")`        |
| `.drop_duplicates()`  | Deduplicate business keys   | `df.drop_duplicates(subset=["TransactionID"])`                    |
| `.groupby().agg()`    | Create summary report       | `df.groupby("Region").agg(Total=("Amount","sum"))`                |
| `.assign()`           | Create derived columns      | `df.assign(Tax=df["Amount"]*0.18)`                                |
| `.pipe()`             | Chain ETL functions         | `df.pipe(clean_data).pipe(validate_data)`                         |
| `.explode()`          | Flatten list-valued column  | `df.explode("Items")`                                             |
| `.melt()`             | Normalize wide spreadsheets | `df.melt(id_vars=["ID"])`                                         |
| `.pivot_table()`      | Generate aggregated report  | `df.pivot_table(index="Region",values="Amount",aggfunc="sum")`    |
| `.to_sql()`           | Load into database          | `df.to_sql("transactions",engine,if_exists="append",index=False)` |
| `.to_parquet()`       | Store analytical dataset    | `df.to_parquet("cleaned.parquet",index=False)`                    |
| `.to_csv()`           | Export processed data       | `df.to_csv("processed.csv",index=False)`                          |

# PART 4: MOST IMPORTANT PANDAS FORMULAS

## 23. Data Cleaning Formulas

| Task                             | Formula / Syntax                                           |
| -------------------------------- | ---------------------------------------------------------- |
| Count missing values             | `df.isna().sum()`                                          |
| Total missing cells              | `df.isna().sum().sum()`                                    |
| Missing percentage               | `df.isna().mean()*100`                                     |
| Rows containing missing values   | `df[df.isna().any(axis=1)]`                                |
| Remove missing salary            | `df.dropna(subset=["Salary"])`                             |
| Fill missing salary with mean    | `df["Salary"].fillna(df["Salary"].mean())`                 |
| Fill missing salary with median  | `df["Salary"].fillna(df["Salary"].median())`               |
| Fill missing department          | `df["Department"].fillna("Unknown")`                       |
| Find duplicate rows              | `df[df.duplicated(keep=False)]`                            |
| Count duplicate rows after first | `df.duplicated().sum()`                                    |
| Remove duplicate IDs             | `df.drop_duplicates(subset=["ID"])`                        |
| Keep latest record by date       | `df.sort_values("Date").drop_duplicates("ID",keep="last")` |
| Remove leading/trailing spaces   | `df["Name"].str.strip()`                                   |
| Standardize text case            | `df["Department"].str.upper()`                             |
| Convert invalid numbers to NaN   | `pd.to_numeric(df["Amount"],errors="coerce")`              |
| Convert invalid dates to NaT     | `pd.to_datetime(df["Date"],errors="coerce")`               |
| Remove negative amounts          | `df[df["Amount"]>=0]`                                      |
| Find invalid categories          | `df[~df["Status"].isin(["Success","Failed"])]`             |

## 24. Aggregation & Analysis Formulas

| Task                               | Formula / Syntax                                                         |
| ---------------------------------- | ------------------------------------------------------------------------ |
| Total salary                       | `df["Salary"].sum()`                                                     |
| Average salary                     | `df["Salary"].mean()`                                                    |
| Median salary                      | `df["Salary"].median()`                                                  |
| Maximum salary                     | `df["Salary"].max()`                                                     |
| Minimum salary                     | `df["Salary"].min()`                                                     |
| Top 3 salaries                     | `df.nlargest(3,"Salary")`                                                |
| Bottom 3 salaries                  | `df.nsmallest(3,"Salary")`                                               |
| Second-highest distinct salary     | `df["Salary"].dropna().drop_duplicates().nlargest(2).iloc[-1]`           |
| Salary by department               | `df.groupby("Department")["Salary"].sum()`                               |
| Average salary by department       | `df.groupby("Department")["Salary"].mean()`                              |
| Employee count per department      | `df.groupby("Department").size()`                                        |
| Unique employees per department    | `df.groupby("Department")["ID"].nunique()`                               |
| Department average per employee    | `df.groupby("Department")["Salary"].transform("mean")`                   |
| Employees above department average | `df[df["Salary"]>df.groupby("Department")["Salary"].transform("mean")]`  |
| Salary rank                        | `df["Salary"].rank(ascending=False)`                                     |
| Rank within department             | `df.groupby("Department")["Salary"].rank(ascending=False)`               |
| Top 2 employees per department     | `df.sort_values("Salary",ascending=False).groupby("Department").head(2)` |
| Cumulative amount                  | `df["Amount"].cumsum()`                                                  |
| Previous amount                    | `df["Amount"].shift(1)`                                                  |
| Amount difference                  | `df["Amount"].diff()`                                                    |
| Percentage change                  | `df["Amount"].pct_change()*100`                                          |
| 3-row moving average               | `df["Amount"].rolling(3).mean()`                                         |
| Percentage contribution            | `df["Amount"]/df["Amount"].sum()*100`                                    |

## 25. Joins & Reconciliation Formulas

| Task                         | Formula / Syntax                                                                |
| ---------------------------- | ------------------------------------------------------------------------------- |
| Inner join                   | `df1.merge(df2,on="ID",how="inner")`                                            |
| Left join                    | `df1.merge(df2,on="ID",how="left")`                                             |
| Right join                   | `df1.merge(df2,on="ID",how="right")`                                            |
| Full outer join              | `df1.merge(df2,on="ID",how="outer")`                                            |
| Join different key names     | `df1.merge(df2,left_on="ID",right_on="EmpID")`                                  |
| Join on index                | `df1.join(df2)`                                                                 |
| Stack datasets vertically    | `pd.concat([df1,df2],ignore_index=True)`                                        |
| Combine columns horizontally | `pd.concat([df1,df2],axis=1)`                                                   |
| Identify unmatched rows      | `df1.merge(df2,on="ID",how="left",indicator=True).query("_merge=='left_only'")` |
| Validate unique join keys    | `df1.merge(df2,on="ID",validate="one_to_one")`                                  |
| Identify changed values      | `df1.compare(df2)`                                                              |
| Find IDs missing in target   | `df1[~df1["ID"].isin(df2["ID"])]`                                               |
| Find matching IDs            | `df1[df1["ID"].isin(df2["ID"])]`                                                |

## 26. Date & Time Formulas

| Task                         | Formula / Syntax                                           |
| ---------------------------- | ---------------------------------------------------------- |
| Convert date column          | `pd.to_datetime(df["Date"])`                               |
| Extract year                 | `df["Date"].dt.year`                                       |
| Extract month                | `df["Date"].dt.month`                                      |
| Extract day                  | `df["Date"].dt.day`                                        |
| Extract weekday              | `df["Date"].dt.day_name()`                                 |
| Extract quarter              | `df["Date"].dt.quarter`                                    |
| Monthly grouping             | `df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()` |
| Monthly resampling           | `df.set_index("Date").resample("MS")["Amount"].sum()`      |
| Calculate days between dates | `(df["EndDate"]-df["StartDate"]).dt.days`                  |
| Add 7 days                   | `df["Date"]+pd.Timedelta(days=7)`                          |
| Filter after date            | `df[df["Date"]>=pd.Timestamp("2026-01-01")]`               |
| Convert UTC to IST           | `df["Date"].dt.tz_convert("Asia/Kolkata")`                 |
| Remove time of day           | `df["Date"].dt.normalize()`                                |
| Format date as string        | `df["Date"].dt.strftime("%d-%m-%Y")`                       |

# PART 5: TOP INTERVIEW DIFFERENCES

| Concept A       | Concept B         | Main Difference                                     |
| --------------- | ----------------- | --------------------------------------------------- |
| Series          | DataFrame         | 1D vs 2D                                            |
| `loc`           | `iloc`            | Labels vs positions                                 |
| `at`            | `iat`             | Scalar label vs scalar position                     |
| `merge`         | `concat`          | Key-based join vs axis combination                  |
| `merge`         | `join`            | General key joins vs convenient index joins         |
| `agg`           | `transform`       | Summary vs original-row-aligned results             |
| `apply`         | `map`             | Axis/custom operations vs element mapping           |
| `pivot`         | `pivot_table`     | Unique combinations vs aggregation                  |
| `melt`          | `pivot`           | Wide-to-long vs long-to-wide                        |
| `count`         | `size`            | Non-null values vs all rows/elements                |
| `unique`        | `nunique`         | Distinct values vs distinct count                   |
| `isna`          | `notna`           | Missing vs non-missing                              |
| `fillna`        | `dropna`          | Replace missing vs remove missing                   |
| `duplicated`    | `drop_duplicates` | Identify vs remove duplicates                       |
| `astype`        | `to_numeric`      | Type casting vs numeric parsing                     |
| `tz_localize`   | `tz_convert`      | Assign timezone vs convert timezone                 |
| `shift`         | `diff`            | Previous/next value vs difference                   |
| `rolling`       | `expanding`       | Fixed/moving window vs growing window               |
| `cut`           | `qcut`            | Fixed value bins vs quantile bins                   |
| `CSV`           | `Parquet`         | Text row-oriented vs binary columnar                |
| `iterrows`      | `itertuples`      | Series-based row iteration vs tuple-based iteration |
| `DataFrame.map` | `Series.map`      | All DataFrame elements vs Series elements           |

# PART 6: FINAL UBER INTERVIEW PRIORITY

| Priority                                                                                                                       | Functions to Master                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| 🔴 VERY HIGH                                                                                                                   | `read_csv`, `read_excel`, `head`, `info`, `loc`, `iloc`, `query`, `isna`, `fillna`, `dropna`, `drop_duplicates` |
| 🔴 VERY HIGH                                                                                                                   | `astype`, `to_numeric`, `to_datetime`, `groupby`, `agg`, `transform`, `merge`, `join`, `concat`                 |
| 🔴 VERY HIGH                                                                                                                   | `apply`, `map`, `sort_values`, `pivot_table`, `melt`, `value_counts`, `nunique`                                 |
| 🟠 HIGH                                                                                                                        | `rank`, `shift`, `diff`, `pct_change`, `rolling`, `cumsum`, `resample`                                          |
| 🟠 HIGH                                                                                                                        | `read_json`, `json_normalize`, `read_parquet`, `to_parquet`, `to_excel`, `to_sql`                               |
| 🟠 HIGH                                                                                                                        | `duplicated`, `merge(indicator=True)`, `merge(validate=)`, `compare`, `isin`, `between`                         |
| 🟡 MEDIUM                                                                                                                      | `cut`, `qcut`, `explode`, `stack`, `unstack`, `crosstab`, `merge_asof`                                          |
| 🟡 MEDIUM                                                                                                                      | `memory_usage`, `convert_dtypes`, `downcast`, `chunksize`, `category`                                           |
| 🟢 LOW                                                                                                                         | `ewm`, `merge_ordered`, `wide_to_long`, `MultiIndex`, `read_feather`                                            |
| **Final Preparation Rule:** For every important function, know its purpose, syntax, input, output, and one practical use case. |                                                                                                                 |
| **Most important Uber interview pattern:** Read data → inspect → clean → validate → transform → merge → aggregate → export.    |                                                                                                                 |
