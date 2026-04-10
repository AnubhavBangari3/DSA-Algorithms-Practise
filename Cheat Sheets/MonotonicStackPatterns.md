Absolutely — here is the **same GitHub-ready format** for **Stack / Monotonic Stack in Competitive Programming** based on the style you shared earlier. 

You can save this as:

```md
monotonic_stack_patterns.md
```

---

# Monotonic Stack Patterns (CP + Interview Guide)

This guide covers **Monotonic Stack patterns** used in Competitive Programming and interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is a Monotonic Stack?

A **Monotonic Stack** is a stack that keeps elements in a specific order:

* **Increasing stack** → elements stay increasing
* **Decreasing stack** → elements stay decreasing

It is mainly used to find:

* next greater element
* next smaller element
* previous greater element
* previous smaller element

efficiently in **O(n)** time.

---

# When to Think of Monotonic Stack

Use Monotonic Stack when you see:

* next greater / smaller
* previous greater / smaller
* nearest greater / smaller
* stock span
* histogram
* trapping rain water
* remove useless elements while maintaining order
* range contribution problems

---

# Core Idea

While processing each element:

* keep popping from stack while stack top is no longer useful
* then current stack top gives the answer
* then push current element

That is why every element is pushed and popped at most once.

So total complexity is usually:

```python
O(n)
```

---

# 1) Next Greater Element

### When to use

* Need nearest greater element on the right

### Code

```python
def next_greater_element(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []  # store indices

    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = nums[stack[-1]]

        stack.append(i)

    return ans
```

### Complexity

* Time: O(n)
* Space: O(n)

### Recognition

* “next greater on right”
* “first larger element after current”

---

# 2) Next Smaller Element

### When to use

* Need nearest smaller element on the right

### Code

```python
def next_smaller_element(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []  # store indices

    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()

        if stack:
            ans[i] = nums[stack[-1]]

        stack.append(i)

    return ans
```

---

# 3) Previous Greater Element

### When to use

* Need nearest greater element on the left

### Code

```python
def previous_greater_element(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()

        if stack:
            ans[i] = nums[stack[-1]]

        stack.append(i)

    return ans
```

---

# 4) Previous Smaller Element

### When to use

* Need nearest smaller element on the left

### Code

```python
def previous_smaller_element(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []

    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()

        if stack:
            ans[i] = nums[stack[-1]]

        stack.append(i)

    return ans
```

---

# 5) Stock Span Problem

### When to use

* Need count of consecutive smaller or equal elements on left
* Common interview question

### Code

```python
def stock_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []  # store indices

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span
```

### Key Idea

Find previous greater element.
Then distance gives span.

---

# 6) Largest Rectangle in Histogram

### When to use

* Histogram bars
* maximum area rectangle
* very famous interview pattern

### Code

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        curr_height = 0 if i == n else heights[i]

        while stack and heights[stack[-1]] > curr_height:
            h = heights[stack.pop()]
            left_smaller_index = stack[-1] if stack else -1
            width = i - left_smaller_index - 1
            max_area = max(max_area, h * width)

        stack.append(i)

    return max_area
```

### Recognition

* “largest rectangle”
* “max area in histogram”
* “expand until smaller boundary”

### Key Insight

For each bar, find:

* previous smaller
* next smaller

That bar becomes the minimum height in that width.

---

# 7) Maximal Rectangle in Binary Matrix

### When to use

* Rectangle of 1s in matrix
* 2D version of histogram

### Code

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        curr_height = 0 if i == n else heights[i]

        while stack and heights[stack[-1]] > curr_height:
            h = heights[stack.pop()]
            left_smaller = stack[-1] if stack else -1
            width = i - left_smaller - 1
            max_area = max(max_area, h * width)

        stack.append(i)

    return max_area


def maximal_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    n = len(matrix[0])
    heights = [0] * n
    ans = 0

    for row in matrix:
        for j in range(n):
            if row[j] == "1":
                heights[j] += 1
            else:
                heights[j] = 0

        ans = max(ans, largest_rectangle_area(heights))

    return ans
```

---

# 8) Trapping Rain Water

### When to use

* rain water between bars
* nearest greater boundaries
* can be solved using stack or two pointers

### Code

```python
def trap(height):
    stack = []
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            width = i - left - 1
            bounded_height = min(height[left], height[i]) - height[bottom]
            water += width * bounded_height

        stack.append(i)

    return water
```

### Key Insight

When a taller bar comes, it may close a container.

---

# 9) Daily Temperatures

### When to use

* next greater element with distance
* very common interview problem

### Code

```python
def daily_temperatures(temperatures):
    n = len(temperatures)
    ans = [0] * n
    stack = []  # indices

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            ans[prev] = i - prev

        stack.append(i)

    return ans
```

### Recognition

