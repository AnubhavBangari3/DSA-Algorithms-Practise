# GIT + GITHUB — UBER INTERVIEW CHEATSHEET

**Role:** Python Automation / Data Transformation Engineer
**Focus:** Git commands, branching, merging, pull requests, conflicts, collaboration, troubleshooting, and CI/CD integration.
**Interview Goal:** Explain how you manage Python scripts, ETL pipelines, code changes, collaboration, and releases using Git/GitHub.

# PART 1 — EASY: GIT FUNDAMENTALS

## 1. What is Git?

Git is a distributed version control system used to track code changes, maintain version history, collaborate with developers, and restore previous versions.
**Example:** You are working on a Python ETL script. You modify its data-cleaning logic, commit your changes, and push them to a shared repository.
**Interview Answer:** "Git helps me track code changes, maintain different development branches, collaborate with other developers, and safely manage releases."

## 2. Git vs GitHub

| Git                                                                              | GitHub                                                       |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Distributed version control system                                               | Cloud-based Git repository hosting platform                  |
| Runs locally                                                                     | Hosts remote repositories                                    |
| Tracks commits and branches                                                      | Provides pull requests, reviews, permissions, and automation |
| Works without internet                                                           | Requires connectivity for remote operations                  |
| Example: `git commit`                                                            | Example: GitHub pull request                                 |
| **Remember:** Git is the tool. GitHub is a platform that hosts Git repositories. |                                                              |

## 3. Git Architecture

**Basic Flow:**
`Working Directory → Staging Area → Local Repository → Remote Repository`

| Area                                                                                                                                                             | Meaning                              | Command       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------- |
| Working Directory                                                                                                                                                | Files you are editing                | Edit `etl.py` |
| Staging Area                                                                                                                                                     | Changes selected for the next commit | `git add`     |
| Local Repository                                                                                                                                                 | Saved commit history                 | `git commit`  |
| Remote Repository                                                                                                                                                | Shared repository on GitHub          | `git push`    |
| **Interview Answer:** "I modify files in my working directory, stage the required changes, create a local commit, and push the commit to the remote repository." |                                      |               |

