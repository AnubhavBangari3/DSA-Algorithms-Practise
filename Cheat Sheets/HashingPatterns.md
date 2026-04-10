
---

# Hashing (Map / Set) Patterns (CP + Interview Guide)

This repository contains essential **Hashing patterns (Map & Set)** used in Competitive Programming and technical interviews.

Each pattern includes:

* When to use
* Core idea
* Code implementation (Python)
* Intuition for quick understanding

---

# 1) Frequency Count (Most Basic)

### When to use

* Count occurrences of elements
* Check duplicates
* Character frequency problems

### Key Idea

Use a hashmap (dictionary) to store counts.

```python
from collections import Counter

def frequency_count(arr):
    freq = Counter(arr)
    return freq
```

---

# 2) Detect Duplicates

### When to use

* Check if array/string contains duplicates

### Key Idea

Use a set to track seen elements.

```python
def has_duplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
```

---

# 3) Two Sum (Classic)

### When to use

* Find two numbers with a given sum

### Key Idea

Store previously seen values in a hashmap.

```python
def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[num] = i

    return []
```

---

# 4) Prefix Sum + HashMap

### When to use

* Subarray sum problems
* Count subarrays with given sum

### Key Idea

Store prefix sums in hashmap.

```python
def subarray_sum(nums, k):
    prefix_sum = 0
    hashmap = {0: 1}
    count = 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in hashmap:
            count += hashmap[prefix_sum - k]

        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count
```

---

# 5) Longest Subarray with Sum K

### When to use

* Need maximum length subarray

### Key Idea

Store first occurrence of prefix sum.

```python
def longest_subarray(nums, k):
    prefix_sum = 0
    hashmap = {}
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum - k in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum - k])

        if prefix_sum not in hashmap:
            hashmap[prefix_sum] = i

    return max_len
```

---

# 6) Longest Substring Without Repeating Characters

### When to use

* String + no duplicates
* Sliding window + set/map

### Key Idea

Expand window and shrink when duplicate appears.

```python
def longest_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

# 7) Anagram Check

### When to use

* Check if two strings are anagrams

### Key Idea

Compare frequency maps.

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

---

# 8) Group Anagrams

### When to use

* Group words with same characters

### Key Idea

Use sorted string as key.

```python
from collections import defaultdict

def group_anagrams(strs):
    hashmap = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        hashmap[key].append(word)

    return list(hashmap.values())
```

---

# 9) Top K Frequent Elements

### When to use

* Find most frequent elements

### Key Idea

Count + sort or heap

```python
from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [num for num, _ in freq.most_common(k)]
```

---

# 10) First Non-Repeating Character

### When to use

* Find unique element in order

### Key Idea

Count first, then scan again

```python
from collections import Counter

def first_unique_char(s):
    freq = Counter(s)

    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i

    return -1
```

---

# 11) Intersection of Two Arrays

### When to use

* Common elements

### Key Idea

Use set intersection

```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```

---

# 12) Subarray with Equal 0s and 1s

### When to use

* Binary array problems

### Key Idea

Convert 0 → -1 and use prefix sum

```python
def equal_0_1(nums):
    prefix_sum = 0
    hashmap = {0: -1}
    max_len = 0

    for i, num in enumerate(nums):
        prefix_sum += -1 if num == 0 else 1

        if prefix_sum in hashmap:
            max_len = max(max_len, i - hashmap[prefix_sum])
        else:
            hashmap[prefix_sum] = i

    return max_len
```

---

# Quick Recognition Guide

* Counting → Frequency Map
* Duplicate detection → Set
* Pair sum → HashMap (Two Sum)
* Subarray sum → Prefix + HashMap
* Longest substring → Sliding Window + Set
* Anagram → Sorted or Counter
* Grouping → HashMap with key transformation
* Top K → Frequency + Heap/Sort
* Binary tricks → Prefix sum transformation

---

# Key Principle

Hashing works best when:

* You need **O(1) lookup**
* You want to **avoid nested loops**
* You can trade **space for time**

---

# Optimization Insight

If brute force looks like:

```python
for i in range(n):
    for j in range(i):
        # check condition
```

Try replacing inner loop using **hashmap or set**

---

# Final Summary

| Pattern          | Use Case           | Core Idea              |
| ---------------- | ------------------ | ---------------------- |
| Frequency Count  | Count elements     | Store counts           |
| Duplicates       | Check repetition   | Use set                |
| Two Sum          | Pair problems      | Store complement       |
| Prefix Sum       | Subarray sum       | Store cumulative sum   |
| Longest Subarray | Max length         | Store first occurrence |
| Sliding Window   | Substring problems | Expand/shrink          |
| Anagram          | String comparison  | Compare counts         |
| Grouping         | Categorization     | Key transformation     |
| Top K            | Frequency ranking  | Sort/Heap              |
| Intersection     | Common elements    | Set ops                |

---

