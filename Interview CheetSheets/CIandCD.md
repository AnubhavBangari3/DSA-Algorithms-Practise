# CI/CD — UBER INTERVIEW CHEATSHEET

**Role:** Python Automation / Data Transformation Engineer
**Experience Level:** 3–5 Years
**Focus:** CI/CD fundamentals, pipelines, GitHub Actions, automated testing, build and deployment workflows, Docker basics, environment variables, troubleshooting, and Python ETL automation.
**Interview Goal:** Explain how code changes move safely from development to testing and production through automated pipelines.

# PART 1 — EASY: CI/CD FUNDAMENTALS

## 1. What is CI/CD?

CI/CD stands for Continuous Integration and Continuous Delivery or Continuous Deployment.
**Continuous Integration (CI):** Developers frequently integrate code changes into a shared repository. Automated pipelines build, validate, and test these changes.
**Continuous Delivery (CD):** Code is automatically tested and prepared for release, but production deployment may require manual approval.
**Continuous Deployment (CD):** Every change that passes all required automated checks is deployed automatically to production.
**Interview Answer:** "CI/CD automates code integration, testing, and delivery. CI catches issues early, while CD ensures validated code can be released consistently and safely."

## 2. CI vs Continuous Delivery vs Continuous Deployment

| Concept                                                                                                                                                                                                 | Meaning                                        | Production Deployment    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------ |
| Continuous Integration                                                                                                                                                                                  | Automatically validate integrated code changes | Not necessarily included |
| Continuous Delivery                                                                                                                                                                                     | Keep software ready for release                | May require approval     |
| Continuous Deployment                                                                                                                                                                                   | Automatically release changes passing checks   | Automatic                |
| **Example:** A developer pushes a Python ETL change. CI runs linting and tests. The pipeline packages the application and deploys it to staging. After approval, the release is deployed to production. |                                                |                          |

## 3. Why Do Companies Use CI/CD?

* Reduce manual deployment errors.
* Detect bugs early.
* Standardize testing and release processes.
* Improve collaboration.
* Make deployments repeatable.
* Enable faster, safer releases.
* Maintain traceability of code changes.
  **Interview Answer:** "CI/CD improves software quality and release reliability by automatically validating code changes and standardizing the deployment process."

## 4. Typical CI/CD Pipeline

**Flow:**
`Developer → Git Commit → GitHub Push/PR → CI Trigger → Install Dependencies → Lint → Unit Tests → Build/Package → Integration Tests → Staging → Approval → Production → Monitoring`
**Important:** The exact stages depend on the application, infrastructure, and organization.

## 5. CI/CD Tools

| Tool                                                                                                                          | Purpose                              |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| GitHub Actions                                                                                                                | Automate repository workflows        |
| Jenkins                                                                                                                       | CI/CD automation server              |
| GitLab CI/CD                                                                                                                  | Pipelines integrated with GitLab     |
| Azure Pipelines                                                                                                               | Build, test, and deploy applications |
| Docker                                                                                                                        | Package applications into containers |
| Kubernetes                                                                                                                    | Deploy and orchestrate containers    |
| pytest                                                                                                                        | Python automated testing             |
| Ruff/Flake8                                                                                                                   | Python linting                       |
| Black                                                                                                                         | Python formatting                    |
| SonarQube                                                                                                                     | Static analysis and quality checks   |
| **Interview Note:** Understand GitHub Actions deeply enough to explain a simple workflow. Recognize other tools conceptually. |                                      |

## 6. CI/CD vs Git/GitHub

| Git/GitHub                                                                                                                                               | CI/CD                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| Tracks code changes                                                                                                                                      | Automates validation and delivery |
| Supports branches and PRs                                                                                                                                | Runs checks on branches and PRs   |
| Stores version history                                                                                                                                   | Builds/tests code versions        |
| Helps collaboration                                                                                                                                      | Helps release reliability         |
| **Interview Answer:** "Git manages version history and collaboration, while CI/CD automates testing, packaging, and deployment when code changes occur." |                                   |

## 7. What Triggers a Pipeline?

Common triggers:

* Push to a branch.
* Pull request creation or update.
* Merge into `main`.
* Scheduled execution.
* Manual execution.
* Release or tag creation.
  **GitHub Actions Examples:**

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:
```

**Interview Answer:** "Pipelines can be triggered by Git events, schedules, manual actions, or other supported events."

## 8. What Is a Build?

A build prepares application code into an executable or deployable form.
**Examples:**

| Application                                                              | Build/Packaging                                                                |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Python package                                                           | Build wheel or source distribution                                             |
| Django API                                                               | Install dependencies, validate configuration, collect static files when needed |
| React/Next.js                                                            | Compile and bundle frontend assets                                             |
| Docker application                                                       | Build container image                                                          |
| Python ETL script                                                        | Validate, test, and package script/dependencies for execution                  |
| **Important:** Python scripts do not always require a compilation stage. |                                                                                |

## 9. What Is a Deployment?

Deployment means delivering a validated application or artifact to an execution environment.
**Examples:**

* Deploy a Django API to a server or cloud platform.
* Deploy a Docker image to a container service.
* Publish a Python package.
* Deploy ETL scripts to a scheduled job environment.
* Update a serverless function.
  **Interview Answer:** "Deployment makes a validated version of an application or job available in the target environment."

# PART 2 — MEDIUM: CI PIPELINE AND AUTOMATED TESTING

## 10. Main CI Pipeline Stages

| Stage                                                                                                                                                             | Purpose                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Checkout                                                                                                                                                          | Retrieve repository code                |
| Setup                                                                                                                                                             | Configure Python/runtime                |
| Dependencies                                                                                                                                                      | Install required packages               |
| Lint                                                                                                                                                              | Check code quality                      |
| Format Check                                                                                                                                                      | Check formatting conventions            |
| Unit Tests                                                                                                                                                        | Validate individual functions           |
| Integration Tests                                                                                                                                                 | Validate component interactions         |
| Security Checks                                                                                                                                                   | Detect selected vulnerabilities/secrets |
| Build                                                                                                                                                             | Produce a deployable artifact           |
| Publish                                                                                                                                                           | Store validated artifact                |
| **Interview Answer:** "A typical CI pipeline checks out the code, installs dependencies, runs quality checks and automated tests, and produces a build artifact." |                                         |

## 11. What Is Automated Testing?

Automated testing uses scripts and tools to verify software behavior without manually repeating every test.
**Common Testing Levels:**

| Test        | Purpose                                  | Example                                 |
| ----------- | ---------------------------------------- | --------------------------------------- |
| Unit        | Test individual functions                | Validate a Pandas cleaning function     |
| Integration | Test component interactions              | ETL script reading from a test database |
| End-to-End  | Test complete workflow                   | Input file → transform → output         |
| Regression  | Ensure existing behavior remains correct | Existing trade validations still pass   |
| Smoke       | Check basic application functionality    | API health endpoint responds            |
| Performance | Evaluate speed and resource usage        | Process a large CSV within limits       |

## 12. Unit Testing with pytest

**Example Function:**

```python
def calculate_total(amounts):
    return sum(amounts)
```

**Test:**

```python
def test_calculate_total():
    assert calculate_total([100, 200, 300]) == 600

def test_empty_list():
    assert calculate_total([]) == 0
```

**Run Tests:**

```bash
python -m pytest
python -m pytest -v
```

**Interview Answer:** "I use automated tests to verify that code changes preserve expected behavior before they are merged or deployed."

## 13. Testing a Pandas ETL Transformation

**Function:**

```python
import pandas as pd