## 4. Basic Git Configuration

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```

**Explanation:** Git uses the configured name and email to identify commit authors.

## 5. Initialize a Repository

```bash
mkdir python-etl
cd python-etl
git init
```

**Explanation:** Creates a new local Git repository.

## 6. Clone an Existing Repository

```bash
git clone https://github.com/example/python-etl.git
cd python-etl
```

**Explanation:** Downloads the repository and its history to your machine.
**Interview Question:** Difference between `git init` and `git clone`?
**Answer:** "`git init` creates a new repository, while `git clone` copies an existing repository."

## 7. Check Repository Status

```bash
git status
git status --short
```

**Explanation:** Shows modified, staged, and untracked files.
**Example:**
`M etl.py` → Modified tracked file.
`?? report.py` → Untracked file.
**Note:** Short status uses two columns; a change can be staged, unstaged, or both.

## 8. Stage Changes

```bash
git add etl.py
git add .
git add -A
git add -p
```

| Command                                                                                                                       | Meaning                               |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `git add etl.py`                                                                                                              | Stage one file                        |
| `git add .`                                                                                                                   | Stage changes under current directory |
| `git add -A`                                                                                                                  | Stage all changes across repository   |
| `git add -p`                                                                                                                  | Interactively stage selected changes  |
| **Best Practice:** Stage only related changes. Avoid accidentally committing generated data, credentials, or unrelated files. |                                       |

## 9. Commit Changes

```bash
git commit -m "Add transaction validation logic"
```

**Explanation:** Saves staged changes as a commit in local Git history.
**Good Commit Messages:**

* `Add CSV schema validation`
* `Fix duplicate transaction handling`
* `Optimize Pandas merge performance`
* `Add unit tests for ETL transformations`
  **Bad Commit Messages:**
* `changes`
* `final`
* `fixed`
* `updated code`
  **Interview Answer:** "I create small, meaningful commits with descriptive messages so changes are easy to review and troubleshoot."

## 10. Push Changes

```bash
git push origin main
```

**Explanation:** Uploads local commits from `main` to the remote `main` branch.
**First Push of a New Branch:**

```bash
git push -u origin feature/data-cleaning
```

**Explanation:** Sets the upstream branch so future pushes can use `git push`.

## 11. Fetch Changes

```bash
git fetch origin
```

**Explanation:** Downloads remote commits and updates remote-tracking references without automatically merging them into your current branch.

## 12. Pull Changes

```bash
git pull origin main
```

**Explanation:** Fetches changes from the remote `main` branch and integrates them into the current branch using the configured pull strategy.
**Important:** `git pull` can merge or rebase depending on configuration.

## 13. Fetch vs Pull

| `git fetch`                                                                                                                                                       | `git pull`                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Downloads remote changes                                                                                                                                          | Downloads and integrates changes            |
| Does not change current working files                                                                                                                             | May update current branch and working files |
| Useful for inspecting updates first                                                                                                                               | Useful for updating a local branch          |
| Safer when you want to review changes                                                                                                                             | Requires attention to conflicts             |
| **Interview Answer:** "`git fetch` downloads remote updates without integrating them into my current branch. `git pull` fetches and then integrates the changes." |                                             |

## 14. View Commit History

```bash
git log
git log --oneline
git log --oneline --graph --all --decorate
git log -5
```

**Explanation:** Shows commit history and branch relationships.

## 15. View Changes

```bash
git diff
git diff --staged
git diff main..feature/data-cleaning
```

| Command                                | Meaning                         |
| -------------------------------------- | ------------------------------- |
| `git diff`                             | Unstaged changes                |
| `git diff --staged`                    | Staged changes                  |
| `git diff main..feature/data-cleaning` | Differences between branch tips |

## 16. Check Remote Repository

```bash
git remote -v
git remote add origin https://github.com/example/python-etl.git
git remote set-url origin https://github.com/example/new-repo.git
```

**Explanation:** View, add, or update remote repository addresses.

## 17. `.gitignore`

**Purpose:** Prevent unnecessary or sensitive untracked files from being added to Git.
**Python ETL `.gitignore`:**

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
.env.*
!.env.example
.pytest_cache/
.mypy_cache/
.coverage
htmlcov/
*.log
data/raw/
data/processed/
output/
*.parquet
```

**Important:** Ignore rules depend on the project. Small test fixtures may intentionally be committed.
**Interview Answer:** "I use `.gitignore` to exclude local environments, generated files, caches, and sensitive configuration."
**Important:** `.gitignore` does not remove files already tracked by Git.

## 18. Stop Tracking a File Without Deleting It Locally

```bash
git rm --cached .env
git commit -m "Stop tracking local environment file"
```

**Security Note:** If credentials were committed, removing the file from the latest commit is insufficient. Rotate exposed credentials and follow the repository's secret-remediation process.

# PART 2 — MEDIUM: BRANCHING AND COLLABORATION

## 19. What is a Branch?

A branch is a movable reference to a commit. It allows developers to work on changes independently.
**Example:** You need to improve CSV validation without directly modifying the production branch.
**Flow:**
`main → feature/csv-validation → Pull Request → Review → Merge into main`

## 20. Common Branch Types

| Branch                                                                                                          | Purpose                                              |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `main`                                                                                                          | Stable/integration branch                            |
| `develop`                                                                                                       | Shared development branch, if the team uses Git Flow |
| `feature/...`                                                                                                   | New functionality                                    |
| `bugfix/...`                                                                                                    | Fix a defect                                         |
| `hotfix/...`                                                                                                    | Urgent production fix                                |
| `release/...`                                                                                                   | Release preparation, if applicable                   |
| **Best Practice:** Follow the team's branching strategy. Not every project needs `develop` or release branches. |                                                      |

## 21. Create and Switch Branches

```bash
git branch
git branch -a
git switch -c feature/csv-validation
git switch main
git switch feature/csv-validation
```

**Older Syntax:**

```bash
git checkout -b feature/csv-validation
git checkout main
```

**Interview Answer:** "I create feature branches for isolated changes, test them, and merge them through reviewed pull requests."

