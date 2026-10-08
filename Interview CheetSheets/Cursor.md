# CURSOR / AI-ASSISTED DEVELOPMENT — UBER INTERVIEW CHEATSHEET

**Role:** Python Automation / Data Transformation Engineer
**Focus:** Cursor AI, AI-assisted coding, refactoring, debugging, code understanding, test generation, code review, security, and practical Python/Pandas/ETL scenarios.
**Interview Goal:** Explain how AI coding assistants improve development productivity while maintaining code correctness, security, performance, and maintainability.

# PART 1 — EASY: CURSOR AND AI FUNDAMENTALS

## 1. What is Cursor?

Cursor is an AI-powered code editor built around a VS Code-like development environment. It provides AI-assisted code generation, editing, debugging, explanation, and codebase exploration.
**Interview Answer:** "Cursor is an AI-assisted code editor that helps developers understand existing code, generate implementations, refactor functions, debug issues, and write tests. I treat AI-generated code as a starting point and validate it before using it."

## 2. Cursor vs VS Code vs GitHub Copilot

| Tool                                                                                                        | Main Purpose                | Typical Use                                                     |
| ----------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------- |
| Cursor                                                                                                      | AI-first code editor        | Codebase understanding, multi-file edits, debugging, generation |
| VS Code                                                                                                     | General-purpose code editor | Development, debugging, extensions, Git integration             |
| GitHub Copilot                                                                                              | AI coding assistant         | Code suggestions, chat, explanations, and assisted edits        |
| **Important:** Features overlap and evolve. The distinction is mainly their product design and integration. |                             |                                                                 |

## 3. What Can Cursor Do?

| Capability                                                                                                                | Example                                          |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Generate code                                                                                                             | Create a Python CSV validation function          |
| Explain code                                                                                                              | Explain an unfamiliar ETL module                 |
| Refactor code                                                                                                             | Break a 300-line function into smaller functions |
| Debug code                                                                                                                | Investigate a Pandas `KeyError`                  |
| Generate tests                                                                                                            | Create pytest cases for data transformations     |
| Improve performance                                                                                                       | Suggest vectorized Pandas operations             |
| Write documentation                                                                                                       | Generate docstrings and README content           |
| Review code                                                                                                               | Identify potential bugs and edge cases           |
| Understand dependencies                                                                                                   | Trace where a function is called                 |
| Assist with SQL                                                                                                           | Suggest queries and explain joins                |
| **Interview Point:** AI helps accelerate development, but the developer remains responsible for the final implementation. |                                                  |

## 4. How AI Coding Assistants Work — High Level

**Basic Flow:**
`Developer Request → Context (code/files/instructions) → AI Model → Suggested Changes → Developer Review → Tests → Commit`
**Explanation:**

1. Developer describes the task.
2. The assistant receives relevant code context.
3. The model generates a suggestion.
4. Developer reviews the proposed changes.
5. Developer runs tests and verifies results.
6. Approved changes are committed through Git.
   **Interview Answer:** "AI coding tools use the developer's instructions and relevant project context to suggest code. I review the changes, test them, and verify they meet the business requirement before committing."

## 5. What Is Prompt Engineering for Coding?

Prompt engineering means writing clear instructions that help an AI assistant produce useful, relevant results.
**Weak Prompt:** "Fix this code."
**Better Prompt:** "This Pandas function fails with a KeyError when the Amount column is missing. Explain the root cause and propose a fix that validates required columns before transformation. Preserve existing behavior for valid files and add pytest tests."
**Best Practice:** Specify the problem, context, constraints, expected output, and acceptance criteria.

## 6. Anatomy of a Good Coding Prompt

**Formula:**
`Task + Context + Constraints + Expected Behavior + Edge Cases + Tests`
**Example:**

```text
Task: Create a Python function to process transaction CSV files.
Context: Files contain TransactionID, TradeDate, Amount, Currency.
Constraints:
- Use Pandas.
- Do not silently drop invalid records.
- Handle missing columns and invalid amounts.
Expected behavior:
- Return cleaned data and rejected records separately.
Edge cases:
- Empty file, duplicate IDs, null amounts, invalid dates.
Tests:
- Generate pytest tests for each edge case.
```

