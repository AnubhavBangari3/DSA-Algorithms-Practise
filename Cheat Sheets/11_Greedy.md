# Greedy Patterns (CP + Interview Guide)

This guide covers **Greedy patterns** used in Competitive Programming and interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is Greedy?

Greedy means making the **best local choice at every step** hoping it leads to the global answer.

```text
At every step:
choose the option that looks best right now
```

---

# When to Think of Greedy

Use Greedy when you see:

* minimum / maximum
* intervals
* sorting + choosing
* jump / reach problem
* assign resources
* scheduling
* buy/sell
* choose optimal order
* “can we reach?”
* “minimum number of operations”

---

# Core Greedy Idea

```text
Sort / scan / choose best current option
```

Greedy usually works when:

```text
local optimal choice → global optimal answer
```

---

# 1) Greedy + Sorting

### When to use

* Need minimum/maximum answer
* Order can be rearranged
* Choosing smallest/largest first helps

### Example: Assign Cookies

```python
def find_content_children(g, s):
    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1

    return child
```

### Recognition

* “maximize number of satisfied”
* “assign”
* “minimum resources”
* sorting possible

### Complexity

* Time: O(n log n)
* Space: O(1)

---

# 2) Interval Greedy — Sort by End Time

### When to use

* Select maximum non-overlapping intervals
* Remove minimum overlapping intervals
* Meeting rooms / activity selection

### Key Idea

Pick the interval that **ends earliest**.

```python
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:
            count += 1
        else:
            prev_end = end

    return count
```

### Recognition

* intervals
* overlapping
* minimum removals
* maximum meetings
* non-overlapping

### Important Trick

```text
Sort by end time, not start time
```

---

# 3) Jump Game Greedy

### When to use

* Can reach end?
* Minimum jumps
* Maximum reachable index

### Example: Jump Game I

```python
def can_jump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

    return True
```

### Recognition

* jump
* reach last index
* maximum reachable distance
* array value = power/range

### Complexity

* Time: O(n)
* Space: O(1)

---

# 4) Jump Game II — Minimum Jumps

### When to use

* Need minimum jumps to reach end

### Code

```python
def jump(nums):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps
```

### Key Insight

Current range = one jump.

When range ends, take next jump.

---

# 5) Greedy with Min/Max Tracking

### When to use

* Track best value so far
* Buy/sell type problems
* Maximum profit

### Example: Best Time to Buy and Sell Stock

```python
def max_profit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit
```

### Recognition

* profit
* buy before sell
* max difference
* best previous value

---

# 6) Greedy + Heap

### When to use

* Need smallest/largest available option repeatedly
* Scheduling
* Minimum rooms
* CPU/task problems

### Example: Meeting Rooms II

```python
import heapq

def min_meeting_rooms(intervals):
    intervals.sort(key=lambda x: x[0])

    heap = []

    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)

        heapq.heappush(heap, end)

    return len(heap)
```

### Recognition

* minimum rooms
* active intervals
* earliest ending task
* scheduling resources

---

# 7) Gas Station Greedy

### When to use

* Circular route
* Need valid starting point

### Code

```python
def can_complete_circuit(gas, cost):
    total = 0
    tank = 0
    start = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff

        if tank < 0:
            start = i + 1
            tank = 0

    if total < 0:
        return -1

    return start
```

### Key Insight

If tank becomes negative at `i`, no index before `i` can be the answer.

---

# 8) Greedy + Two Pointers

### When to use

* Pair smallest with largest
* Minimize/maximize boats, pairs, resources

### Example: Boats to Save People

```python
def num_rescue_boats(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats
```

### Recognition

* pair people/items
* weight limit
* minimum number of groups
* sorted pairing

---

# 9) Greedy + Frequency Counting

### When to use

* Rearranging characters
* Minimum deletions
* Frequency constraints

### Example: Minimum Deletions to Make Character Frequencies Unique

```python
def min_deletions(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    used = set()
    deletions = 0

    for count in freq.values():
        while count > 0 and count in used:
            count -= 1
            deletions += 1

        used.add(count)

    return deletions
```

### Recognition

* frequency
* unique counts
* delete minimum
* rearrange characters

---

# 10) Greedy + Stack

### When to use

* Remove digits/chars to make smallest/largest result
* Lexicographically smallest answer

### Example: Remove K Digits

```python
def remove_k_digits(num, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    result = ''.join(stack).lstrip('0')

    return result if result else "0"
```