* “how many days until greater value”
* “distance to next greater”

---

# 10) Remove K Digits

### When to use

* need smallest / largest possible number after deletions
* greedy + monotonic stack combo

### Code

```python
def remove_k_digits(num, k):
    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = "".join(stack).lstrip("0")
    return result if result else "0"
```

### Key Insight

Keep number as small as possible from left to right.

---

# 11) Sum of Subarray Minimums

### When to use

* Need contribution of each element as minimum
* advanced monotonic stack pattern

### Code

```python
def sum_subarray_mins(arr):
    n = len(arr)
    mod = 10**9 + 7

    left = [0] * n
    right = [0] * n
    stack = []

    # distance to previous strictly smaller
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        if not stack:
            left[i] = i + 1
        else:
            left[i] = i - stack[-1]

        stack.append(i)

    stack = []

    # distance to next smaller or equal
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        if not stack:
            right[i] = n - i
        else:
            right[i] = stack[-1] - i

        stack.append(i)

    ans = 0
    for i in range(n):
        ans = (ans + arr[i] * left[i] * right[i]) % mod

    return ans
```

### Key Insight

Instead of generating all subarrays, count:

* in how many subarrays is `arr[i]` the minimum?

Contribution:

```python
arr[i] * left_choices * right_choices
```

---

# 12) Sum of Subarray Ranges

### When to use

* Need sum of `(max - min)` over all subarrays
* advanced CP pattern

### Idea

Compute:

```text
sum_of_subarray_maximums - sum_of_subarray_minimums
```

Both parts use monotonic stack contribution logic.

---

# Quick Recognition Guide

| Problem Type                         | Use             |
| ------------------------------------ | --------------- |
| Next greater/smaller                 | Monotonic Stack |
| Previous greater/smaller             | Monotonic Stack |
| Nearest boundary element             | Monotonic Stack |
| Histogram area                       | Monotonic Stack |
| Stock span                           | Monotonic Stack |
| Daily temperatures                   | Monotonic Stack |
| Contribution of min/max in subarrays | Monotonic Stack |

---

# Master Notes

## 1) Why is it O(n)?

Each element:

* pushed once
* popped once

So even if there is a while loop, total operations are still linear.

---

## 2) Increasing vs Decreasing Stack

### Increasing stack

Useful for:

* previous smaller
* next smaller

### Decreasing stack

Useful for:

* previous greater
* next greater

---

## 3) Store indices, not values

Most of the time we store **indices** because we need:

* actual value
* position
* width / distance

Example:

```python
stack.append(i)
```

not just:

```python
stack.append(nums[i])
```

---

## 4) Direction matters

To find:

* **next** element → often traverse from right to left, or resolve while going left to right
* **previous** element → usually traverse left to right

---

## 5) Strict vs non-strict comparison matters

These change duplicate handling:

```python
>
>=
<
<=
```

This is very important in contribution problems like:

* sum of subarray minimums
* sum of subarray maximums

---

# Common Problems

* Next Greater Element
* Next Greater Element II
* Daily Temperatures
* Stock Span
* Largest Rectangle in Histogram
* Maximal Rectangle
* Trapping Rain Water
* Sum of Subarray Minimums
* Sum of Subarray Ranges
* Remove K Digits

---

# Final Summary Table

| Pattern            | Use Case                          | Core Idea                |
| ------------------ | --------------------------------- | ------------------------ |
| Next Greater       | nearest greater on right          | decreasing stack         |
| Next Smaller       | nearest smaller on right          | increasing stack         |
| Previous Greater   | nearest greater on left           | decreasing stack         |
| Previous Smaller   | nearest smaller on left           | increasing stack         |
| Stock Span         | consecutive smaller/equal on left | previous greater         |
| Histogram          | max area rectangle                | previous + next smaller  |
| Daily Temperatures | distance to next greater          | stack of indices         |
| Rain Water         | bounded containers                | boundaries via stack     |
| Remove K Digits    | smallest number after deletions   | greedy + monotonic stack |
| Subarray Minimums  | contribution counting             | previous/next boundary   |

---

# Final Intuition

Monotonic Stack is about:

* keeping only useful candidates
* removing bad candidates immediately
* finding nearest valid boundary fast
* converting O(n²) search into O(n)

---

# One-Line Memory Trick

**If the problem says nearest greater/smaller, previous/next, span, histogram, or boundary → think Monotonic Stack**

---

## Pro Level Insight (VERY IMPORTANT)

| Situation                                   | Technique       |
| ------------------------------------------- | --------------- |
| Need nearest greater/smaller                | Monotonic Stack |
| Need previous/next boundary                 | Monotonic Stack |
| Need width using smaller boundaries         | Monotonic Stack |
| Need contribution of each element           | Monotonic Stack |
| Need min/max over all subarrays efficiently | Monotonic Stack |

---


