
# Two Pointers Patterns (CP + Interview Guide)

This repository contains essential **Two Pointers patterns** used in Competitive Programming and technical interviews.

Each pattern includes:
- When to use
- Core idea
- Code implementation (Python)
- Intuition for quick understanding

---

# 1) Opposite Direction (Classic Two Sum Sorted)

### When to use
- Array is sorted
- Need to find a pair with given sum

### Key Idea
Start one pointer from left and one from right, shrink space.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
````

---

# 2) Remove Duplicates (In-Place)

### When to use

* Sorted array
* Need unique elements in-place

### Key Idea

Use slow pointer to track position of unique elements.

```python
def remove_duplicates(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

---

# 3) Move Zeroes

### When to use

* Rearranging elements while maintaining order

### Key Idea

Push non-zero elements forward.

```python
def move_zeroes(nums):
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

---

# 4) Container With Most Water

### When to use

* Max area / optimization with two ends

### Key Idea

Move the pointer with smaller height.

```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        max_area = max(max_area, h * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

---

# 5) 3 Sum (Very Important)

### When to use

* Triplets / combinations
* Sorted array + avoid duplicates

### Key Idea

Fix one element, use two pointers for remaining.

```python
def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
```

---

# 6) Sliding Window (Variable Size)

### When to use

* Subarray / substring problems
* Condition-based shrinking

### Key Idea

Expand right pointer, shrink left when condition breaks.

```python
def longest_substring_without_repeating(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

# 7) Fixed Size Sliding Window

### When to use

* Fixed size window (k)

### Key Idea

Maintain window of size k and update result.

```python
def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

# 8) Partition (Dutch National Flag)

### When to use

* 3 categories (0,1,2)
* Sorting without extra space

```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

---

# 9) Palindrome Check

### When to use

* String validation problems

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

---

# 10) Merge Two Sorted Arrays

### When to use

* Merge operations
* Already sorted arrays

```python
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
```

---

#  Quick Recognition Guide

* Sorted + pair → Opposite pointers
* Unique elements → Slow/Fast pointer
* Rearrangement → Swap with slow pointer
* Triplets → Fix + two pointers
* Subarray → Sliding window
* Fixed size → Window size k
* 3 categories → Dutch flag
* String → Left/right compare
* Merge → Backward merge

---

# Key Principle

Two pointers work when:

```
Search space can be reduced using relative movement
```

You either:

* Move both pointers
* Move one pointer based on condition

---

# Optimization Insight

If brute force is:

```python
for i in range(n):
    for j in range(i+1, n):
```

You can likely optimize using Two Pointers.

---

# Final Summary

| Pattern           | Use Case          | Core Idea            |
| ----------------- | ----------------- | -------------------- |
| Two Sum Sorted    | Pair sum          | Left + Right         |
| Remove Duplicates | Unique elements   | Slow/Fast            |
| Move Zeroes       | Rearrangement     | Swap forward         |
| Container Water   | Max area          | Move smaller pointer |
| 3 Sum             | Triplets          | Fix + two pointers   |
| Sliding Window    | Subarray problems | Expand + shrink      |
| Fixed Window      | Size k            | Rolling sum          |
| Dutch Flag        | 3 categories      | Partition            |
| Palindrome        | String check      | Compare ends         |
| Merge Arrays      | Sorted merge      | Backward fill        |

---

````

---



---


---

````
