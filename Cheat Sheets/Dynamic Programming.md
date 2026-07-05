# Dynamic Programming (DP) Patterns (CP + Interview Guide)

This guide covers the **most important Dynamic Programming patterns** used in Competitive Programming and coding interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is Dynamic Programming?

Dynamic Programming (DP) is an optimization technique used when a problem has:

1. **Overlapping Subproblems**
2. **Optimal Substructure**

Instead of solving the same subproblem repeatedly, we solve it once and store the answer.

Think of DP as:

> "Remember the answer so you don't calculate it again."

---

# When to Think of DP

DP is usually required when you see:

* maximum
* minimum
* count ways
* total ways
* longest
* shortest
* optimal
* partition
* subset
* coin change
* climb stairs
* path counting
* interval problems

If recursion repeats the same state many times → Think DP.

---

# DP Approaches

There are three major approaches.

## 1. Pure Recursion

Very slow.

```
solve(n)

    solve(n-1)

    solve(n-2)
```

Time:

```
O(2^n)
```

---

## 2. Memoization (Top Down)

Store already computed answers.

```
memo[state]

if already solved:
    return memo[state]
```

---

## 3. Tabulation (Bottom Up)

Start from smallest state.

```
dp[0]

dp[1]

dp[2]

...

dp[n]
```

Usually preferred in interviews.

---

# DP Recipe (VERY IMPORTANT)

Whenever solving DP:

Step 1

Define the state

```
dp[i]
```

means what?

Example:

```
Maximum profit till i

Minimum cost till i

Ways to reach i
```

---

Step 2

Find transition

How does current answer depend on previous answers?

Example

```
dp[i] = dp[i-1] + dp[i-2]
```

---

Step 3

Base Case

```
dp[0]

dp[1]
```

---

Step 4

Build answer

Fill DP table.

---

# Pattern 1) Fibonacci DP

### When to use

Simple introduction to DP.

### Recurrence

```
dp[i] = dp[i-1] + dp[i-2]
```

### Code

```python
def fib(n):
    if n <= 1:
        return n

    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

Complexity

Time

```
O(n)
```

Space

```
O(n)
```

---

# Pattern 2) Climbing Stairs

### When to use

Count number of ways.

### Transition

```
dp[i] = dp[i-1] + dp[i-2]
```

### Code

```python
def climbStairs(n):
    if n <= 2:
        return n

    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

Recognition

* count ways
* staircase
* jumps

---

# Pattern 3) House Robber

### When to use

Maximum sum without adjacent elements.

### Transition

```
Take current

Skip current
```

```
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

### Code

```python
def rob(nums):
    if len(nums) == 1:
        return nums[0]

    dp = [0]*len(nums)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]
```

Recognition

* cannot choose adjacent
* maximize profit

---

# Pattern 4) Coin Change (Minimum Coins)

### When to use

Need minimum number of coins.

### Transition

```
dp[amount]

Try every coin
```

### Code

```python
def coinChange(coins, amount):
    INF = float('inf')

    dp = [INF]*(amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(
                    dp[i],
                    dp[i-coin] + 1
                )

    return dp[amount] if dp[amount] != INF else -1
```

Recognition

* minimum coins
* minimum cost

---

# Pattern 5) Coin Change II

### When to use

Count number of ways.

### Transition

```
dp[i] += dp[i-coin]
```

### Code

```python
def change(amount, coins):
    dp = [0]*(amount+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]

    return dp[amount]
```

Recognition

* number of ways
* combinations

---

# Pattern 6) Longest Increasing Subsequence (LIS)

### When to use

Longest increasing sequence.

### Transition

```
dp[i]

Look at all j < i
```

### Code

```python
def lengthOfLIS(nums):
    dp = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)
```

Complexity

```
O(n²)
```

---

# Pattern 7) Longest Common Subsequence (LCS)

### When to use

Compare two strings.

### Transition

If equal

```
1 + diagonal
```

Else

```
max(top,left)
```

### Code

```python
def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(
                    dp[i-1][j],
                    dp[i][j-1]
                )

    return dp[m][n]
```

Recognition

* common subsequence
* compare strings

---

# Pattern 8) Edit Distance

### When to use

Minimum operations.

Operations

* Insert
* Delete
* Replace

### Transition

```
min(
insert,
delete,
replace
)
```

Recognition

* convert string
* minimum edits

---

# Pattern 9) 0/1 Knapsack

### When to use

Each item can be taken once.

State

```
dp[item][capacity]
```

Transition

```
Take

Skip
```

Code

```python
def knapsack(weights, values, W):

    n = len(weights)

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(W+1):

            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )

            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]
```

---

# Pattern 10) Partition Equal Subset Sum

### When to use

Can array be divided equally?

Idea

Subset sum DP.

Recognition

* subset
* partition

---

# Pattern 11) Unique Paths

### When to use

Count paths in grid.

Transition

```
Top