## 22. Rename and Delete Branches

```bash
git branch -m feature/old-name feature/new-name
git branch -d feature/old-name
git branch -D feature/old-name
git push origin --delete feature/old-name
```

| Command                                                                        | Meaning                              |
| ------------------------------------------------------------------------------ | ------------------------------------ |
| `-m`                                                                           | Rename branch                        |
| `-d`                                                                           | Delete local branch if safely merged |
| `-D`                                                                           | Force-delete local branch            |
| `push --delete`                                                                | Delete remote branch                 |
| **Warning:** Force-deleting a branch may make unmerged work harder to recover. |                                      |

## 23. Merge Branches

**Scenario:** You completed CSV validation on a feature branch.

```bash
git switch main
git pull --ff-only origin main
git merge feature/csv-validation
git push origin main
```

**Explanation:** Integrates changes from the feature branch into `main`.
**Team Best Practice:** In a protected repository, developers normally create a pull request instead of pushing directly to `main`.

## 24. Fast-Forward Merge vs Three-Way Merge

| Fast-Forward Merge                                                                                                                                                             | Three-Way Merge                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| Target branch has not diverged                                                                                                                                                 | Branches have diverged                   |
| Moves branch pointer forward                                                                                                                                                   | Combines changes using a common ancestor |
| May not create a merge commit                                                                                                                                                  | Usually creates a merge commit           |
| Simple linear history                                                                                                                                                          | Preserves branch integration history     |
| **Interview Answer:** "A fast-forward merge moves the target branch pointer forward when possible. A three-way merge combines diverged histories using their common ancestor." |                                          |

## 25. What is a Pull Request?

A pull request (PR) is a request to review and integrate changes from one branch into another.
**Typical Workflow:**

1. Create a feature branch.
2. Implement the change.
3. Add tests.
4. Commit and push.
5. Open a PR on GitHub.
6. Request code review.
7. Address review comments.
8. Wait for required CI checks.
9. Merge after approval.
   **Interview Answer:** "I use pull requests to make code changes reviewable, discuss implementation choices, run automated checks, and merge changes safely."

## 26. Practical Pull Request Example

**Scenario:** You optimized a Pandas ETL script.
**Branch:** `feature/optimize-etl`
**PR Title:** `Optimize transaction processing using chunked CSV reads`
**PR Description:**

```text
Summary:
- Replace full-file CSV loading with chunked processing.
- Add validation for required columns.
- Improve logging and error handling.
Testing:
- Tested valid and invalid CSV inputs.
- Verified output row counts and totals.
- Compared results with the previous implementation.
Impact:
- Reduces peak memory usage for large input files.
```

**Best Practice:** Include what changed, why, how it was tested, and any deployment or compatibility risks.

## 27. How to Review a Pull Request

**Check:**

* Does the change meet the requirement?
* Is the logic correct?
* Are edge cases handled?
* Are tests included?
* Are credentials or sensitive data exposed?
* Are error messages meaningful?
* Does the change affect performance?
* Are unrelated changes included?
* Are CI checks passing?
  **Uber-Relevant Example:** A PR changes duplicate transaction handling. Verify whether the business rule is to retain the first record, latest record, or reject conflicting duplicates.

## 28. Merge vs Rebase

| Merge                                  | Rebase                                     |
| -------------------------------------- | ------------------------------------------ |
| Integrates branch histories            | Replays commits onto a new base            |
| Usually preserves original commit IDs  | Rewrites commit IDs for replayed commits   |
| May create a merge commit              | Can produce linear history                 |
| Suitable for shared branch integration | Useful for updating local feature branches |
| **Example Merge:**                     |                                            |

```bash
git switch feature/data-cleaning
git fetch origin
git merge origin/main
```

**Example Rebase:**

```bash
git switch feature/data-cleaning
git fetch origin
git rebase origin/main
```

**Interview Answer:** "Merge preserves the existing history, while rebase rewrites the feature branch's commits on top of another base. I avoid rebasing shared branches unless the team has explicitly agreed on that workflow."

## 29. What Happens After Rebase?

If you already pushed the feature branch, rebasing changes its commit history.
**Possible Command:**