def clean_transactions(df):
    required = {"TransactionID", "Amount"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    result = df.copy()
    result["Amount"] = pd.to_numeric(result["Amount"], errors="coerce")
    return result.dropna(subset=["TransactionID", "Amount"])
```

**Test:**

```python
import pandas as pd
from pandas.testing import assert_frame_equal

def test_clean_transactions():
    source = pd.DataFrame({
        "TransactionID": [1, 2, None],
        "Amount": ["100", "invalid", "300"]
    })
    actual = clean_transactions(source)
    expected = pd.DataFrame({
        "TransactionID": [1.0],
        "Amount": [100.0]
    })
    assert_frame_equal(
        actual.reset_index(drop=True),
        expected,
        check_dtype=False
    )
```

**What CI Verifies:** The transformation still handles invalid amounts and missing transaction IDs according to the implemented rule.
**Production Note:** Silently dropping records may be inappropriate; rejection handling must follow the business requirement.

## 14. What Is Linting?

Linting identifies coding-style problems, suspicious patterns, and certain errors.
**Example Commands:**

```bash
pip install ruff
ruff check .
```

**Interview Answer:** "Linting catches code-quality issues before review or deployment."

## 15. What Is a Formatting Check?

Formatting tools enforce consistent code layout.
**Example:**

```bash
pip install black
black --check .
```

**Difference:**

| Linting                                                                    | Formatting                 |
| -------------------------------------------------------------------------- | -------------------------- |
| Detects code issues and rule violations                                    | Enforces consistent layout |
| Example: Ruff                                                              | Example: Black             |
| **Note:** Some tools, including Ruff, support both linting and formatting. |                            |

## 16. What Happens When a Test Fails?

**Flow:**
`Test Failure → CI Job Fails → Developer Checks Logs → Fix Code/Test → Push Commit → Pipeline Reruns`
**Interview Answer:** "If a CI test fails, I inspect the logs, reproduce the failure locally, identify the root cause, fix the issue, and rerun the pipeline. I would not bypass required checks without an approved exception."

## 17. What Is a Quality Gate?

A quality gate is a condition that must be satisfied before code can progress.
**Examples:**

* All required tests pass.
* Lint checks pass.
* Required code reviews completed.
* No unacceptable security findings.
* Coverage meets the team's threshold.
  **Interview Answer:** "Quality gates prevent changes from progressing when they fail defined engineering standards."

## 18. What Is Test Coverage?

Test coverage measures which parts of code were exercised by tests.
**Command:**

```bash
python -m pytest --cov=.
```

**Requires:** `pytest-cov`.
**Interview Answer:** "Coverage helps identify untested code, but high coverage alone does not guarantee correct behavior. Test quality and edge cases are equally important."

# PART 3 — GITHUB ACTIONS

## 19. What Is GitHub Actions?

GitHub Actions is GitHub's workflow automation platform. It can run tests, builds, security checks, and deployments in response to repository events.
**Interview Answer:** "GitHub Actions allows us to define automated workflows using YAML files stored in the repository."

## 20. GitHub Actions Architecture

**Hierarchy:**
`Workflow → Jobs → Steps → Actions/Commands`

| Component | Meaning                             |
| --------- | ----------------------------------- |
| Workflow  | Automated process defined in YAML   |
| Event     | Trigger such as push or PR          |
| Job       | Group of steps executed on a runner |
| Runner    | Machine/environment executing a job |
| Step      | Individual command or action        |
| Action    | Reusable automation component       |
| Artifact  | File/package produced by a workflow |

## 21. Where Are GitHub Actions Workflows Stored?

```text
project/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── src/
├── tests/
├── requirements.txt
└── README.md
```

**Path:** `.github/workflows/python-ci.yml`

## 22. Complete GitHub Actions CI Example for Python

```yaml
name: Python CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest ruff
      - name: Lint
        run: ruff check .
      - name: Run tests
        run: python -m pytest -v
```

**Prerequisites:** The repository must have `requirements.txt` and discoverable tests; linting rules must be compatible with the project.
**Security Note:** For production workflows, pin third-party actions to reviewed commit SHAs and use dependency version controls as appropriate.

## 23. Explain the YAML Line by Line

| YAML Element  | Explanation                        |
| ------------- | ---------------------------------- |
| `name`        | Workflow name                      |
| `on`          | Events that trigger workflow       |
| `permissions` | GitHub token permissions           |
| `jobs`        | Defines pipeline jobs              |
| `test`        | Job identifier                     |
| `runs-on`     | Runner operating system            |
| `steps`       | Commands/actions executed in order |
| `uses`        | Reusable action                    |
| `run`         | Shell command                      |
| `with`        | Inputs passed to an action         |

## 24. Multiple Jobs in GitHub Actions

```yaml
name: Multi Job CI
on: [push, pull_request]
permissions:
  contents: read
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install ruff
      - run: ruff check .
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt pytest
      - run: python -m pytest
```

**Important:** Independent jobs can run in parallel unless dependencies are declared.

## 25. Job Dependencies with `needs`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Run tests here"
  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: echo "Build after tests"
```

**Explanation:** The `build` job starts after the `test` job completes successfully by default.

## 26. What Is a Runner?

A runner is the execution environment where GitHub Actions jobs run.
**Types:**

* GitHub-hosted runner.
* Self-hosted runner.
  **Interview Answer:** "A runner is the machine that executes workflow jobs. GitHub-hosted runners are managed by GitHub, while self-hosted runners are managed by the organization."

## 27. What Are GitHub Actions Secrets?

Secrets are sensitive values stored for controlled use in workflows.
**Examples:**

* API tokens.
* Database credentials.
* Deployment credentials.
  **Example Reference:**

```yaml
env:
  API_TOKEN: ${{ secrets.API_TOKEN }}
```

**Best Practices:**

* Do not hardcode credentials in YAML.
* Limit access to secrets.
* Avoid printing secrets in logs.
* Prefer short-lived cloud credentials through OIDC where supported.
* Restrict deployment permissions.
  **Interview Answer:** "I store sensitive values using approved secret management and restrict access to deployment credentials."

## 28. Environment Variables in CI/CD

**Example:**

```yaml
env:
  APP_ENV: test
  LOG_LEVEL: INFO
```

**Difference:**

| Environment Variable   | Secret                              |
| ---------------------- | ----------------------------------- |
| General configuration  | Sensitive configuration             |
| Example: `LOG_LEVEL`   | Example: API token                  |
| May be visible in logs | Should be protected from disclosure |

## 29. What Is an Artifact?

An artifact is a file produced by a workflow.
**Examples:**

* Test reports.
* Coverage reports.
* Python wheels.
* Build packages.
* Deployment manifests.
  **Interview Answer:** "Artifacts allow pipeline jobs to preserve or share outputs such as test reports and deployable packages."

## 30. Caching vs Artifacts

| Cache                                                                                                      | Artifact                                |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Speeds up repeated workflow execution                                                                      | Stores workflow outputs                 |
| Example: pip dependency cache                                                                              | Example: test report                    |
| Reusable optimization                                                                                      | Output for inspection or downstream use |
| **Interview Answer:** "Caching improves pipeline performance, while artifacts preserve generated outputs." |                                         |

# PART 4 — CONTINUOUS DELIVERY AND DEPLOYMENT

## 31. Typical CD Workflow

**Flow:**
`CI Pass → Build Artifact → Publish Artifact → Deploy to Staging → Smoke Tests → Approval → Deploy to Production → Monitor`
**Interview Answer:** "After CI validates the code, the delivery pipeline packages a versioned artifact, deploys it to a test environment, runs checks, and releases it according to the organization's approval process."

## 32. Development, Staging, and Production

| Environment                                                                                                          | Purpose                            |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Development                                                                                                          | Developer testing and iteration    |
| Testing/QA                                                                                                           | Functional and integration testing |
| Staging                                                                                                              | Preproduction validation           |
| Production                                                                                                           | Live workloads                     |
| **Best Practice:** Keep environments consistent where practical while separating credentials, data, and permissions. |                                    |

## 33. Deployment Strategies

| Strategy                                                                                                                                                                 | Explanation                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| Rolling                                                                                                                                                                  | Replace instances gradually                 |
| Blue-Green                                                                                                                                                               | Switch traffic between two environments     |
| Canary                                                                                                                                                                   | Release to a small portion of traffic first |
| Recreate                                                                                                                                                                 | Stop old version and start new version      |
| **Interview Answer:** "Deployment strategies help control release risk. For example, canary deployments expose a new version to limited traffic before broader rollout." |                                             |

## 34. What Is Rollback?

Rollback means restoring a previously known-good version or state after a problematic release.
**Example:** A new ETL deployment produces incorrect transaction totals. The team stops the affected job and restores the approved previous version.
**Important:** Rolling back code does not automatically undo incorrect database writes or generated outputs.
**Interview Answer:** "I would stop further impact, follow the approved rollback procedure, validate the restored version, and reconcile any data affected by the failed deployment."

## 35. What Is a Deployment Approval?

An approval is a control requiring authorized review before a release proceeds.
**Example:** Production deployment requires approval from an authorized engineer.
**Interview Answer:** "Approval gates add control to production releases, especially for systems where failures can affect customers or business-critical data."

## 36. CI/CD for Docker Applications

**Flow:**
`Code → Tests → Docker Build → Image Scan → Registry → Deployment → Health Checks`
**Example Dockerfile for a Python Job:**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "etl.py"]
```

**Build:**

```bash
docker build -t python-etl:1.0 .
```

**Run:**

```bash
docker run --rm python-etl:1.0
```

**Note:** The example assumes `etl.py` and its required dependencies are present. Production images should follow organizational hardening and image-pinning practices.

## 37. Why Use Docker in CI/CD?

* Consistent runtime dependencies.
* Reproducible packaging.
* Easier deployment across environments.
* Reduced environment-specific differences.
  **Interview Answer:** "Docker packages the application and its runtime dependencies, helping reduce differences between development, testing, and deployment environments."

## 38. CI/CD for Django + React/Next.js

**Typical Full Stack Workflow:**
`Git Push → Backend Tests + Frontend Tests → Backend Build + Frontend Build → Deploy to Staging → Integration Tests → Deploy`
**Backend Checks:**

```bash
python -m pytest
python manage.py check
```

**Frontend Checks:**

```bash
npm ci
npm run build
```

**Interview Answer:** "For a full-stack application, CI can validate backend and frontend components separately before deploying them together or independently."

# PART 5 — CI/CD FOR PYTHON ETL AND DATA AUTOMATION

## 39. CI/CD vs ETL Job Scheduling

| CI/CD                                                                                                                                                         | ETL Scheduling                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Validates and deploys code                                                                                                                                    | Executes data processing                |
| Triggered by code/release events                                                                                                                              | Triggered by time/data/events           |
| Example: GitHub Actions tests ETL code                                                                                                                        | Example: Scheduler runs ETL every night |
| Focuses on code quality and delivery                                                                                                                          | Focuses on data processing              |
| **Important:** CI/CD and job scheduling are related but not the same.                                                                                         |                                         |
| **Interview Answer:** "CI/CD ensures ETL code is tested and deployed safely, while a scheduler runs the deployed ETL job according to business requirements." |                                         |

## 40. Example ETL Deployment Flow

**Scenario:** A Python script processes transaction CSV files every night.
**Workflow:**

1. Developer modifies transformation logic.
2. Pushes changes to a feature branch.
3. CI runs linting and tests.
4. PR is reviewed and merged.
5. Pipeline packages the ETL job.
6. Job is deployed to the execution environment.
7. Scheduler triggers the job nightly.
8. Monitoring tracks success, failures, and data quality.
   **Interview Answer:** "I separate code deployment from scheduled ETL execution. CI/CD validates and releases the pipeline code, while operational scheduling and monitoring manage its execution."

## 41. Testing ETL Pipelines in CI

**Checks:**

| Check                | Example                                              |
| -------------------- | ---------------------------------------------------- |
| Schema validation    | Required columns exist                               |
| Null validation      | Mandatory fields are populated                       |
| Duplicate validation | Transaction IDs satisfy uniqueness rules             |
| Type validation      | Amount is numeric                                    |
| Date validation      | Trade date is valid                                  |
| Reconciliation       | Input and output counts/totals satisfy rules         |
| Regression           | Previous valid inputs still produce expected outputs |
| Error handling       | Invalid files produce controlled failures            |

## 42. ETL Integration Test Example

**Scenario:** Read a sample CSV, clean data, and verify output.

```python
import pandas as pd