**Interview Answer:** "I provide the business requirement, input schema, expected output, edge cases, and constraints so the assistant generates code that is easier to verify."

# PART 2 — MEDIUM: PRACTICAL CURSOR WORKFLOWS

## 7. AI-Assisted Code Generation

**Scenario:** Generate a Python function to clean transaction data.
**Prompt:**

```text
Write a Pandas function that:
1. Accepts a DataFrame with TransactionID, Amount, and TradeDate.
2. Validates required columns.
3. Converts Amount to numeric.
4. Converts TradeDate to datetime.
5. Separates invalid rows from valid rows.
6. Returns both DataFrames.
7. Includes type hints and pytest tests.
```

**Illustrative Implementation:**

```python
import pandas as pd

def clean_transactions(df: pd.DataFrame):
    required = {"TransactionID", "Amount", "TradeDate"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    result = df.copy()
    result["Amount"] = pd.to_numeric(result["Amount"], errors="coerce")
    result["TradeDate"] = pd.to_datetime(
        result["TradeDate"], errors="coerce"
    )

    invalid_mask = (
        result["TransactionID"].isna()
        | result["Amount"].isna()
        | result["TradeDate"].isna()
    )

    valid = result.loc[~invalid_mask].copy()
    rejected = result.loc[invalid_mask].copy()
    return valid, rejected
```

**What You Must Verify:**

* Are required columns validated?
* Are invalid values handled correctly?
* Are rejected records preserved?
* Are duplicates allowed or rejected?
* Are business rules for negative amounts defined?
* Are date formats and time zones handled correctly?
  **Interview Answer:** "I use AI to generate an initial implementation, then check schema validation, business rules, edge cases, and output correctness."

## 8. AI-Assisted Refactoring

**What Is Refactoring?** Improving internal code structure without intentionally changing its observable behavior.
**Scenario:** A single ETL function reads files, cleans data, performs joins, and writes output.
**Before:**

```python
def process_file(path):
    df = pd.read_csv(path)
    df = df.dropna(subset=["TransactionID"])
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
    df = df.dropna(subset=["Amount"])
    df.to_csv("output.csv", index=False)
```

**Cursor Prompt:**

```text
Refactor this ETL function into smaller functions:
read_data, validate_data, transform_data, and save_data.
Preserve existing behavior.
Add type hints and meaningful error handling.
Do not introduce new dependencies.
Provide unit tests.
```

**After:**

```python
import pandas as pd

def read_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna(subset=["TransactionID"]).copy()

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["Amount"] = pd.to_numeric(result["Amount"], errors="coerce")
    return result.dropna(subset=["Amount"])

def save_data(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)

def process_file(input_path: str, output_path: str) -> None:
    df = read_data(input_path)
    df = validate_data(df)
    df = transform_data(df)
    save_data(df, output_path)
```

**Benefits:**

* Easier unit testing.
* Better readability.
* Improved maintainability.
* Clear separation of responsibilities.
* Easier debugging.
  **Interview Answer:** "I use AI to suggest modular refactoring, but I compare the original and refactored behavior using tests to ensure the business logic remains unchanged."

## 9. AI-Assisted Debugging

**Scenario:** A Pandas ETL job fails with:

```text
KeyError: 'Amount'
```

**Possible Causes:**

* Missing column.
* Different capitalization.
* Leading/trailing spaces.
* Incorrect header row.
* Wrong input file.
  **Cursor Prompt:**

```text
This Pandas ETL script raises KeyError: 'Amount'.
Analyze the relevant code and input schema.
Identify possible root causes.
Suggest a minimal fix.
Add validation and a clear error message.
Do not silently invent missing financial values.
```

**Possible Fix:**

```python
df.columns = df.columns.str.strip()

required = {"TransactionID", "Amount"}
missing = required - set(df.columns)

if missing:
    raise ValueError(f"Required columns missing: {sorted(missing)}")
```

**Interview Answer:** "I provide the error trace and relevant code to the AI assistant, review its diagnosis, reproduce the issue, implement a minimal fix, and add a regression test."