```bash
git push --force-with-lease origin feature/data-cleaning
```

**Why `--force-with-lease`?** It adds a safety check against overwriting remote changes you have not seen.
**Warning:** Use only when permitted by team policy and after understanding the effect on collaborators. Avoid force-pushing protected branches.

# PART 3 — MERGE CONFLICTS

## 30. What is a Merge Conflict?

A merge conflict occurs when Git cannot automatically combine changes, such as when two branches modify the same lines differently.
**Example:** Two developers modify the transaction validation logic in `etl.py`.

## 31. Example Merge Conflict

```python
<<<<<<< HEAD
def validate_amount(amount):
    return amount >= 0
=======
def validate_amount(amount):
    return amount > 0
>>>>>>> feature/validation
```

**Meaning:**

| Marker                                                              | Meaning                   |
| ------------------------------------------------------------------- | ------------------------- |
| `<<<<<<< HEAD`                                                      | Current branch's version  |
| `=======`                                                           | Separator                 |
| `>>>>>>> feature/validation`                                        | Incoming branch's version |
| **Important:** Git cannot determine which business rule is correct. |                           |

## 32. How to Resolve a Merge Conflict

**Steps:**

1. Run `git status`.
2. Identify conflicted files.
3. Open each file and inspect both changes.
4. Discuss the intended business logic if necessary.
5. Edit the file to the correct final version.
6. Remove conflict markers.
7. Run tests.
8. Stage the resolved file.
9. Complete the merge or rebase.
   **During Merge:**

```bash
git status
git add etl.py
git merge --continue
```

**During Rebase:**

```bash
git status
git add etl.py
git rebase --continue
```

**Interview Answer:** "I inspect both versions, understand the intended behavior, resolve the conflict manually, run tests, and complete the merge. I don't blindly choose one side because that may discard valid logic."

## 33. Abort a Merge or Rebase

```bash
git merge --abort
git rebase --abort
```

**Explanation:** Attempts to return the repository to the state before the current merge or rebase operation.

## 34. How to Prevent Frequent Conflicts

* Pull or fetch regularly.
* Keep feature branches short-lived.
* Make small, focused changes.
* Avoid unnecessary formatting changes.
* Communicate before modifying shared files.
* Divide large modules into smaller components where appropriate.
  **Interview Answer:** "I reduce conflicts by keeping branches up to date, making focused commits, and coordinating changes to shared code."

# PART 4 — UNDO, RECOVERY, AND TROUBLESHOOTING

## 35. `git restore`

**Discard unstaged changes in one file:**

```bash
git restore etl.py
```

**Unstage a file while preserving working changes:**

```bash
git restore --staged etl.py
```

**Warning:** Discarding working changes can permanently lose uncommitted work.

## 36. `git reset`

| Command                                                                                                                                           | Effect                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `git reset --soft HEAD~1`                                                                                                                         | Move HEAD back; keep changes staged                         |
| `git reset --mixed HEAD~1`                                                                                                                        | Move HEAD back; keep changes unstaged                       |
| `git reset --hard HEAD~1`                                                                                                                         | Move HEAD back; discard corresponding working/index changes |
| **Interview Answer:** "`reset` moves the current branch's reference and can modify the staging area and working directory depending on the mode." |                                                             |
| **Warning:** Avoid resetting shared published history without understanding the consequences.                                                     |                                                             |

## 37. `git revert`

```bash
git revert <commit-hash>
```

**Explanation:** Creates a new commit that reverses the effect of an earlier commit.
**Interview Answer:** "For a problematic commit already shared with the team, I usually prefer `git revert` because it preserves history."

## 38. Reset vs Revert

| Reset                                  | Revert                                       |
| -------------------------------------- | -------------------------------------------- |
| Moves branch history                   | Creates a new inverse commit                 |
| Can rewrite published history          | Preserves published history                  |
| Useful for local cleanup               | Generally safer for shared branches          |
| `git reset --hard` can discard changes | Does not inherently discard existing history |

## 39. `git stash`

**Scenario:** You have unfinished ETL changes but need to switch branches.

