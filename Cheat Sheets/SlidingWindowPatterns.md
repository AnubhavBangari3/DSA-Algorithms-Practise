# Sliding Window Patterns (CP + Interview Guide)

This repository contains essential **Sliding Window patterns** used in Competitive Programming and technical interviews.

Each pattern includes:
- When to use
- Core idea
- Code implementation (Python)
- Fast recognition notes
- Interview and CP intuition

---

# What is Sliding Window?

Sliding Window is used when the problem involves:

- Subarrays
- Substrings
- Contiguous sequences
- Optimizing brute force over ranges

Instead of recalculating every range again and again, we maintain a **window** and move it efficiently.

---

# When to Think of Sliding Window

Use Sliding Window when you see words like:

- longest substring
- smallest subarray
- maximum sum of subarray
- count of subarrays
- contiguous part of array
- continuous sequence
- at most k
- exactly k
- no repeating characters

---

# 🧩 Main Types of Sliding Window

1. **Fixed Size Window**
   - Window size is already given, usually `k`

2. **Variable Size Window**
   - Window expands and shrinks based on condition

3. **Window + HashMap/Set**
   - Used when frequency, uniqueness, duplicates, or character tracking is needed

4. **Exactly K Problems**
   - Usually solved using:
   - `exactly(k) = atMost(k) - atMost(k-1)`

---

# 1) Fixed Size Window — Maximum Sum Subarray of Size K

### When to use
- Window size is fixed
- Need max/min/sum over every subarray of size `k`

### Key Idea
Compute first window, then slide by:
- remove left element
- add new right element

```python
def max_sum_subarray(nums, k):
    n = len(nums)
    if n < k:
        return -1

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, n):
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Why this works
Instead of calculating sum of every subarray again, we update the previous window in O(1).

### Complexity
- Time: O(n)
- Space: O(1)

---

# 2) Fixed Size Window — First Negative Number in Every Window

### When to use
- Fixed window
- Need special element info in every window

### Key Idea
Maintain useful candidates for current window.

```python
from collections import deque

def first_negative_in_window(nums, k):
    q = deque()
    result = []

    for i in range(len(nums)):
        if nums[i] < 0:
            q.append(i)

        # Remove elements outside the window
        while q and q[0] <= i - k:
            q.popleft()

        # Start recording once first window is formed
        if i >= k - 1:
            if q:
                result.append(nums[q[0]])
            else:
                result.append(0)

    return result
```

### Complexity
- Time: O(n)
- Space: O(k)

---

# 3) Variable Size Window — Longest Substring Without Repeating Characters

### When to use
- Substring
- Unique characters
- Longest valid window

### Key Idea
Expand right pointer.
If duplicate appears, shrink from left until valid again.

```python
def longest_substring_without_repeating(s):
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

### Recognition
Whenever question says:
- longest substring
- without repeating
- unique characters

This pattern is one of the first things to try.

### Complexity
- Time: O(n)
- Space: O(n)

---

# 4) Variable Size Window — Smallest Subarray With Sum Greater Than or Equal to Target

### When to use
- Minimum length
- Contiguous subarray
- Positive numbers usually

### Key Idea
Expand until condition becomes valid.
Then shrink to find minimum valid window.

```python
def min_subarray_len(target, nums):
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
```

### Important Note
This direct variable window approach works properly when numbers are non-negative.

### Complexity
- Time: O(n)
- Space: O(1)

---

# 5) Variable Size Window — Longest Subarray With Sum Less Than or Equal to K

### When to use
- Longest valid subarray
- Condition-based shrinking
- Usually non-negative array

### Key Idea
Keep expanding while valid, shrink when invalid.

```python
def longest_subarray_sum_at_most_k(nums, k):
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(len(nums)):
        curr_sum += nums[right]

        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Complexity
- Time: O(n)
- Space: O(1)

---

# 6) Sliding Window + Frequency Map — Permutation in String

### When to use
- Need to check whether one string’s permutation exists in another
- Frequency comparison
- Fixed-size window on string

### Key Idea
Window length should match pattern length.
Track frequencies efficiently.

```python
from collections import Counter