## 10. Understanding an Existing Codebase

**Scenario:** You join a project containing unfamiliar Python ETL scripts.
**Cursor Prompt:**

```text
Explain this project's architecture.
Identify:
1. Entry points.
2. Input data sources.
3. Data validation functions.
4. Transformation functions.
5. Database/API integrations.
6. Output destinations.
7. Error handling and logging.
8. Existing tests.
Reference the relevant files and functions.
Do not assume behavior that is not visible in the code.
```

**Manual Verification:**

* Read the entry-point scripts.
* Trace function calls.
* Inspect configuration files.
* Review dependencies.
* Run tests.
* Confirm actual runtime behavior.
  **Interview Answer:** "I use AI to accelerate codebase understanding, then verify its explanation against actual source files, dependencies, and execution flow."

## 11. Generating Unit Tests with AI

**Scenario:** You wrote a function that removes duplicate transactions.
**Cursor Prompt:**

```text
Generate pytest tests for a transaction deduplication function.
Cover:
- No duplicates.
- Duplicate transaction IDs.
- Empty DataFrame.
- Missing TransactionID column.
- Null transaction IDs.
- Different records sharing the same ID.
Do not assume which duplicate should be retained.
Ask for the business rule if required.
```

**Example Tests:**

```python
import pandas as pd
import pytest

def remove_duplicates(df):
    if "TransactionID" not in df.columns:
        raise ValueError("Missing TransactionID")
    return df.drop_duplicates(subset=["TransactionID"], keep="first")

def test_no_duplicates():
    df = pd.DataFrame({"TransactionID": [1, 2, 3]})
    result = remove_duplicates(df)
    assert len(result) == 3

def test_duplicates():
    df = pd.DataFrame({"TransactionID": [1, 1, 2]})
    result = remove_duplicates(df)
    assert len(result) == 2

def test_missing_column():
    df = pd.DataFrame({"Amount": [100]})
    with pytest.raises(ValueError):
        remove_duplicates(df)
```

**Important:** The sample implements `keep="first"` only as an illustrative policy. A production rule must be confirmed before implementation.
**Interview Answer:** "AI helps me generate test cases quickly, but I independently verify the assertions and ensure the tests reflect actual business requirements."

## 12. AI-Assisted Code Review

**Cursor Prompt:**

```text
Review this Python ETL change for:
1. Correctness.
2. Missing-value handling.
3. Duplicate handling.
4. Data type conversion.
5. Performance.
6. Security.
7. Error handling.
8. Test coverage.
Report issues by severity and explain why they matter.
Do not modify the code yet.
```

**Review Checklist:**

| Area            | What to Check                              |
| --------------- | ------------------------------------------ |
| Correctness     | Does output match requirements?            |
| Data Quality    | Missing, invalid, duplicate records        |
| Security        | Credentials, sensitive data, unsafe inputs |
| Performance     | Loops, repeated joins, memory usage        |
| Maintainability | Readability, modularity, naming            |
| Reliability     | Error handling, retries, logging           |
| Testing         | Unit, integration, regression tests        |

# PART 3 — AI FOR PANDAS AND ETL OPTIMIZATION

## 13. AI-Assisted Pandas Performance Optimization

**Scenario:** A Pandas script processes millions of records slowly.
**Inefficient Code:**

```python
df["Tax"] = df["Amount"].apply(lambda x: x * 0.18)
```

**Optimized Code:**

```python
df["Tax"] = df["Amount"] * 0.18
```

**Why Better?** Vectorized operations generally avoid Python-level per-row function calls and can improve performance.
**Cursor Prompt:**

```text
Review this Pandas transformation for performance bottlenecks.
Suggest vectorized alternatives where appropriate.
Preserve null-handling and numerical behavior.
Explain memory implications.
Provide a benchmark approach and correctness tests.
```

**Interview Answer:** "I use AI to identify potential inefficiencies such as unnecessary row-wise operations, but I benchmark improvements and compare outputs before accepting changes."

## 14. AI-Assisted Memory Optimization