```bash
git stash push -m "WIP ETL validation"
git stash list
git stash pop
```

**Include Untracked Files:**

```bash
git stash push -u -m "WIP ETL validation"
```

**Other Commands:**

```bash
git stash apply
git stash drop
```

| Command                                                                                                                             | Meaning                                 |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `stash push`                                                                                                                        | Save selected local changes temporarily |
| `stash pop`                                                                                                                         | Apply stash and remove it if successful |
| `stash apply`                                                                                                                       | Apply stash without removing it         |
| `stash drop`                                                                                                                        | Delete stash entry                      |
| **Interview Answer:** "Stash lets me temporarily save unfinished work so I can switch tasks without committing incomplete changes." |                                         |

## 40. `git cherry-pick`

**Scenario:** A critical ETL bug fix exists on another branch, and you need that specific commit.

```bash
git cherry-pick <commit-hash>
```

**Explanation:** Applies the changes introduced by a selected commit to the current branch, normally creating a new commit.
**Interview Answer:** "Cherry-pick is useful when I need a specific fix without merging an entire branch."

## 41. `git reflog`

```bash
git reflog
```

**Explanation:** Shows local movements of HEAD and other recorded references.
**Use Case:** Recovering a commit after an accidental reset.
**Example:**

```bash
git switch -c recovery-branch <commit-hash>
```

**Interview Answer:** "Reflog can help recover commits after certain local history operations, provided those objects are still available."

## 42. Find Who Changed a Line

```bash
git blame etl.py
```

**Explanation:** Shows the commit associated with each line of the file.
**Use Case:** Investigate when validation logic changed.

## 43. Find the Commit That Introduced a Bug

```bash
git bisect start
git bisect bad
git bisect good <known-good-commit>
```

**Explanation:** Git bisect helps identify a problematic commit through binary search.
**Finish:**

```bash
git bisect reset
```

**Interview Answer:** "If a regression was introduced somewhere across many commits, I can use `git bisect` to narrow down the first bad commit."

# PART 5 — REAL-WORLD GIT WORKFLOW FOR PYTHON ETL

## 44. Scenario: Develop a New ETL Feature

**Requirement:** Add validation for missing transaction IDs.
**Step 1: Update local main.**

```bash
git switch main
git pull --ff-only origin main
```

**Step 2: Create feature branch.**

```bash
git switch -c feature/transaction-validation
```

**Step 3: Modify code.**

```python
def validate_transactions(df):
    return df.dropna(subset=["TransactionID"])
```

**Step 4: Run tests.**

```bash
python -m pytest
```

**Step 5: Review changes.**

```bash
git status
git diff
```

**Step 6: Stage and commit.**

```bash
git add etl.py tests/
git commit -m "Add transaction ID validation"
```

**Step 7: Push feature branch.**

```bash
git push -u origin feature/transaction-validation
```

**Step 8:** Create a pull request on GitHub.
**Step 9:** Complete review and required CI checks.
**Step 10:** Merge through the team's approved process.
**Interview Answer:** "I work on a feature branch, implement and test the change, create focused commits, push the branch, and open a pull request. After review and successful CI checks, the change is merged."

## 45. Scenario: Production ETL Script Has a Bug

**Question:** "A production ETL job is failing because of a recent code change. How would you fix it?"
**Answer:**

1. Check the failure logs and identify the affected version.
2. Review recent commits and deployment history.
3. Reproduce the issue using a representative test case.
4. If urgent, follow the approved rollback or hotfix process.
5. Create a fix branch.
6. Correct the logic and add a regression test.
7. Raise a PR and complete required checks.
8. Deploy through the approved release process.
9. Monitor the job and validate output.
   **Important:** Do not assume every failure requires a rollback; assess data impact and operational risk.

## 46. Scenario: Two Developers Modify the Same ETL Script

**Question:** "Both developers change `etl.py`, and Git reports a conflict. What will you do?"
**Answer:** "I would inspect both sets of changes, determine whether both are needed, resolve the conflicting code, run the relevant tests, and complete the merge. If the conflict concerns business rules, I would confirm the expected behavior before finalizing."

