

# 🚀 Prefix Sum Patterns (CP + Interview Guide)

This guide covers **Prefix Sum patterns** used in Competitive Programming and interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is Prefix Sum?

Prefix Sum helps you **precompute cumulative values** so that range queries become fast.

Instead of recalculating sum repeatedly, we store:

```text
prefix[i] = sum of elements from index 0 to i
```

---

# When to Think of Prefix Sum

Use Prefix Sum when you see:

* subarray sum
* range sum queries
* count of subarrays
* cumulative sum
* sum between indices
* prefix / suffix
* many queries on array

---

# Core Formula

```python
prefix[i] = prefix[i - 1] + nums[i]
```

To get sum from `L → R`:

```python
sum(L, R) = prefix[R] - prefix[L - 1]
```

---

# 1) Basic Prefix Sum — Range Sum Query

### When to use

* Multiple queries asking sum of subarray

### Code

```python
def build_prefix(nums):
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix


def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L - 1]
```

### Complexity

* Build: O(n)
* Query: O(1)

---

# 2) Subarray Sum Equals K (VERY IMPORTANT)

### When to use

* Count subarrays with given sum
* Array may contain negative numbers

### Key Idea

Use **prefix sum + hashmap**

```python
from collections import defaultdict

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]

        freq[prefix_sum] += 1

    return count
```

### Recognition

* “count subarrays”
* “sum = k”
* **negative numbers present**

### Complexity

* Time: O(n)
* Space: O(n)

---

# 3) Longest Subarray With Sum K

### When to use

* Need **maximum length**
* sum = k

### Code

```python
def longest_subarray_sum_k(nums, k):
    prefix_sum = 0
    index_map = {}
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum - k in index_map:
            max_len = max(max_len, i - index_map[prefix_sum - k])

        if prefix_sum not in index_map:
            index_map[prefix_sum] = i

    return max_len
```

### Key Insight

Store **first occurrence** of prefix sum.

---

# 4) Count Subarrays With Sum Divisible by K

### When to use

* sum % k = 0

### Code

```python
from collections import defaultdict

def subarrays_div_by_k(nums, k):
    prefix_sum = 0
    count = 0
    mod_map = defaultdict(int)
    mod_map[0] = 1

    for num in nums:
        prefix_sum += num
        mod = prefix_sum % k

        if mod < 0:
            mod += k

        count += mod_map[mod]
        mod_map[mod] += 1

    return count
```

### Trick

Same remainder → valid subarray

---

# 5) Prefix Sum + Binary Array (0/1)

### Example: Count subarrays with sum = goal

```python
def num_subarrays_with_sum(nums, goal):
    from collections import defaultdict

    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1
    count = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - goal in freq:
            count += freq[prefix_sum - goal]

        freq[prefix_sum] += 1

    return count
```

---

# 6) 2D Prefix Sum (Matrix)

### When to use

* Rectangle sum queries

### Build

```python
def build_2d_prefix(matrix):
    m, n = len(matrix), len(matrix[0])
    prefix = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            prefix[i+1][j+1] = (
                matrix[i][j]
                + prefix[i][j+1]
                + prefix[i+1][j]
                - prefix[i][j]
            )

    return prefix
```

### Query

```python
def query(prefix, r1, c1, r2, c2):
    return (
        prefix[r2+1][c2+1]
        - prefix[r1][c2+1]
        - prefix[r2+1][c1]
        + prefix[r1][c1]
    )
```

### Complexity

* Build: O(m*n)
* Query: O(1)

---

# 7) Prefix Sum + Sliding Window Combo

### Important Insight

When array has:

* only positive numbers → Sliding Window
* negative numbers → Prefix Sum

This is a **VERY IMPORTANT INTERVIEW POINT**

---

# Quick Recognition Guide

| Problem Type             | Use              |
| ------------------------ | ---------------- |
| Range sum queries        | Prefix Sum       |
| Count subarrays sum = k  | Prefix + HashMap |
| Negative numbers present | Prefix Sum       |
| Sum divisible by k       | Prefix mod       |
| Matrix sum queries       | 2D Prefix        |
| Binary array sum         | Prefix           |

---

# Master Notes

## 1) Prefix Sum avoids recomputation

Instead of:

```python
for i in range(n):
    for j in range(i, n):
        sum(nums[i:j])
```

Use prefix → O(1) query

---

## 2) HashMap trick

```python
if prefix_sum - k exists:
    count += freq[prefix_sum - k]
```

---

## 3) Why it works?

Because:

```text
prefix[j] - prefix[i] = k
→ prefix[j] - k = prefix[i]
```

---

## 4) Negative numbers → Sliding window fails

Use prefix sum instead

---

## 5) Store first occurrence for longest problems

```python
if prefix not in map:
    map[prefix] = index
```

---

# Common Problems

* Subarray Sum Equals K
* Longest Subarray Sum K
* Subarrays Divisible by K
* Binary Subarrays With Sum
* Range Sum Query
* Matrix Block Sum
* Continuous Subarray Sum

---

# Final Summary Table

| Pattern            | Use Case   | Idea                    |
| ------------------ | ---------- | ----------------------- |
| Basic Prefix       | Range sum  | prefix[R] - prefix[L-1] |
| Subarray Sum K     | Count      | prefix + hashmap        |
| Longest Subarray K | Max length | store first index       |
| Divisible by K     | mod trick  | same remainder          |
| Binary Array       | count      | prefix freq             |
| 2D Prefix          | matrix     | inclusion-exclusion     |

---

# Final Intuition

Prefix Sum is about:

* precomputing information
* answering queries instantly
* reducing nested loops

---

# One-Line Memory Trick

**If problem has “subarray + sum + many queries / negative numbers” → think Prefix Sum**

---

## Pro Level Insight (VERY IMPORTANT)

| Situation                | Technique        |
| ------------------------ | ---------------- |
| Positive numbers only    | Sliding Window   |
| Negative numbers present | Prefix Sum       |
| Count subarrays          | Prefix + HashMap |
| Exact sum                | Prefix           |
| Max/min length           | Prefix + Map     |

---

```

---