**Scenario:** A 5 GB CSV file causes an out-of-memory error.
**Cursor Prompt:**

```text
This Pandas ETL script runs out of memory while processing a 5 GB CSV.
Suggest a memory-efficient approach using:
- Chunked reading.
- Required columns only.
- Appropriate dtypes.
- Incremental output.
Explain any limitations for global operations such as deduplication and joins.
```

**Example:**

```python
import pandas as pd

for chunk in pd.read_csv(
    "transactions.csv",
    chunksize=100_000,
    usecols=["TransactionID", "Amount"],
):
    chunk["Amount"] = pd.to_numeric(chunk["Amount"], errors="coerce")
    chunk = chunk.dropna(subset=["Amount"])
    # Write validated chunks incrementally to the chosen destination.
```

**Important:** Chunk processing requires additional design for global deduplication, sorting, and aggregation.
**Interview Answer:** "I may use AI to propose chunking and dtype optimizations, but I validate that the new approach preserves global business rules and does not introduce duplicate or aggregation errors."

## 15. AI-Assisted SQL Generation

**Scenario:** Generate a query to find duplicate transaction IDs.
**Prompt:**

```text
Write an SQL query to find TransactionID values appearing more than once.
Return TransactionID and duplicate count.
Explain the query and provide an example.
```

**SQL:**

```sql
SELECT TransactionID, COUNT(*) AS duplicate_count
FROM transactions
GROUP BY TransactionID
HAVING COUNT(*) > 1;
```

**Verification:**

* Check table and column names.
* Confirm SQL dialect.
* Validate null handling.
* Check expected output.
* Inspect performance for large tables.
  **Interview Answer:** "I can use AI to draft SQL queries, but I validate the syntax, business logic, database dialect, and execution plan when performance matters."

## 16. AI-Assisted API Integration

**Scenario:** Fetch paginated API data and convert it to a DataFrame.
**Cursor Prompt:**

```text
Write a Python requests-based API client that:
1. Uses bearer-token authentication.
2. Handles pagination.
3. Sets request timeouts.
4. Handles rate limits and transient failures.
5. Avoids exposing credentials in logs.
6. Converts validated JSON records into a Pandas DataFrame.
Use the provided API documentation; do not invent response fields.
```

**Important:** Pagination, authentication, and retry behavior depend on the actual API contract.
**Interview Answer:** "AI can accelerate API client development, but I verify the API documentation, authentication requirements, response schema, pagination rules, and error handling."

# PART 4 — HARD: VERIFYING AI-GENERATED CODE

## 17. Why Should We Not Blindly Trust AI Code?

AI-generated code may:

* Contain logical bugs.
* Misinterpret requirements.
* Invent nonexistent functions or API fields.
* Introduce security vulnerabilities.
* Handle edge cases incorrectly.
* Produce inefficient algorithms.
* Use outdated libraries.
* Silently change business logic.
  **Interview Answer:** "AI-generated code is not automatically correct. I treat it as an unverified suggestion and validate it through code review, tests, documentation, and real input/output comparisons."

## 18. How Do You Verify AI-Generated Code?

**Recommended Workflow:**
`Understand Requirement → Generate Suggestion → Review Diff → Validate Logic → Run Tests → Check Security → Benchmark if Needed → PR Review`
**Verification Checklist:**

| Step                                                                                                                                                                                                                                                           | Verification                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| 1. Requirements                                                                                                                                                                                                                                                | Does it solve the actual problem?              |
| 2. Code Review                                                                                                                                                                                                                                                 | Are there logic errors?                        |
| 3. Dependencies                                                                                                                                                                                                                                                | Are libraries and APIs real and supported?     |
| 4. Unit Tests                                                                                                                                                                                                                                                  | Do individual functions work?                  |
| 5. Integration Tests                                                                                                                                                                                                                                           | Does the full workflow work?                   |
| 6. Edge Cases                                                                                                                                                                                                                                                  | Nulls, duplicates, empty inputs, invalid types |
| 7. Data Reconciliation                                                                                                                                                                                                                                         | Do counts and totals match expectations?       |
| 8. Security                                                                                                                                                                                                                                                    | No secrets or unauthorized data exposure       |
| 9. Performance                                                                                                                                                                                                                                                 | Memory and execution time acceptable           |
| 10. Git Review                                                                                                                                                                                                                                                 | Is the final diff focused and understandable?  |
| **Interview Answer:** "I verify AI-generated code by reviewing the diff, checking business rules, running unit and integration tests, validating edge cases, and comparing data counts and totals. I also check security and performance before raising a PR." |                                                |