## 47. Scenario: You Accidentally Commit a Password

**Question:** "You accidentally committed an API key. What should you do?"
**Answer:** "I would treat the credential as exposed, revoke or rotate it immediately, inform the appropriate team, remove it from active code, and follow the repository's approved secret-remediation process. I would also add secret scanning and move credentials to environment variables or a secret manager."
**Important:** Deleting the password in a later commit does not guarantee removal from repository history.

## 48. Scenario: Your Push Is Rejected

**Error:** `non-fast-forward`
**Reason:** The remote branch has changes that your local branch does not contain.
**Possible Resolution for a Personal Feature Branch:**

```bash
git fetch origin
git rebase origin/feature/data-cleaning
git push origin feature/data-cleaning
```

**Alternative:** Merge the remote branch into your local branch.
**Interview Answer:** "I first fetch the latest changes and inspect the divergence. Then I integrate the remote updates using the team's approved merge or rebase strategy, resolve any conflicts, and push again."
**Important:** Avoid force-pushing simply to bypass a rejected push.

## 49. Scenario: You Committed to the Wrong Branch

**If the commit is local and unpublished:**

```bash
git switch -c feature/correct-branch
git switch main
git reset --hard HEAD~1
```

**Warning:** This example assumes the mistaken commit is the latest commit on `main`, and the working tree is clean. Verify before using `reset --hard`.
**If already pushed:** Follow the team's approved correction process; a revert or new PR may be appropriate.

## 50. Scenario: Your Teammate's PR Breaks Your Code

**Question:** "A teammate merged a change that breaks your ETL pipeline. What will you do?"
**Answer:** "I would reproduce the failure, identify the conflicting change using logs and Git history, discuss the issue with the teammate, and implement a compatible fix or approved revert. I would add regression tests to prevent recurrence."

# PART 6 — GITHUB BEST PRACTICES

## 51. Branch Protection

**Common Rules:**

* Require pull requests before merging.
* Require approvals.
* Require successful CI checks.
* Restrict force pushes.
* Restrict branch deletion.
* Require resolved review conversations.
  **Interview Answer:** "Branch protection helps prevent unreviewed or failing changes from reaching important branches."

## 52. Commit Best Practices

| Good Practice              | Why                        |
| -------------------------- | -------------------------- |
| Small commits              | Easier review and rollback |
| Descriptive messages       | Clear history              |
| Separate unrelated changes | Easier troubleshooting     |
| Test before commit/push    | Catch errors early         |
| Review staged diff         | Avoid accidental files     |
| Never commit secrets       | Security                   |
| Keep branches focused      | Reduce conflicts           |

## 53. Pull Request Best Practices

| Practice                     | Why                  |
| ---------------------------- | -------------------- |
| Clear PR title               | Easy to understand   |
| Explain business requirement | Context for reviewer |
| Summarize changes            | Faster review        |
| Include test results         | Confidence           |
| Mention risks                | Safer releases       |
| Link relevant ticket         | Traceability         |
| Address review feedback      | Maintain quality     |

## 54. GitHub Issues vs Pull Requests

| GitHub Issue                      | Pull Request                    |
| --------------------------------- | ------------------------------- |
| Tracks a task, bug, or discussion | Proposes code changes           |
| Can exist without code            | Usually includes branch changes |
| Used for planning and tracking    | Used for review and integration |

## 55. Tags and Releases

**Create a Tag:**

```bash
git tag -a v1.0.0 -m "ETL release 1.0.0"
git push origin v1.0.0
```

**Purpose:** Mark a specific commit as a release version.
**Interview Answer:** "Tags help identify released versions, making it easier to track deployments and investigate regressions."

## 56. What is a GitHub Actions Workflow?

GitHub Actions is an automation platform that can run workflows when repository events occur.
**Example:** When a developer opens a PR, GitHub Actions runs Python tests automatically.
**Simple Workflow:**

```yaml
name: Python Tests
on:
  pull_request:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python -m pytest
```

**Interview Point:** "GitHub Actions connects version control with automated testing and deployment workflows."
**Note:** Detailed CI/CD concepts will be covered separately in module 5C.