def check_inclusion(s1, s2):
    need = Counter(s1)
    window = Counter()
    k = len(s1)

    for i in range(len(s2)):
        window[s2[i]] += 1

        if i >= k:
            left_char = s2[i - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        if window == need:
            return True

    return False
```

### Complexity
- Time: O(n * alphabet_check) in practical terms acceptable
- Space: O(alphabet)

---

# 7) Sliding Window + HashMap — Longest Repeating Character Replacement

### When to use
- At most `k` replacements allowed
- Need longest valid window

### Key Idea
Window is valid if:
`window_size - max_frequency <= k`

```python
from collections import defaultdict

def character_replacement(s, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Interview Insight
This is a very important pattern:
- maintain frequency
- maintain validity formula
- shrink only when invalid

### Complexity
- Time: O(n)
- Space: O(1) for uppercase English letters, otherwise O(n)

---

# 8) Sliding Window + Count Distinct — Longest Substring With At Most K Distinct Characters

### When to use
- At most K distinct
- Frequency + shrink logic

### Key Idea
Track frequency of characters.
If distinct count exceeds `k`, shrink.

```python
from collections import defaultdict

def longest_substring_k_distinct(s, k):
    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
```

### Complexity
- Time: O(n)
- Space: O(k) or O(n)

---

# 9) Count Subarrays With At Most K Distinct Integers

### When to use
- Counting valid subarrays
- At most / exactly k distinct

### Key Idea
For each `right`, all subarrays ending at `right` and starting from `left` to `right` are valid.

```python
from collections import defaultdict

def at_most_k_distinct(nums, k):
    count = defaultdict(int)
    left = 0
    result = 0

    for right in range(len(nums)):
        count[nums[right]] += 1

        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        result += right - left + 1

    return result
```

### Complexity
- Time: O(n)
- Space: O(k)

---

# 10) Count Subarrays With Exactly K Distinct Integers

### When to use
- Exactly K distinct
- Counting problem

### Key Idea
A famous trick:

```python
exactly_k = at_most_k(k) - at_most_k(k - 1)
```

```python
from collections import defaultdict

def at_most(nums, k):
    count = defaultdict(int)
    left = 0
    result = 0

    for right in range(len(nums)):
        count[nums[right]] += 1

        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        result += right - left + 1

    return result

def subarrays_with_k_distinct(nums, k):
    return at_most(nums, k) - at_most(nums, k - 1)
```

### Interview Gold Point
Whenever you see:
- exactly k distinct
- exact count with sliding window

Think of:
- at most k
- at most k-1
- subtract

### Complexity
- Time: O(n)
- Space: O(k)

---

# 11) Minimum Window Substring

### When to use
- Need smallest valid substring containing all required characters

### Key Idea
Expand until window satisfies requirement.
Then shrink while still valid.

```python
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    need = Counter(t)
    window = {}
    required = len(need)
    formed = 0
    left = 0
    min_len = float('inf')
    ans = (0, 0)

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right)

            left_char = s[left]
            window[left_char] -= 1

            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return "" if min_len == float('inf') else s[ans[0]:ans[1] + 1]
```

### Complexity
- Time: O(n)
- Space: O(n)

---

# 12) Sliding Window Maximum

### When to use
- Need maximum of every window of size `k`

### Key Idea
Use deque to keep useful elements in decreasing order.

```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### Why deque?
It helps us keep the best candidate at front in O(1).

### Complexity
- Time: O(n)
- Space: O(k)

---

# Quick Recognition Guide

- Fixed length `k` given → Fixed Sliding Window
- Longest/Smallest valid contiguous part → Variable Sliding Window
- Unique / duplicate / frequency → Window + Set/Map
- At most k distinct → Frequency map + shrink
- Exactly k distinct → `atMost(k) - atMost(k-1)`
- Maximum in every window → Deque
- Smallest substring containing pattern → Expand + shrink + frequency map

---

# Master Notes for Competitive Programming

## 1) Sliding Window works mostly on contiguous ranges
If the problem is about:
- subsequence → maybe not sliding window
- subset → not sliding window
- subarray / substring → strong chance of sliding window

## 2) Variable window usually follows this template

```python
def sliding_window_template(arr):
    left = 0

    for right in range(len(arr)):
        # 1. Expand the window
        # add arr[right]

        while window_is_invalid:
            # 2. Shrink the window
            # remove arr[left]
            left += 1

        # 3. Update answer
```

## 3) Counting problems often use this formula

```python
result += right - left + 1
```

Because if current window `[left ... right]` is valid, then all subarrays ending at `right`
and starting anywhere from `left` to `right` are also valid.

## 4) Exactly K is rarely solved directly
Usually solve:
- at most k
- at most k - 1
- subtract

## 5) For negative numbers, normal sliding window may fail
For example:
- smallest/longest subarray with sum target

Why?
Because shrinking or expanding does not behave monotonically with negatives.

In such cases, prefix sum + hashmap / deque may be needed.

---

# Common CP / Interview Problems Based on Sliding Window

- Maximum sum subarray of size k
- First negative number in every window
- Longest substring without repeating characters
- Longest substring with at most k distinct characters
- Longest repeating character replacement
- Permutation in string
- Minimum window substring
- Count subarrays with at most k distinct
- Count subarrays with exactly k distinct
- Sliding window maximum
- Fruit into baskets
- Binary subarrays with sum
- Number of nice subarrays

---

# Final Summary Table

| Pattern | Use Case | Core Idea |
|--------|----------|----------|
| Fixed Window Sum | Size k subarray | Add new, remove old |
| First Negative | Fixed window special element | Queue useful candidates |
| Longest Unique Substring | No duplicates | Expand + shrink set |
| Minimum Length Subarray | Smallest valid range | Shrink while valid |
| At Most K Distinct | Distinct count limited | Frequency map |
| Exactly K Distinct | Exact count | atMost(k) - atMost(k-1) |
| Character Replacement | At most k changes | Window size - maxFreq |
| Minimum Window Substring | Smallest covering window | Need vs window count |
| Sliding Window Maximum | Max in every window | Monotonic deque |

---

# Final Intuition

Sliding Window is not just one technique.

It is a family of patterns where you:

- maintain a valid range
- move pointers efficiently
- avoid recomputing from scratch

If brute force is checking all subarrays like this:

```python
for i in range(n):
    for j in range(i, n):
        # process subarray
```

then there is a strong chance Sliding Window can optimize it.

---

# One-Line Memory Trick

**If the problem says contiguous + optimize range + move efficiently, think Sliding Window first.**