## 19. How to Verify AI-Generated ETL Code

**Scenario:** AI generates code that cleans 100,000 transactions.
**Validation Metrics:**

```text
Input rows:       100,000
Valid rows:        96,000
Rejected rows:      4,000
Expected total:   100,000
```

**Core Assertion:**

```python
assert len(valid_df) + len(rejected_df) == len(input_df)
```

**Additional Checks:**

```python
assert valid_df["TransactionID"].notna().all()
assert valid_df["Amount"].notna().all()
```

**Important:** These checks are useful only when the pipeline partitions input rows without expansion or intentional deletion. Joins and aggregations require different reconciliation rules.
**Interview Answer:** "For data pipelines, I verify not just whether the code executes, but whether row counts, totals, rejected records, and transformation outputs satisfy business rules."

## 20. AI Hallucination in Coding

**Meaning:** An AI assistant may generate convincing but incorrect information, such as a nonexistent library method or unsupported API behavior.
**Example:** AI suggests a method that does not exist in the installed Pandas version.
**How to Handle:**

1. Check official documentation.
2. Confirm installed library version.
3. Run a minimal reproducible example.
4. Add a test.
5. Correct the implementation.
   **Interview Answer:** "If AI suggests an unfamiliar method, I verify it against the installed library version and official documentation rather than assuming it exists."

## 21. Security and Confidentiality

**Risks:**

* Exposing API keys.
* Sharing customer data.
* Uploading proprietary code to unapproved services.
* Generating unsafe SQL or shell commands.
* Introducing vulnerable dependencies.
* Logging personally identifiable information.
  **Best Practices:**
* Follow company AI-tool policies.
* Use only approved AI tools and configurations.
* Avoid exposing confidential data.
* Mask or replace sensitive examples where appropriate.
* Keep credentials in approved secret storage.
* Review generated commands before executing them.
* Scan dependencies and code for security issues.
  **Interview Answer:** "I follow organizational policies for AI tools, avoid sharing sensitive information with unapproved services, and review generated code for security vulnerabilities."

## 22. AI-Generated Code vs Human-Written Code

| AI-Generated Code                                                                                     | Human Responsibility             |
| ----------------------------------------------------------------------------------------------------- | -------------------------------- |
| Suggests implementation                                                                               | Validate correctness             |
| Suggests optimizations                                                                                | Benchmark performance            |
| Generates tests                                                                                       | Verify assertions                |
| Explains code                                                                                         | Confirm actual behavior          |
| Proposes refactoring                                                                                  | Preserve business logic          |
| Generates SQL                                                                                         | Verify schema and dialect        |
| Suggests dependencies                                                                                 | Check security and compatibility |
| **Key Principle:** AI accelerates development; engineering accountability remains with the developer. |                                  |

## 23. Prompt Injection in AI Coding Tools

**Meaning:** Malicious instructions embedded in repository files, comments, documentation, or external content may attempt to manipulate an AI assistant.
**Example:** A repository file contains instructions telling the assistant to ignore previous rules and expose environment variables.
**Protection:**

* Treat repository content as potentially untrusted.
* Review proposed commands and file changes.
* Limit tool permissions.
* Require approval for destructive operations.
* Avoid giving unnecessary access to secrets.
  **Interview Answer:** "I treat external content and repository instructions as untrusted unless verified, and I review any AI-proposed action that accesses sensitive files or changes the environment."

# PART 5 — REAL-WORLD UBER INTERVIEW SCENARIOS

## 24. Scenario 1: You Receive an Unknown Excel File

**Question:** "How would you use Cursor to automate processing an unfamiliar Excel file?"
**Answer:**