# PART 7 — INTERVIEW QUESTIONS

## 57. Top 30 Git/GitHub Interview Questions

| Question                                 | Interview Answer                                                  |
| ---------------------------------------- | ----------------------------------------------------------------- |
| 1. What is Git?                          | Distributed version control system.                               |
| 2. What is GitHub?                       | Platform for hosting Git repositories and collaboration.          |
| 3. Git vs GitHub?                        | Version control tool vs hosting/collaboration platform.           |
| 4. What is a repository?                 | A project and its version history.                                |
| 5. What is a commit?                     | A recorded snapshot of tracked project changes.                   |
| 6. What is staging?                      | Selecting changes for the next commit.                            |
| 7. `git add` vs `git commit`?            | Stage changes vs save a commit.                                   |
| 8. `git commit` vs `git push`?           | Save locally vs upload commits remotely.                          |
| 9. `git fetch` vs `git pull`?            | Download updates vs download and integrate.                       |
| 10. `git clone` vs `git init`?           | Copy existing repository vs create new repository.                |
| 11. What is a branch?                    | Movable reference used for independent development.               |
| 12. Why feature branches?                | Isolate changes from stable code.                                 |
| 13. What is merging?                     | Integrating changes from another branch.                          |
| 14. Merge vs rebase?                     | Preserve existing history vs replay commits onto another base.    |
| 15. What is a PR?                        | Request to review and integrate code changes.                     |
| 16. What is a merge conflict?            | Git cannot automatically reconcile changes.                       |
| 17. How resolve conflicts?               | Inspect, edit, test, stage, complete integration.                 |
| 18. What is `.gitignore`?                | Rules for ignoring matching untracked files.                      |
| 19. What is `git stash`?                 | Temporarily save local changes.                                   |
| 20. What is `git revert`?                | Create a commit that reverses an earlier change.                  |
| 21. Reset vs revert?                     | Move history vs create a reversing commit.                        |
| 22. What is cherry-pick?                 | Apply a selected commit's changes elsewhere.                      |
| 23. What is HEAD?                        | Reference to the current checkout/commit.                         |
| 24. What is origin?                      | Conventional name for a remote repository.                        |
| 25. What is upstream?                    | Branch used as the default remote tracking/integration reference. |
| 26. What is fast-forward merge?          | Move branch pointer forward without divergence.                   |
| 27. What is branch protection?           | Rules restricting updates to important branches.                  |
| 28. What is GitHub Actions?              | Workflow automation for repositories.                             |
| 29. How recover deleted commit?          | Inspect reflog if the commit is still available.                  |
| 30. How handle accidental secret commit? | Rotate credential, notify team, remediate repository exposure.    |

# PART 8 — COMMONLY CONFUSED COMMANDS

## 58. Git Command Comparison

| Commands                     | Difference                                                     |
| ---------------------------- | -------------------------------------------------------------- |
| `add` vs `commit`            | Stage changes vs save staged snapshot                          |
| `commit` vs `push`           | Save locally vs upload remotely                                |
| `fetch` vs `pull`            | Download vs download + integrate                               |
| `merge` vs `rebase`          | Combine histories vs replay commits                            |
| `reset` vs `revert`          | Move branch reference vs inverse commit                        |
| `restore` vs `reset`         | Restore files/index vs move HEAD and optionally index/worktree |
| `stash apply` vs `stash pop` | Keep stash vs remove after successful apply                    |
| `clone` vs `fork`            | Local copy vs server-side repository copy                      |
| `branch` vs `tag`            | Movable development reference vs release/version marker        |
| `checkout` vs `switch`       | General older command vs branch-focused switching              |

# PART 9 — PRACTICAL COMMAND REFERENCE

## 59. Essential Commands

