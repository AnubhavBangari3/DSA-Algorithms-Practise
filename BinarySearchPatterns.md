
# Binary Search Patterns (CP + Interview Guide)

This repository contains essential **Binary Search patterns** used in Competitive Programming and technical interviews.

Each pattern includes:
- When to use
- Core idea
- Code implementation (Python)
- Intuition for quick understanding

---

# 1) Basic Binary Search

### When to use
- The array is sorted
- You need to find an exact target value

### Key Idea
Reduce the search space by half in each iteration.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
````

---

# 2) Lower Bound

### When to use

* Find the first index where value is **greater than or equal to target**
* Insert position problems
* Range queries

### Key Idea

Find the first valid position that satisfies the condition.

```python
def lower_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 3) Upper Bound

### When to use

* Find the first index where value is **strictly greater than target**
* Count occurrences

### Key Idea

Identify the boundary where elements become greater than the target.

```python
def upper_bound(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

### Note

```python
count = upper_bound(nums, target) - lower_bound(nums, target)
```

---

# 4) First Occurrence

### When to use

* Sorted array with duplicate elements
* Need the first occurrence of a target

### Key Idea

Continue searching towards the left even after finding the target.

```python
def first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

# 5) Last Occurrence

### When to use

* Sorted array with duplicate elements
* Need the last occurrence of a target

### Key Idea

Continue searching towards the right after finding the target.

```python
def last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

# 6) Binary Search on Answer (Most Important)

### When to use

* Problems involving:

  * Minimum value
  * Maximum value
  * Capacity, speed, time, distance

### Key Idea

Search over the answer space instead of the array.

---

## Template (Minimize)

```python
def binary_search_min_answer(low, high):
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if is_possible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
```

---

## Template (Maximize)

```python
def binary_search_max_answer(low, high):
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if is_possible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans
```

---

# Example: Koko Eating Bananas

```python
def minEatingSpeed(piles, h):

    def canEat(speed):
        total_hours = 0
        for bananas in piles:
            total_hours += (bananas + speed - 1) // speed
        return total_hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2

        if canEat(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

---

# 7) Peak Element

### When to use

* Array has increasing and decreasing patterns
* Need to find a peak element

```python
def findPeak(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left
```

---

# 8) Search in Rotated Sorted Array

### When to use

* Array was sorted but then rotated

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

---

# 9) Missing Number (Index-Based)

### When to use

* Sorted array where `nums[i] == i` pattern breaks

```python
def missingNumber(nums):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == mid:
            left = mid + 1
        else:
            right = mid - 1

    return left
```

---

# 10) Square Root using Binary Search

### When to use

* Find integer square root
* No array involved

```python
def sqrt(x):
    left, right = 0, x
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans
```

---

# Quick Recognition Guide

* Sorted + exact target → Basic Binary Search
* First ≥ target → Lower Bound
* First > target → Upper Bound
* Duplicates → First/Last Occurrence
* Min/Max optimization → Binary Search on Answer
* Peak problems → Compare adjacent elements
* Rotated array → One half is always sorted
* Index mismatch → Missing number pattern

---

# 💡 Key Principle

Binary Search works on **monotonic conditions**:

```
False False False True True True
or
True True True False False False
```

Your goal is to find the boundary.

---

# Optimization Insight

If a brute-force solution looks like:

```python
for x in range(low, high + 1):
    if condition(x):
        return x
```

You can likely optimize it using Binary Search.

---

# Final Summary

| Pattern          | Use Case             | Core Idea            |
| ---------------- | -------------------- | -------------------- |
| Basic BS         | Exact target         | Reduce search space  |
| Lower Bound      | First ≥ target       | Find insertion point |
| Upper Bound      | First > target       | Range/count          |
| First Occurrence | Duplicates           | Search left          |
| Last Occurrence  | Duplicates           | Search right         |
| BS on Answer Min | Smallest valid value | Move left if valid   |
| BS on Answer Max | Largest valid value  | Move right if valid  |
| Peak Element     | Mountain pattern     | Compare neighbors    |
| Rotated Array    | Sorted + rotated     | One half sorted      |
| Missing Number   | Index mismatch       | Detect boundary      |
| Square Root      | Numeric search       | Largest valid square |

---

```

---


```