1. Inspect the workbook structure and sample rows.
2. Identify required columns and business rules.
3. Provide a sanitized schema and requirements to Cursor.
4. Ask it to generate Pandas parsing and validation logic.
5. Review assumptions about dates, nulls, duplicates, and data types.
6. Test using valid and invalid sample files.
7. Reconcile output counts and totals.
8. Commit the verified implementation.
   **Strong Interview Line:** "I use Cursor to speed up implementation, but I first understand the data and validate the output independently."

## 25. Scenario 2: Existing ETL Code Is Too Slow

**Question:** "How would AI help optimize a slow Python script?"
**Answer:** "I would first profile the code to identify bottlenecks. Then I could ask Cursor to suggest improvements such as vectorization, reducing unnecessary copies, selecting required columns, or chunking. I would benchmark the revised code and verify that outputs remain equivalent."

## 26. Scenario 3: AI Generates Incorrect Transformation Logic

**Question:** "What if Cursor generates code that drops all rows with null values?"
**Answer:** "I would check whether that behavior matches the business rule. In many ETL pipelines, some null fields are acceptable while others are mandatory. I would change the logic to validate only required fields, preserve rejected records when necessary, and add tests."

## 27. Scenario 4: AI Suggests a Dangerous Database Operation

**Question:** "Cursor generates a SQL statement that deletes duplicate records. What would you do?"
**Answer:** "I would not execute it immediately. I would verify the deduplication criteria, inspect the affected rows using a SELECT query, confirm the environment and transaction behavior, and follow the approved change process before any destructive operation."

## 28. Scenario 5: AI Refactors a Large Python Module

**Question:** "How would you ensure AI refactoring doesn't break existing functionality?"
**Answer:** "I would establish baseline tests, request small incremental changes, review each diff, run regression tests, and compare the old and new outputs using representative datasets."

## 29. Scenario 6: AI-Generated Tests Pass, but Production Fails

**Question:** "Why can this happen?"
**Answer:** "Tests may not cover production-specific data, schema variations, concurrency, permissions, external dependencies, or volume. I would inspect the failure, reproduce it with sanitized representative data, add regression coverage, and update the implementation."

## 30. Scenario 7: AI Suggests Using `apply()` for Every Pandas Transformation

**Question:** "Would you accept it?"
**Answer:** "Not automatically. I would check whether a vectorized operation is clearer or faster, especially for large datasets. I would compare correctness and benchmark performance."

## 31. Scenario 8: You Need to Understand a Large Legacy Python Project

**Question:** "How can Cursor help?"
**Answer:** "I can ask Cursor to summarize the architecture, trace function calls, identify input/output flows, and explain unfamiliar modules. Then I validate those explanations by reading the source code and running the project."

## 32. Scenario 9: AI Suggests Installing a New Dependency

**Question:** "What checks would you perform?"
**Answer:** "I would verify the package is legitimate, actively maintained, compatible with our Python version, approved by the organization, and free from known unacceptable vulnerabilities. I would also check whether an existing dependency already solves the problem."

## 33. Scenario 10: How Would You Use Cursor in Daily Development?

**Answer:** "I would use Cursor to understand unfamiliar code, generate boilerplate, draft tests, debug exceptions, suggest refactoring, and identify potential optimizations. I would still review all changes, run tests, and use Git pull requests for collaboration."

# PART 6 — INTERVIEW QUESTIONS AND ANSWERS

## 34. Top 25 Cursor/AI Interview Questions