### Recognition

* remove k elements
* smallest number
* lexicographically smallest
* monotonic stack + greedy

---

# Quick Recognition Guide

| Problem Type           | Use                |
| ---------------------- | ------------------ |
| Maximum/minimum answer | Greedy             |
| Intervals overlap      | Sort by end time   |
| Can reach end          | Farthest reach     |
| Minimum jumps          | Range greedy       |
| Buy/sell profit        | Track min/max      |
| Assign resources       | Sorting            |
| Meeting rooms          | Heap               |
| Circular route         | Gas station greedy |
| Pair with limit        | Two pointers       |
| Remove k digits        | Greedy stack       |

---

# Master Notes

## 1) Greedy usually needs sorting

Many greedy problems become simple after sorting.

```python
intervals.sort(key=lambda x: x[1])
```

---

## 2) Intervals → think end time

For maximum non-overlapping intervals:

```text
Pick the interval that ends earliest
```

---

## 3) Jump Game → track farthest

```python
farthest = max(farthest, i + nums[i])
```

---

## 4) Buy/Sell → track best previous value

```python
min_price = min(min_price, price)
```

---

## 5) Heap helps when active choices change

Use heap when you need:

```text
smallest ending time / largest priority repeatedly
```

---

# Common Problems

* Assign Cookies
* Lemonade Change
* Best Time to Buy and Sell Stock
* Jump Game
* Jump Game II
* Gas Station
* Non-overlapping Intervals
* Minimum Number of Arrows to Burst Balloons
* Meeting Rooms II
* Boats to Save People
* Remove K Digits
* Partition Labels
* Task Scheduler
* Candy
* Queue Reconstruction by Height
* Minimum Deletions to Make Character Frequencies Unique

---

# Final Summary Table

| Pattern             | Use Case                     | Idea                      |
| ------------------- | ---------------------------- | ------------------------- |
| Sorting Greedy      | Assign / minimize / maximize | Sort and pick best        |
| Interval Greedy     | Non-overlap                  | Sort by end time          |
| Jump Greedy         | Reachability                 | Track farthest            |
| Range Greedy        | Minimum jumps                | Expand current range      |
| Min/Max Tracking    | Profit                       | Store best previous value |
| Heap Greedy         | Scheduling                   | Pick earliest/latest      |
| Gas Station         | Circular path                | Reset bad start           |
| Two Pointers Greedy | Pairing                      | Smallest + largest        |
| Frequency Greedy    | Unique counts                | Reduce duplicates         |
| Stack Greedy        | Smallest/largest result      | Remove bad previous       |

---

# Final Intuition

Greedy is about:

* making the best current choice
* avoiding unnecessary future work
* sorting to reveal the correct order
* proving why local choice is safe

---

# One-Line Memory Trick

**If problem asks minimum/maximum and choice at each step seems obvious → think Greedy.**

---

## Pro Level Insight (VERY IMPORTANT)

| Situation                 | Technique                   |
| ------------------------- | --------------------------- |
| Intervals + remove/select | Sort by end time            |
| Can reach index           | Farthest reach              |
| Minimum jumps             | Current range + farthest    |
| Assign smallest resource  | Sort + two pointers         |
| Active meetings/tasks     | Heap                        |
| Buy/sell once             | Track minimum               |
| Remove digits/chars       | Monotonic stack             |
| Circular route            | Reset start when tank fails |
| Pair under limit          | Sort + two pointers         |

---

# Greedy Proof Template

In interview, say this:

```text
At every step, I choose the option that gives the best immediate benefit.
This choice is safe because choosing anything worse cannot improve the future result.
So local optimal choice leads to global optimal answer.
```

---

# When Greedy Fails

Greedy may fail when:

* future choices depend heavily on current choice
* local best does not guarantee global best
* problem asks for all combinations
* need exact count of ways
* overlapping subproblems exist

Then think:

```text
Dynamic Programming
Backtracking
Graph Search
```

---

# Greedy vs DP

| Situation                    | Use               |
| ---------------------------- | ----------------- |
| Need best immediate choice   | Greedy            |
| Need try all possibilities   | DP / Backtracking |
| Choices overlap              | DP                |
| Need count number of ways    | DP                |
| Sorting makes answer obvious | Greedy            |

---

# Final Interview Line

Greedy works when:

```text
A locally optimal decision never hurts the global answer.
```