Left
```

Code

```python
def uniquePaths(m,n):

    dp = [[1]*n for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
```

Recognition

* grid
* robot
* count paths

---

# Pattern 12) Minimum Path Sum

### Transition

```
Current

+

minimum(top,left)
```

Recognition

* minimum cost path

---

# Pattern 13) Decode Ways

Transition

```
One digit

Two digits
```

Recognition

* number string
* decode
* count ways

---

# Pattern 14) Palindrome DP

Examples

* Longest Palindrome Substring
* Palindrome Partitioning

State

```
dp[i][j]
```

means

Substring

```
i

to

j
```

Recognition

* palindrome
* substring

---

# Pattern 15) Interval DP

Examples

* Burst Balloons
* Matrix Chain Multiplication

State

```
dp[left][right]
```

Recognition

* interval
* partition

---

# Pattern 16) Bitmask DP

Used when

```
n <= 20
```

Examples

* Traveling Salesman
* Assignment Problem

State

```
mask

current node
```

Recognition

* visit all nodes
* minimum cost

---

# Pattern 17) Digit DP

When numbers become huge.

Examples

Count numbers satisfying property.

Recognition

* range of numbers
* digits

---

# Pattern 18) Tree DP

Run DFS.

Every node returns answer.

Recognition

* tree
* maximum path
* independent set

---

# Pattern 19) State Machine DP

Examples

Best Time to Buy and Sell Stock

States

```
Buy

Sell

Cooldown

Transaction
```

Recognition

* stock
* transaction

---

# Pattern 20) DP on Strings

Examples

* LCS
* Edit Distance
* Distinct Subsequences
* Wildcard Matching

Recognition

* two strings
* transformation

---

# Space Optimization

Sometimes only previous row needed.

Example

Instead of

```
dp[n]
```

Use

```python
prev

curr
```

Example

Fibonacci

```python
a,b = 0,1

for _ in range(n):
    a,b = b,a+b
```

Space

```
O(1)
```

---

# DP Recognition Guide

| Problem Type | Pattern |
|-------------|---------|
| Count ways | Fibonacci DP |
| Maximum sum | House Robber |
| Minimum coins | Coin Change |
| Count combinations | Coin Change II |
| Longest sequence | LIS |
| Two strings | LCS |
| Convert strings | Edit Distance |
| Subset | Knapsack |
| Equal partition | Subset Sum DP |
| Grid paths | Grid DP |
| Palindrome | Interval DP |
| Stock | State Machine DP |
| Tree | Tree DP |
| Visit all nodes | Bitmask DP |

---

# Common DP Problems

Easy

* Climbing Stairs
* Min Cost Climbing Stairs
* House Robber
* Fibonacci

Medium

* Coin Change
* Coin Change II
* Longest Increasing Subsequence
* Partition Equal Subset Sum
* Decode Ways
* Unique Paths
* Minimum Path Sum
* Longest Common Subsequence

Hard

* Edit Distance
* Burst Balloons
* Distinct Subsequences
* Regular Expression Matching
* Wildcard Matching

---

# Master Notes

## 1) DP = Cache Results

Never solve the same state twice.

---

## 2) Every DP needs a state

Always ask

"What does dp[i] represent?"

---

## 3) Transition is everything

Most interview questions are solved after identifying:

```
Current answer depends on which previous states?
```

---

## 4) Base Case matters

Wrong base case

↓

Whole DP becomes wrong.

---

## 5) Bottom Up usually faster

Recursion

↓

Memoization

↓

Tabulation

↓

Space Optimization

---

# DP State Cheat Sheet

| Pattern | State |
|----------|-------|
| Fibonacci | dp[i] |
| House Robber | dp[i] |
| LIS | dp[i] |
| LCS | dp[i][j] |
| Edit Distance | dp[i][j] |
| Knapsack | dp[item][capacity] |
| Grid | dp[row][col] |
| Interval | dp[left][right] |
| Tree | dfs(node) |
| Bitmask | dp[mask][node] |

---

# Interview Tips (VERY IMPORTANT)

## Ask Yourself These Questions

1. What is the state?
2. What are the choices?
3. What is the recurrence?
4. What is the base case?
5. Can I optimize space?

If you answer these five questions, you've solved 90% of DP interview problems.

---

# One-Line Memory Trick

**If the problem asks for maximum, minimum, longest, shortest, or number of ways—and recursion repeats the same states—think Dynamic Programming.**

---

# Pro Level Insight (VERY IMPORTANT)

| Situation | Technique |
|-----------|-----------|
| Count ways | DP |
| Maximum / Minimum | DP |
| Grid path | 2D DP |
| Two strings | LCS DP |
| Subset problems | Knapsack DP |
| Stock problems | State Machine DP |
| Interval splitting | Interval DP |
| Visit all states | Bitmask DP |
| Tree optimization | Tree DP |
| Huge recursion | Memoization |
| Iterative optimization | Tabulation |
| Memory optimization | Rolling Array |