| Question                                       | Interview Answer                                                                                               |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| 1. What is Cursor?                             | An AI-powered code editor for code generation, explanation, editing, and debugging.                            |
| 2. How is Cursor different from VS Code?       | Cursor emphasizes integrated AI-assisted development; both support standard coding workflows.                  |
| 3. What is AI-assisted coding?                 | Using AI to suggest or modify code under developer supervision.                                                |
| 4. How do you use AI to generate code?         | Provide requirements, context, constraints, and tests.                                                         |
| 5. How do you debug with AI?                   | Provide error trace, relevant code, and expected behavior; verify the diagnosis.                               |
| 6. How do you refactor with AI?                | Request focused structural improvements and run regression tests.                                              |
| 7. Can AI replace developers?                  | AI assists development, but developers remain responsible for requirements, design, validation, and decisions. |
| 8. What is prompt engineering?                 | Writing clear instructions to guide AI output.                                                                 |
| 9. What makes a good coding prompt?            | Task, context, constraints, edge cases, expected behavior, and tests.                                          |
| 10. How do you verify AI-generated code?       | Review, test, validate business rules, check security and performance.                                         |
| 11. What is AI hallucination?                  | Plausible but incorrect generated information or code.                                                         |
| 12. How do you handle hallucinations?          | Verify documentation, reproduce behavior, and test.                                                            |
| 13. How can AI improve code quality?           | Suggest tests, refactoring, documentation, and potential issues.                                               |
| 14. How can AI help with Pandas?               | Suggest transformations, debugging, and optimization approaches.                                               |
| 15. How can AI help with ETL?                  | Draft parsing, validation, transformation, and test code.                                                      |
| 16. How can AI help with SQL?                  | Generate and explain queries that must be validated.                                                           |
| 17. How can AI help with APIs?                 | Draft clients, parsing logic, retries, and tests based on documentation.                                       |
| 18. How do you protect sensitive data?         | Use approved tools, restrict access, and avoid exposing secrets or customer data.                              |
| 19. What if AI code passes tests but is wrong? | Revisit requirements and improve test coverage using real edge cases.                                          |
| 20. How do you measure AI productivity?        | Compare development time, defect rate, review effort, and delivered quality.                                   |
| 21. How do you review AI-generated code?       | Inspect diffs, logic, edge cases, dependencies, and tests.                                                     |
| 22. How do you optimize AI-generated code?     | Profile, benchmark, and verify equivalent outputs.                                                             |
| 23. What are AI coding limitations?            | Incorrect assumptions, hallucinations, security risks, and missing context.                                    |
| 24. Can AI generate unit tests?                | Yes, but assertions and coverage require human verification.                                                   |
| 25. Would you blindly accept Cursor changes?   | No. Every change must satisfy requirements and pass appropriate validation.                                    |

# PART 7 — PROMPTS TO REMEMBER

## 35. Code Generation Prompt

```text
Generate a Python implementation for [requirement].
Use [libraries].
Input schema: [columns/types].
Expected output: [format].
Handle nulls, duplicates, invalid data, and empty input.
Add type hints and tests.
Do not invent unspecified business rules.
```

## 36. Debugging Prompt

```text
Analyze this error: [stack trace].
Relevant code: [code].
Expected behavior: [expected].
Actual behavior: [actual].
Identify the likely root cause.
Suggest the smallest safe fix.
Add a regression test.
```

## 37. Refactoring Prompt

```text
Refactor this Python module for readability and maintainability.
Preserve existing behavior and public interfaces.
Avoid unnecessary dependencies.
Split responsibilities where appropriate.
Show the changes and explain them.
Add regression tests.
```

## 38. Optimization Prompt

```text
Analyze this Pandas pipeline for performance and memory issues.
Identify likely bottlenecks.
Suggest measurable optimizations.
Preserve output correctness and business rules.
Provide benchmarks and correctness checks.
```

## 39. Code Review Prompt

```text
Review this code for correctness, security, performance,
maintainability, and edge cases.
Identify concrete issues with explanations.
Do not make changes until the issues are reviewed.
```

## 40. Codebase Understanding Prompt

```text
Explain the architecture of this Python project.
Identify entry points, modules, dependencies,
data sources, transformation steps, outputs,
error handling, and tests.
Reference actual files/functions.
Flag anything that cannot be verified.
```

# PART 8 — AI-ASSISTED DEVELOPMENT WORKFLOW

## 41. Recommended End-to-End Workflow