| Task                     | Command                           |
| ------------------------ | --------------------------------- |
| Check version            | `git --version`                   |
| Initialize repository    | `git init`                        |
| Clone repository         | `git clone <url>`                 |
| Check status             | `git status`                      |
| Stage one file           | `git add file.py`                 |
| Stage all changes        | `git add -A`                      |
| Commit                   | `git commit -m "message"`         |
| Push                     | `git push origin branch`          |
| Pull                     | `git pull origin branch`          |
| Fetch                    | `git fetch origin`                |
| View branches            | `git branch -a`                   |
| Create branch            | `git switch -c branch`            |
| Switch branch            | `git switch branch`               |
| Merge branch             | `git merge branch`                |
| Rebase                   | `git rebase main`                 |
| View history             | `git log --oneline`               |
| View changes             | `git diff`                        |
| View staged changes      | `git diff --staged`               |
| Unstage file             | `git restore --staged file.py`    |
| Discard unstaged changes | `git restore file.py`             |
| Revert commit            | `git revert <hash>`               |
| Reset last commit        | `git reset --soft HEAD~1`         |
| Stash changes            | `git stash`                       |
| Restore stash            | `git stash pop`                   |
| Cherry-pick commit       | `git cherry-pick <hash>`          |
| View remotes             | `git remote -v`                   |
| View reflog              | `git reflog`                      |
| Delete merged branch     | `git branch -d branch`            |
| Delete remote branch     | `git push origin --delete branch` |
| View line history        | `git blame file.py`               |
| Create tag               | `git tag -a v1.0.0 -m "Release"`  |

# PART 10 — FINAL UBER INTERVIEW REVISION

## 60. Most Important Git Scenarios

| Priority | Scenario                       | What Interviewer Expects                     |
| -------- | ------------------------------ | -------------------------------------------- |
| 🔴 1     | New feature development        | Branch → code → test → commit → push → PR    |
| 🔴 2     | Merge conflict                 | Understand both changes → resolve → test     |
| 🔴 3     | Fetch vs pull                  | Correct conceptual difference                |
| 🔴 4     | Merge vs rebase                | Understand history and collaboration risks   |
| 🔴 5     | Undo a pushed commit           | Prefer revert for shared history             |
| 🔴 6     | Push rejected                  | Fetch → inspect → integrate → push           |
| 🟠 7     | Production bug                 | Investigate → hotfix/revert → test → release |
| 🟠 8     | Accidentally committed secrets | Rotate → report → remediate                  |
| 🟠 9     | CI checks fail                 | Inspect logs → fix → push updated commit     |
| 🟠 10    | ETL code collaboration         | PR review, validation, regression testing    |

## 61. One-Minute Git/GitHub Interview Answer

"Git is a distributed version control system that helps manage code changes and collaboration. In a typical development workflow, I start by updating my local repository, create a feature branch, implement the required changes, and test them locally. Then I stage and commit the changes with meaningful messages, push the branch to GitHub, and create a pull request. The PR goes through code review and automated checks before merging. If conflicts occur, I inspect both changes, resolve them carefully, and rerun tests. For production fixes, I use the team's approved hotfix or rollback process."

## 62. Final Preparation Checklist

| Topic                                                                                                                                                                                           | Priority     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Git workflow: add → commit → push                                                                                                                                                               | 🔴 Must Know |
| Clone, fetch, pull                                                                                                                                                                              | 🔴 Must Know |
| Branch creation and switching                                                                                                                                                                   | 🔴 Must Know |
| Merge and pull requests                                                                                                                                                                         | 🔴 Must Know |
| Merge conflict resolution                                                                                                                                                                       | 🔴 Must Know |
| Merge vs rebase                                                                                                                                                                                 | 🔴 Must Know |
| Reset vs revert                                                                                                                                                                                 | 🔴 Must Know |
| `.gitignore`                                                                                                                                                                                    | 🔴 Must Know |
| Stash                                                                                                                                                                                           | 🟠 Important |
| Push rejection                                                                                                                                                                                  | 🟠 Important |
| Cherry-pick                                                                                                                                                                                     | 🟠 Important |
| Branch protection                                                                                                                                                                               | 🟠 Important |
| GitHub Actions basics                                                                                                                                                                           | 🟠 Important |
| Reflog and bisect                                                                                                                                                                               | 🟢 Optional  |
| **FINAL INTERVIEW RULE:** Don't just memorize Git commands. Be ready to explain when to use them, why they matter, and how you would handle problems in a real Python ETL development workflow. |              |