def transform(df):
    result = df.copy()
    result["Amount"] = pd.to_numeric(result["Amount"], errors="coerce")
    return result.dropna(subset=["Amount"])

def test_etl_pipeline(tmp_path):
    input_path = tmp_path / "input.csv"
    pd.DataFrame({
        "TransactionID": [1, 2],
        "Amount": ["100", "invalid"]
    }).to_csv(input_path, index=False)

    source = pd.read_csv(input_path)
    output = transform(source)

    assert len(output) == 1
    assert output["Amount"].iloc[0] == 100
```

**Interview Answer:** "I test ETL pipelines using representative input files and verify expected transformations, output counts, and failure handling."

## 43. How Do You Prevent Bad ETL Code from Reaching Production?

**Answer:**

1. Validate code through CI.
2. Run unit and integration tests.
3. Check data quality rules.
4. Require PR review.
5. Deploy to staging.
6. Test with representative data.
7. Require production approval where applicable.
8. Monitor outputs after deployment.

## 44. How Do You Handle a Failed ETL Deployment?

**Answer:** "I would check deployment and execution logs, identify the failure stage, stop further impact, and restore the previous approved version if necessary. I would also check whether any partial data was written and whether reconciliation or recovery is required."

# PART 6 — HARD: TROUBLESHOOTING AND BEST PRACTICES

## 45. Pipeline Failure Scenarios

| Failure                           | Possible Cause                           | Resolution                                       |
| --------------------------------- | ---------------------------------------- | ------------------------------------------------ |
| Dependency installation fails     | Incompatible package versions            | Inspect logs and dependency constraints          |
| Unit tests fail                   | Code regression                          | Reproduce and fix                                |
| Lint fails                        | Rule violations                          | Correct issues                                   |
| Build fails                       | Missing configuration/dependencies       | Inspect build logs                               |
| Deployment fails                  | Credentials, permissions, infrastructure | Check environment and access                     |
| Tests pass locally but fail in CI | Environment mismatch                     | Compare runtime, dependencies, and configuration |
| Pipeline is slow                  | Repeated installations/heavy tests       | Use caching, parallelism, optimization           |
| Secret unavailable                | Incorrect scope or permissions           | Check approved secret configuration              |
| ETL output incorrect              | Business logic/data issue                | Reconcile output and fix transformation          |

## 46. Tests Pass Locally but Fail in CI

**Possible Causes:**

* Different Python versions.
* Different dependency versions.
* Missing environment variables.
* OS-specific behavior.
* Different file paths.
* Time-zone differences.
* Tests relying on execution order.
* External service availability.
  **Interview Answer:** "I compare the CI and local environments, reproduce the failure, inspect dependencies and configuration, and make the tests deterministic where possible."

## 47. How to Optimize a Slow CI Pipeline

**Approaches:**

* Cache dependencies.
* Run independent jobs in parallel.
* Avoid unnecessary installations.
* Separate fast unit tests from expensive integration tests.
* Use targeted workflows for relevant changes.
* Reuse build artifacts.
* Profile slow test suites.
  **Interview Answer:** "I would identify the slowest stages first, then optimize dependency installation, parallelize independent checks, and avoid unnecessary work without compromising required validation."

## 48. What Is a Flaky Test?

A flaky test passes or fails inconsistently without a corresponding code change.
**Possible Causes:**

* Timing dependencies.
* Race conditions.
* Shared test state.
* External API instability.
* Random data without fixed seeds.
  **Interview Answer:** "I investigate flaky tests by reproducing them, isolating dependencies, and removing nondeterministic behavior. I avoid treating repeated retries as a permanent solution."

## 49. What Is Idempotency in Deployment?

Idempotency means repeating an operation produces the same intended end state without unwanted additional effects.
**Example:** Running a deployment script twice should not create duplicate scheduled jobs or duplicate infrastructure resources.
**ETL Example:** Reprocessing the same batch should not duplicate records if the business requirement demands exactly-once outcomes.
**Interview Answer:** "Idempotency makes retries safer by ensuring repeated execution does not create unintended duplicate effects."

## 50. What Is Infrastructure as Code?

Infrastructure as Code (IaC) means defining infrastructure using version-controlled configuration.
**Examples:** Terraform, CloudFormation, Bicep.
**Interview Answer:** "IaC makes infrastructure changes repeatable, reviewable, and easier to automate through CI/CD."
**Priority:** Conceptual knowledge is sufficient unless the JD explicitly requires hands-on IaC.

## 51. CI/CD Security Best Practices

* Use least-privilege permissions.
* Protect production environments.
* Keep secrets out of source code.
* Use approved secret storage.
* Prefer short-lived credentials.
* Pin and review dependencies/actions.
* Scan for known vulnerabilities.
* Restrict untrusted workflow execution.
* Require review for sensitive changes.
* Maintain deployment audit trails.
  **Interview Answer:** "I secure CI/CD by limiting permissions, protecting secrets, reviewing dependencies, and enforcing approvals and automated checks."

## 52. What Is OIDC in CI/CD?

OpenID Connect allows workflows to obtain short-lived credentials from supported cloud providers without storing long-lived cloud access keys in repository secrets.
**Interview Answer:** "OIDC helps reduce credential exposure by allowing trusted CI/CD workflows to authenticate using short-lived cloud credentials."
**Priority:** Awareness-level knowledge.

## 53. Monitoring After Deployment

**Common Metrics:**

* Deployment success/failure.
* Application error rate.
* Job execution duration.
* CPU and memory usage.
* ETL processed/rejected record counts.
* Data quality failures.
* API latency.
  **Interview Answer:** "A successful deployment is not the end of the process. I monitor application health and business metrics to ensure the released version behaves correctly."

# PART 7 — REAL-WORLD INTERVIEW SCENARIOS

## 54. Scenario 1: A Developer Pushes Code to GitHub

**Question:** "What happens next in CI/CD?"
**Answer:** "A configured workflow is triggered. It checks out the code, prepares the environment, installs dependencies, runs automated quality checks and tests, and may build an artifact. Deployment proceeds only if the required conditions are satisfied."

## 55. Scenario 2: A PR Has Failing Tests

**Question:** "Would you merge it?"
**Answer:** "Normally no. I would inspect the failing checks, reproduce the problem, fix it, and rerun the pipeline. Any exception should follow the team's documented approval process."

## 56. Scenario 3: Production Deployment Fails

**Question:** "What would you do?"
**Answer:** "I would inspect deployment logs and health checks, identify whether the failure involves code, configuration, or infrastructure, stop further impact, and follow the approved rollback or recovery process."

## 57. Scenario 4: ETL Job Produces Incorrect Data After Deployment

**Question:** "How would you respond?"
**Answer:** "I would pause affected processing, inspect recent code and configuration changes, compare input/output records, identify the root cause, and coordinate rollback or correction. I would also assess whether already-written data needs reconciliation or reprocessing."

## 58. Scenario 5: CI Pipeline Takes 30 Minutes

**Question:** "How would you improve it?"
**Answer:** "I would examine job timings, cache dependencies, parallelize independent checks, and separate fast tests from slower integration tests while preserving required quality gates."

## 59. Scenario 6: Deployment Requires a Database Migration

**Question:** "What precautions would you take?"
**Answer:** "I would test the migration in staging, verify backups and recovery procedures, assess compatibility between application versions and database schema, and follow a controlled deployment sequence."

## 60. Scenario 7: How Would You Set Up CI/CD for a Python Project?

**Answer:** "I would store code in GitHub, configure GitHub Actions to run on pull requests and relevant pushes, install dependencies, run linting and pytest tests, package the application if required, and deploy approved versions through a controlled release process."

## 61. Scenario 8: How Would You Set Up CI/CD for a Full Stack Application?

**Answer:** "I would create separate backend and frontend validation jobs, run Python and JavaScript tests, build the application components, deploy to staging, run integration checks, and release to production through the approved process."

# PART 8 — TOP 30 CI/CD INTERVIEW QUESTIONS

## 62. Questions and Answers

| Question                                | Interview Answer                                                      |
| --------------------------------------- | --------------------------------------------------------------------- |
| 1. What is CI/CD?                       | Automated integration, validation, and delivery/deployment.           |
| 2. What is CI?                          | Frequent code integration with automated checks.                      |
| 3. Continuous Delivery vs Deployment?   | Release-ready with possible approval vs automatic production release. |
| 4. Why use CI/CD?                       | Improve quality, consistency, and release speed.                      |
| 5. What is a pipeline?                  | Sequence of automated workflow stages.                                |
| 6. What triggers a pipeline?            | Push, PR, schedule, manual action, release event.                     |
| 7. What is GitHub Actions?              | GitHub's workflow automation platform.                                |
| 8. What is a workflow?                  | YAML-defined automation process.                                      |
| 9. What is a job?                       | Group of steps running on a runner.                                   |
| 10. What is a runner?                   | Environment executing a job.                                          |
| 11. What is a step?                     | Individual command or reusable action.                                |
| 12. What is an artifact?                | Output file/package from a workflow.                                  |
| 13. What is caching?                    | Reusing selected data to speed up workflows.                          |
| 14. What is automated testing?          | Programmatic validation of software behavior.                         |
| 15. Unit vs integration testing?        | Individual function vs component interaction.                         |
| 16. What is regression testing?         | Checking existing functionality after changes.                        |
| 17. What is linting?                    | Static checks for code issues and conventions.                        |
| 18. What is a quality gate?             | Required condition before progression.                                |
| 19. What happens when CI fails?         | Investigate, fix, and rerun checks.                                   |
| 20. What is staging?                    | Preproduction validation environment.                                 |
| 21. What is rollback?                   | Restore a previously approved state/version.                          |
| 22. What is blue-green deployment?      | Switch traffic between two environments.                              |
| 23. What is canary deployment?          | Gradually expose a release to limited traffic.                        |
| 24. What is Docker's role?              | Package runtime and application consistently.                         |
| 25. What are CI/CD secrets?             | Protected credentials used by workflows.                              |
| 26. How do you secure pipelines?        | Least privilege, secrets management, approvals, scanning.             |
| 27. How do you speed up CI?             | Caching, parallelism, targeted tests, artifact reuse.                 |
| 28. What is a flaky test?               | Test with inconsistent results absent code changes.                   |
| 29. CI/CD vs scheduling?                | Code delivery vs execution timing.                                    |
| 30. How do you validate ETL deployment? | Test code, reconcile data, monitor processing.                        |

# PART 9 — COMMANDS AND QUICK REFERENCE

## 63. Common Commands

| Task                       | Command                           |
| -------------------------- | --------------------------------- |
| Run Python tests           | `python -m pytest`                |
| Run verbose tests          | `python -m pytest -v`             |
| Run coverage               | `python -m pytest --cov=.`        |
| Run Ruff linting           | `ruff check .`                    |
| Run Black format check     | `black --check .`                 |
| Install dependencies       | `pip install -r requirements.txt` |
| Build Docker image         | `docker build -t app:1.0 .`       |
| Run Docker container       | `docker run --rm app:1.0`         |
| Check Django configuration | `python manage.py check`          |
| Install Node dependencies  | `npm ci`                          |
| Build frontend             | `npm run build`                   |

## 64. Common CI/CD Terms

| Term         | Meaning                                         |
| ------------ | ----------------------------------------------- |
| Pipeline     | Automated workflow                              |
| Workflow     | Automation configuration                        |
| Trigger      | Event starting a workflow                       |
| Runner       | Execution machine                               |
| Job          | Group of workflow steps                         |
| Step         | Individual command/action                       |
| Artifact     | Generated output                                |
| Cache        | Reusable data for speed                         |
| Quality Gate | Required validation                             |
| Staging      | Preproduction environment                       |
| Deployment   | Release to an environment                       |
| Rollback     | Restore previous approved version               |
| Secret       | Protected sensitive value                       |
| OIDC         | Short-lived federated authentication            |
| IaC          | Version-controlled infrastructure configuration |

# PART 10 — FINAL UBER INTERVIEW REVISION

## 65. Most Important Topics

| Priority | Topic                                   | Expected Depth                |
| -------- | --------------------------------------- | ----------------------------- |
| 🔴 1     | CI vs Continuous Delivery vs Deployment | Explain clearly               |
| 🔴 2     | End-to-end CI/CD pipeline               | Explain complete flow         |
| 🔴 3     | GitHub Actions                          | Understand and explain YAML   |
| 🔴 4     | Automated testing                       | Unit, integration, regression |
| 🔴 5     | Pipeline failure troubleshooting        | Practical scenarios           |
| 🔴 6     | CI/CD for Python ETL                    | Apply concepts                |
| 🔴 7     | Secrets and environment variables       | Security basics               |
| 🟠 8     | Docker in CI/CD                         | Basic commands and purpose    |
| 🟠 9     | Deployment and rollback                 | Practical understanding       |
| 🟠 10    | GitHub PR + CI integration              | Collaboration workflow        |
| 🟠 11    | Caching and artifacts                   | Conceptual knowledge          |
| 🟢 12    | Kubernetes, IaC, OIDC                   | Overview only                 |

## 66. One-Minute Interview Answer

"CI/CD automates the process of integrating, testing, and delivering code changes. In a Python project, I would configure a pipeline using a tool such as GitHub Actions. When a developer raises a pull request, the pipeline checks out the code, installs dependencies, runs linting and automated tests, and verifies the changes. Once approved and merged, a delivery pipeline can package the application and deploy it to staging or production according to the release process. For ETL applications, I would also validate data quality, reconciliation rules, and job execution after deployment. If a deployment fails, I would inspect logs and follow the approved rollback or recovery process."

## 67. Final Interview Checklist

* [ ] Explain CI/CD in simple terms.
* [ ] Differentiate CI, Continuous Delivery, and Continuous Deployment.
* [ ] Explain the complete pipeline flow.
* [ ] Explain GitHub Actions workflows, jobs, runners, and steps.
* [ ] Understand a basic Python GitHub Actions YAML file.
* [ ] Explain unit, integration, and regression testing.
* [ ] Explain linting and quality gates.
* [ ] Explain staging and production deployments.
* [ ] Explain how to handle a failed pipeline.
* [ ] Explain how to handle a failed production deployment.
* [ ] Explain Docker's role in CI/CD.
* [ ] Explain secrets and environment variables.
* [ ] Explain CI/CD for Python ETL scripts.
* [ ] Explain CI/CD for Django and React applications.
* [ ] Explain how GitHub PRs integrate with CI checks.
  **FINAL INTERVIEW RULE:** Don't memorize only definitions. Be prepared to describe an end-to-end CI/CD workflow, explain a basic GitHub Actions YAML file, and troubleshoot a failed Python pipeline.
