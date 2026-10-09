# STREAMLIT — UBER PYTHON AUTOMATION ENGINEER INTERVIEW CHEATSHEET
**Role:** Python Automation Engineer | Data & Analytics | 3–5 Years
**Priority:** Medium — Mentioned by Surya, not explicitly required in JD.
**Focus:** Streamlit basics, Python/Pandas integration, Excel/CSV uploads, data transformations, visualizations, exceptions, alerts, and practical interview scenarios.
## 1. What Is Streamlit?
Streamlit is an open-source Python framework used to create interactive web applications and data dashboards with Python.
It is commonly used for:
- Data analysis dashboards.
- Excel/CSV processing tools.
- Pandas DataFrame visualization.
- Internal automation interfaces.
- Simple data validation and reporting applications.

**Interview Answer:** "Streamlit is a Python framework for building interactive data applications without writing a separate frontend in React or JavaScript. It can be used to upload files, process data with Pandas, display results, and download reports."

## 2. Streamlit vs Pandas vs Tableau
| Technology | Purpose |
|---|---|
| Streamlit | Build interactive Python-based data applications |
| Pandas | Clean, transform, join, aggregate, and analyze tabular data |
| NumPy | Perform numerical and vectorized calculations |
| Tableau | Create business intelligence dashboards and reports |

**Interview Answer:** "Pandas performs data transformations, Streamlit provides the user interface, and Tableau is a dedicated BI and visualization platform."