**Step 1 — Understand:** Read the requirement and identify business rules.
**Step 2 — Inspect:** Explore existing code, tests, and schemas.
**Step 3 — Prompt:** Give Cursor a specific task with constraints.
**Step 4 — Generate:** Review the suggested implementation.
**Step 5 — Validate:** Check logic, security, and dependencies.
**Step 6 — Test:** Run unit, integration, and edge-case tests.
**Step 7 — Benchmark:** Measure performance if relevant.
**Step 8 — Review:** Inspect Git diff and create a PR.
**Step 9 — Integrate:** Merge after approvals and CI checks.
**Step 10 — Monitor:** Verify behavior after deployment.
**Flow:**
`Requirement → Cursor Assistance → Developer Review → Testing → Git PR → CI/CD → Deployment → Monitoring`

# PART 9 — UBER-SPECIFIC INTERVIEW ANSWERS

## 42. "How Would You Use Cursor for Data Transformation?"

**Answer:** "I would first understand the input format, expected output, and transformation rules. Then I could use Cursor to generate Pandas code for cleaning, validation, joins, and aggregation. I would review the implementation, test nulls and duplicates, and reconcile row counts and totals before using the output."

## 43. "How Would You Use AI to Improve an Existing ETL Pipeline?"

**Answer:** "I would identify the current bottlenecks or maintainability issues, then ask AI for focused suggestions such as modularizing functions, vectorizing Pandas operations, improving validation, or reducing memory usage. I would verify correctness using baseline outputs and measure performance before accepting changes."

## 44. "How Would You Validate AI-Generated Python Code?"

**Answer:** "I would review the code against the requirements, verify libraries and APIs, test normal and edge cases, check security, and compare actual outputs with expected results. For ETL code, I would also verify row counts, totals, and rejected records."

## 45. "What Are the Risks of Using AI Coding Assistants?"

**Answer:** "The main risks are incorrect business logic, hallucinated APIs, insecure code, performance problems, and exposing confidential information. I reduce these risks by using approved tools, limiting sensitive context, reviewing changes, and running tests."

## 46. "How Would You Explain Your AI Development Workflow?"

**Answer:** "I use AI as a development assistant rather than a replacement for engineering judgment. I provide clear requirements, review suggested changes, run tests, verify business logic, and integrate approved changes through Git and CI/CD."

## 47. If You Have Not Used Cursor Professionally

**Interview-Safe Answer:**
"I understand Cursor's core capabilities, including code generation, debugging, refactoring, and codebase exploration. My approach would be to use it for focused development tasks while reviewing every change and validating it through tests. I am comfortable adopting AI-assisted development tools within the team's approved workflow."
**Important:** Do not claim professional Cursor experience unless you actually have it.

# PART 10 — FINAL REVISION

## 48. Priority Checklist

| Topic                                | Priority     |
| ------------------------------------ | ------------ |
| What Cursor is                       | 🔴 Must Know |
| Cursor vs VS Code/Copilot            | 🟠 Important |
| AI-assisted code generation          | 🔴 Must Know |
| AI-assisted debugging                | 🔴 Must Know |
| AI-assisted refactoring              | 🔴 Must Know |
| Understanding existing code          | 🔴 Must Know |
| Writing effective prompts            | 🔴 Must Know |
| Verifying AI-generated code          | 🔴 Must Know |
| Generating and validating tests      | 🔴 Must Know |
| AI for Pandas/ETL                    | 🔴 Must Know |
| AI hallucinations                    | 🔴 Must Know |
| Security and confidentiality         | 🔴 Must Know |
| AI-assisted performance optimization | 🟠 Important |
| Prompt injection awareness           | 🟠 Important |
| AI + Git + CI/CD workflow            | 🟠 Important |

## 49. One-Minute Interview Answer

"AI-assisted development tools such as Cursor can improve productivity by helping developers generate code, understand unfamiliar modules, debug errors, refactor functions, and write tests. For Python and Pandas projects, I would use them to accelerate data-cleaning, validation, and transformation tasks. However, I would never blindly accept generated code. I would review the implementation, verify business requirements, run unit and integration tests, check edge cases, and validate output counts and totals. I would also follow company security policies and integrate changes through Git pull requests and CI/CD checks."

## 50. Final Interview Rule

**The strongest answer is not "Cursor writes code for me."**
**The strongest answer is "Cursor accelerates my development, but I remain responsible for correctness, security, performance, and maintainability."**