## 3. Installation and Running an Application
**Install:**
```bash
pip install streamlit pandas openpyxl pyarrow
```
**Create:** `app.py`
```python
import streamlit as st
st.title("Uber Data Processing Dashboard")
st.write("Upload and process your data")
```
**Run:**
```bash
streamlit run app.py
```
**Alternative:**
```bash
python -m streamlit run app.py
```
**Interview Question:** How does Streamlit work?
**Answer:** "Streamlit executes the Python application script and renders UI elements in a browser. When a user interacts with widgets, the script generally reruns from top to bottom, while session state and caching help preserve data or avoid unnecessary computation."
## 4. Important Streamlit Functions
| Function | Purpose |
|---|---|
| `st.title()` | Display page title |
| `st.header()` | Display section heading |
| `st.subheader()` | Display smaller heading |
| `st.write()` | Display text, objects, or data |
| `st.text()` | Display plain text |
| `st.markdown()` | Display Markdown |
| `st.dataframe()` | Display interactive DataFrame |
| `st.table()` | Display static table |
| `st.metric()` | Display KPI/metric |
| `st.file_uploader()` | Upload CSV/Excel files |
| `st.button()` | Trigger an action |
| `st.selectbox()` | Select one option |
| `st.multiselect()` | Select multiple options |
| `st.checkbox()` | Boolean selection |
| `st.slider()` | Select numeric value/range |
| `st.download_button()` | Download processed output |
| `st.error()` | Display error message |
| `st.warning()` | Display warning |
| `st.success()` | Display success message |
| `st.info()` | Display information |
| `st.spinner()` | Display processing indicator |
| `st.stop()` | Stop execution of the current run |
## 5. Display a Pandas DataFrame
```python
import streamlit as st
import pandas as pd
df = pd.DataFrame({
    "TransactionID": [101, 102, 103],
    "Amount": [1000, 2000, 3000]
})
st.title("Transaction Dashboard")
st.dataframe(df)
```
**Interview Answer:** "I can display a Pandas DataFrame using `st.dataframe()`, which provides an interactive table for exploring data."
## 6. Upload a CSV File
```python
import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
```
**Workflow:** User uploads CSV → Pandas reads file → Streamlit displays records.
## 7. Upload an Excel File
```python
uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx"]
)
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
```
**Important:** `openpyxl` is commonly used by Pandas for `.xlsx` files.
## 8. Handle Multiple Excel Sheets
```python
uploaded_file = st.file_uploader(
    "Upload Excel workbook",
    type=["xlsx"]
)
if uploaded_file is not None:
    excel = pd.ExcelFile(uploaded_file)
    sheet = st.selectbox("Choose sheet", excel.sheet_names)
    df = pd.read_excel(excel, sheet_name=sheet)
    st.dataframe(df)
```
**Uber Scenario:** "An Excel workbook contains 10 sheets. How will you let users choose which sheet to process?"
**Answer:** "I would read the workbook's sheet names with Pandas, display them through `st.selectbox()`, and load the selected sheet."
## 9. Filter Data Using Streamlit
```python
df = pd.DataFrame({
    "Department": ["Tax", "Finance", "Tax"],
    "Amount": [1000, 2000, 3000]
})
department = st.selectbox(
    "Choose Department",
    df["Department"].unique()
)
filtered_df = df[df["Department"] == department]
st.dataframe(filtered_df)
```
**Interview Answer:** "Streamlit captures the user's filter selection, and Pandas performs the actual filtering."
## 10. Perform Data Transformations
```python
df = pd.DataFrame({
    "TransactionID": [101, 102, 103],
    "Amount": [1000, 2000, 3000]
})
if st.button("Calculate Fee"):
    df["Fee"] = df["Amount"] * 0.02
    st.dataframe(df)
```
**Interview Answer:** "I would keep the transformation logic in reusable Python functions and use Streamlit only to trigger and display the results."
## 11. Handle Null Values
```python
df = pd.DataFrame({
    "TransactionID": [101, 102, 103],
    "Amount": [100.0, None, 300.0]
})
missing_count = df["Amount"].isna().sum()
st.metric("Missing Amounts", missing_count)
valid_df = df.dropna(subset=["Amount"])
st.dataframe(valid_df)
```
**Uber Scenario:** "How would you display records with missing mandatory fields?"
**Answer:** "I would use Pandas to identify invalid records, display their count with `st.metric()`, and show rejected records separately. I would not automatically replace mandatory financial values with zero."
## 12. Detect Duplicate Primary Keys
```python
df = pd.DataFrame({
    "TransactionID": [101, 102, 101, 103],
    "Amount": [100, 200, 300, 400]
})
duplicates = df[
    df.duplicated(subset=["TransactionID"], keep=False)
]
st.metric("Duplicate Records", len(duplicates))
st.dataframe(duplicates)
```
**Interview Answer:** "I would check primary-key uniqueness using Pandas and display duplicate records for investigation before loading data."
## 13. GroupBy and Summarization
```python
df = pd.DataFrame({
    "Department": ["Tax", "Finance", "Tax"],
    "Amount": [1000, 2000, 3000]
})
summary = df.groupby("Department", as_index=False)["Amount"].sum()
st.dataframe(summary)
st.bar_chart(summary.set_index("Department"))
```
**Uber Scenario:** "How would you build a simple dashboard showing total transaction amounts by department?"
**Answer:** "I would aggregate data with Pandas `groupby()` and display the results using Streamlit charts and metrics."
## 14. Display Metrics
```python
st.metric("Total Records", len(df))
st.metric("Total Amount", f"{df['Amount'].sum():,.2f}")
st.metric("Missing Amounts", df["Amount"].isna().sum())
```
**Use Cases:** Total transactions, valid records, rejected records, processing counts, aggregate amounts.
## 15. Basic Charts
```python
st.line_chart(df.set_index("TransactionID")["Amount"])
st.bar_chart(df.set_index("TransactionID")["Amount"])
```
| Function | Use |
|---|---|
| `st.line_chart()` | Trends |
| `st.bar_chart()` | Comparisons |
| `st.area_chart()` | Area trends |
**Important:** Streamlit charts are sufficient for simple internal dashboards; Tableau remains the primary BI tool mentioned in the Uber JD.
## 16. Download Processed Data
```python
csv_data = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download Processed CSV",
    data=csv_data,
    file_name="processed_transactions.csv",
    mime="text/csv"
)
```
**Interview Answer:** "After transformation and validation, I can convert the DataFrame to CSV and let the user download the processed output."
## 17. Display Exceptions and Errors
```python
try:
    df = pd.read_csv("transactions.csv")
    st.success("File processed successfully")
except FileNotFoundError:
    st.error("Input file not found")
except pd.errors.ParserError:
    st.error("CSV parsing failed")
```
**Important:** `st.error()` only displays a message in the application. It does not automatically send an email, Teams message, or Slack alert.
## 18. How Would You Send Exception Alerts?
**Uber Scenario:** "A Streamlit data-processing application fails. How will you notify the support team?"
**Answer:**
1. Catch the exception in the processing function.
2. Log the full error on the server.
3. Display a safe error message using `st.error()`.
4. Send an alert through an approved email, Teams, Slack, or monitoring integration.
5. Include job ID, error type, timestamp, and log reference.
6. Avoid exposing credentials or sensitive records.
**Example:**
```python
import logging
import streamlit as st
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception("Processing failed")
    st.error("Processing failed. Please contact support.")
```
**Interview Answer:** "Streamlit handles user-facing error messages, while Python logging and a separate notification integration handle operational alerts."
## 19. Streamlit Session State
**Definition:** `st.session_state` stores values across reruns for a user's session.
```python
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(st.session_state.count)
```
**Interview Question:** Why use session state?
**Answer:** "Streamlit reruns the script on user interactions. Session state helps preserve values such as selections, counters, or processing results between reruns."
## 20. Streamlit Caching
**Definition:** Caching avoids unnecessarily repeating expensive operations.
```python
@st.cache_data
def load_data():
    return pd.read_parquet("transactions.parquet")
df = load_data()
st.dataframe(df.head())
```
| Feature | Use |
|---|---|
| `st.cache_data` | Cache data-loading or transformation results |
| `st.cache_resource` | Cache shared resources such as database connections or models |
**Interview Answer:** "I would cache expensive read or transformation operations where appropriate, but ensure cached data is refreshed when the underlying source changes."
**Important:** Be careful with sensitive data and shared caches in multi-user applications.
## 21. Large Files — More Than One Million Rows
**Uber Scenario:** "A user uploads a CSV containing 2 million records through Streamlit. How will you process it?"
**Answer:**
1. Validate file type and size.
2. Avoid rendering the entire dataset.
3. Read CSV in chunks using Pandas when necessary.
4. Apply transformations to each chunk.
5. Track valid and rejected records.
6. Store intermediate results in staging or Parquet.
7. Display only a sample and summary metrics.
8. Provide a downloadable output or a reference to the generated file.
**Important:** Streamlit is a UI framework, not a distributed data-processing engine. For very large workloads, processing may be better handled by a backend job or database.
## 22. Streamlit + SQL Database
**Uber Scenario:** "How would you show Oracle database records in Streamlit?"
**Answer:** "I would use a supported Python database connector or SQLAlchemy engine, execute a filtered query, load the required result into Pandas, and display it using Streamlit. I would keep credentials in an approved secret manager or environment configuration."
**Workflow:** Oracle → SQL Query → Pandas DataFrame → Streamlit Dashboard.
## 23. Streamlit + Parquet
```python
df = pd.read_parquet("transactions.parquet")
st.dataframe(df.head(100))
```
**Interview Answer:** "I can use Pandas to read Parquet files and Streamlit to display summaries and previews. For large files, I would avoid loading or rendering unnecessary columns and rows."
## 24. Streamlit + API Calls
**Uber Scenario:** "How would you show API data in a Streamlit dashboard?"
```python
import requests
import pandas as pd
import streamlit as st
try:
    response = requests.get(
        "https://api.example.com/transactions",
        timeout=10
    )
    response.raise_for_status()
    df = pd.DataFrame(response.json())
    st.dataframe(df)
except requests.RequestException:
    st.error("Unable to retrieve transaction data")
```
**Important:** This is an illustrative endpoint. Actual APIs may require authentication, pagination, and nested JSON normalization.
## 25. Streamlit vs Django/Flask
| Feature | Streamlit | Django/Flask |
|---|---|---|
| Primary purpose | Interactive Python data apps | General web applications and APIs |
| UI development | Built-in widgets | Templates or separate frontend |
| Data dashboards | Very convenient | Requires additional implementation |
| Complex backend services | Not primary focus | More suitable |
| Authentication/business workflows | Requires appropriate integration/design | More flexible architecture |
**Interview Answer:** "Streamlit is useful for quickly building data tools and dashboards. Django or Flask is more suitable when building complex backend services and custom web applications."
## 26. COMPLETE PRACTICAL PROJECT — EXCEL/CSV DATA PROCESSING DASHBOARD
**Uber Scenario:** "Build a simple Streamlit application where a user uploads an Excel/CSV file, validates data, removes invalid records, identifies duplicate primary keys, calculates fees, displays a summary, and downloads the processed file."
**File:** `app.py`
```python
import logging
import numpy as np
import pandas as pd
import streamlit as st

logging.basicConfig(level=logging.INFO)

st.title("Transaction Data Processing Tool")
st.write("Upload CSV or Excel data for validation and transformation.")

uploaded_file = st.file_uploader(
    "Upload transaction file",
    type=["csv", "xlsx"]
)

def process_data(df):
    required = {"TransactionID", "Amount"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    df = df.copy()
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    invalid = df["TransactionID"].isna() | df["Amount"].isna()
    invalid |= ~np.isfinite(df["Amount"].to_numpy(dtype=float))
    duplicate = df["TransactionID"].duplicated(keep=False)

    rejected_mask = invalid | duplicate
    rejected = df.loc[rejected_mask].copy()
    valid = df.loc[~rejected_mask].copy()

    valid["Fee"] = np.where(
        valid["Amount"] >= 1000,
        valid["Amount"] * 0.02,
        valid["Amount"] * 0.01
    )
    return valid, rejected

if uploaded_file is not None:
    try:
        if uploaded_file.name.lower().endswith(".csv"):
            raw_df = pd.read_csv(uploaded_file)
        else:
            raw_df = pd.read_excel(uploaded_file)

        st.subheader("Input Preview")
        st.dataframe(raw_df.head(20))

        if st.button("Process Data"):
            valid_df, rejected_df = process_data(raw_df)

            st.metric("Total Records", len(raw_df))
            st.metric("Valid Records", len(valid_df))
            st.metric("Rejected Records", len(rejected_df))

            st.subheader("Processed Data")
            st.dataframe(valid_df.head(100))

            st.subheader("Rejected Records")
            st.dataframe(rejected_df.head(100))

            st.download_button(
                "Download Processed CSV",
                valid_df.to_csv(index=False).encode("utf-8"),
                "processed_transactions.csv",
                "text/csv"
            )
            st.success("Processing completed successfully")

    except (ValueError, OSError, pd.errors.ParserError):
        logging.exception("Data processing failed")
        st.error("Processing failed. Check the file format and required columns.")
```
**Run:**
```bash
streamlit run app.py
```
**Workflow:** Upload → Read → Validate Required Columns → Convert Data Types → Identify Nulls/Duplicates → Separate Valid/Rejected → Calculate Fees → Display Metrics → Download.
**Interview Explanation:** "I would create a Streamlit UI for file upload and reporting, while keeping the ETL logic in reusable Python functions. Pandas would handle validation and cleaning, NumPy would perform vectorized fee calculations, and Streamlit would display results and enable downloads."
**Limitations:** This is a simple interview demo. It loads the uploaded file into memory and is not intended as a production solution for very large files. Production use would need file-size controls, stronger key validation, monitoring, security, and a scalable processing strategy.
## 27. TOP 15 STREAMLIT INTERVIEW QUESTIONS
| Question | Short Answer |
|---|---|
| 1. What is Streamlit? | Python framework for interactive data applications |
| 2. How do you install Streamlit? | `pip install streamlit` |
| 3. How do you run an app? | `streamlit run app.py` |
| 4. How do you upload files? | `st.file_uploader()` |
| 5. How do you display DataFrames? | `st.dataframe()` |
| 6. How do you add filters? | `st.selectbox()`, `st.multiselect()` |
| 7. How do you trigger processing? | `st.button()` |
| 8. How do you show KPIs? | `st.metric()` |
| 9. How do you display charts? | `st.bar_chart()`, `st.line_chart()` |
| 10. How do you download results? | `st.download_button()` |
| 11. How do you handle errors? | Python try/except + `st.error()` + logging |
| 12. How do you preserve values across reruns? | `st.session_state` |
| 13. How do you avoid repeated expensive processing? | `st.cache_data` |
| 14. How do you handle large datasets? | Chunking, staging, background processing, summary previews |
| 15. Streamlit vs Pandas? | Streamlit provides UI; Pandas transforms data |
## 28. FINAL UBER INTERVIEW SCENARIOS
| Priority | Scenario | Expected Answer |
|---|---|---|
| 🔴 1 | Upload Excel and clean data | `st.file_uploader()` + Pandas validation/transformation |
| 🔴 2 | Show missing/duplicate records | Pandas checks + `st.metric()` + `st.dataframe()` |
| 🔴 3 | Download processed output | `st.download_button()` |
| 🔴 4 | Handle an exception | try/except + logging + `st.error()` |
| 🔴 5 | Process 1M+ records | Chunking, staging, backend processing, limited preview |
| 🟠 6 | Build an interactive dashboard | Selectbox + DataFrame + metrics + charts |
| 🟠 7 | Avoid reprocessing data | Caching or session state, where appropriate |
| 🟠 8 | Connect to Oracle | Database connector → SQL → Pandas → Streamlit |
| 🟠 9 | Read Parquet files | `pd.read_parquet()` → Streamlit preview |
| 🟠 10 | Build reusable automation | Separate ETL functions from Streamlit UI |
## 29. FINAL REVISION CHECKLIST
- [ ] Explain Streamlit in 30 seconds.
- [ ] Know `streamlit run app.py`.
- [ ] Know `st.file_uploader()`.
- [ ] Know `st.dataframe()`.
- [ ] Know `st.button()` and `st.selectbox()`.
- [ ] Know `st.metric()` and basic charts.
- [ ] Know `st.download_button()`.
- [ ] Explain Pandas + Streamlit integration.
- [ ] Explain Excel/CSV upload and transformation.
- [ ] Explain null and duplicate validation.
- [ ] Explain exceptions, logging, and operational alerts.
- [ ] Explain session state and caching.
- [ ] Explain how to handle 1M+ rows.
- [ ] Understand the complete sample application.
## 30. ONE-MINUTE INTERVIEW ANSWER
"Streamlit is a Python framework for creating interactive data-processing applications and dashboards. For example, I could build an internal tool where a user uploads an Excel or CSV file, Pandas validates and transforms the data, NumPy performs numerical calculations, and Streamlit displays summary metrics, rejected records, and a downloadable report. I would keep the transformation logic separate from the UI so it remains reusable and testable. For large files, I would use chunking or backend processing rather than loading everything into the Streamlit interface. For failures, I would use Python logging and exception handling, display user-friendly errors, and integrate operational alerts when required."
**HONEST EXPERIENCE ANSWER:** "I haven't worked with Streamlit professionally yet. My experience is primarily in Python backend development and data-processing workflows, but I understand Streamlit's core concepts and how it integrates with Pandas. I'm comfortable building a basic file-processing dashboard with it."
**FINAL PREPARATION ADVICE:** Do not spend hours memorizing Streamlit widgets. Understand the complete Excel/CSV processing example and be able to explain upload → validation → transformation → display → download → exception handling.