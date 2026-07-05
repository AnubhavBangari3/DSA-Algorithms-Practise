# Heap (Priority Queue) Patterns (CP + Interview Guide)

This guide covers **Heap / Priority Queue patterns** used in Competitive Programming and interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is a Heap?

A Heap is a **complete binary tree** that allows efficient access to the smallest or largest element.

Python provides a **Min Heap** using:

```python
import heapq
```

Default:

```python
heap[0]
```

is always the **smallest** element.

---

# When to Think of Heap

Use Heap when you see:

* kth largest / smallest
* top k
* priority
* merge sorted lists
* stream of numbers
* scheduling
* repeatedly need smallest/largest
* shortest path
* greedy extraction

---

# Heap Operations

```python
import heapq

heap = []

heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

smallest = heapq.heappop(heap)

top = heap[0]
```

### Complexity

| Operation | Complexity |
|------------|------------|
| Push | O(log n) |
| Pop | O(log n) |
| Peek | O(1) |
| Heapify | O(n) |

---

# Max Heap in Python

Python only supports Min Heap.

Use negative values.

```python
import heapq

heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -5)
heapq.heappush(heap, -20)

largest = -heapq.heappop(heap)
```

---

# 1) Kth Largest Element (VERY IMPORTANT)

### When to use

* kth largest
* kth smallest
* don't sort entire array

### Code

```python
import heapq

def findKthLargest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
```

### Recognition

* kth largest
* top k
* keep only k elements

### Complexity

Time: O(n log k)

Space: O(k)

---

# 2) Top K Frequent Elements

### When to use

* frequency
* top k frequent

### Code

```python
from collections import Counter
import heapq

def topKFrequent(nums, k):

    freq = Counter(nums)

    heap = []

    for num, count in freq.items():

        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]
```

### Trick

Store

```python
(frequency, value)
```

inside heap.

---

# 3) Merge K Sorted Lists

### When to use

* multiple sorted arrays
* merge efficiently

### Code

```python
import heapq

def merge_lists(lists):

    heap = []

    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    answer = []

    while heap:

        value, list_id, index = heapq.heappop(heap)

        answer.append(value)

        if index + 1 < len(lists[list_id]):
            heapq.heappush(
                heap,
                (
                    lists[list_id][index + 1],
                    list_id,
                    index + 1
                )
            )

    return answer
```

### Complexity

O(N log K)

---

# 4) K Closest Points

### When to use

* nearest points
* closest values

### Code

```python
import heapq

def kClosest(points, k):

    heap = []

    for x, y in points:

        dist = x*x + y*y

        heapq.heappush(heap, (-dist, [x, y]))

        if len(heap) > k:
            heapq.heappop(heap)

    return [point for dist, point in heap]
```

---

# 5) Heap for Running Median

### When to use

* stream
* median after every insertion

### Idea

Maintain

* Max Heap (left)
* Min Heap (right)

Largest on left

Smallest on right

Balance sizes.

This gives

Median in O(1)

Insertion O(log n)

---

# 6) Task Scheduler / CPU Scheduling

### When to use

* highest priority task
* scheduling
* greedy execution

Heap stores

```python
(priority, task)
```

Repeatedly execute highest priority.

---

# 7) Dijkstra's Algorithm

### When to use

* shortest path
* weighted graph

Heap stores

```python
(distance, node)
```

Always process node having minimum distance.

---

# 8) Meeting Rooms / Interval Problems

### When to use

* meeting rooms
* interval scheduling

Heap stores ending times.

Whenever earliest ending meeting finishes,

reuse that room.

---

# Quick Recognition Guide

| Problem Type | Use |
|--------------|-----|
| kth largest | Heap |
| kth smallest | Heap |
| top k | Heap |
| merge k sorted lists | Heap |
| running median | Two Heaps |
| scheduling | Heap |
| shortest path | Heap |
| priority | Heap |

---

# Master Notes

## 1) Heap always gives smallest element quickly

```python
heap[0]
```

is always minimum.

---

## 2) Max Heap

Python has no Max Heap.

Use

```python
-value
```

---

## 3) K Largest Trick

Instead of storing all numbers

Store only

```
k numbers
```

Whenever heap exceeds

```
k
```

remove smallest.

---

## 4) Heapify

Instead of pushing one by one

```python
heapq.heapify(nums)
```

Builds heap in

```
O(n)
```

---

## 5) Heap vs Sorting

Sorting

```
O(n log n)
```

Heap

```
O(n log k)
```

when only Top K is needed.

---

# Common Problems

* Kth Largest Element
* K Closest Points
* Top K Frequent Elements
* Merge K Sorted Lists
* Find Median from Data Stream
* Task Scheduler
* Meeting Rooms II
* Dijkstra
* IPO
* Smallest Range Covering K Lists

---

# Final Summary Table

| Pattern | Use Case | Idea |
|----------|----------|------|
| Min Heap | smallest element | root minimum |
| Max Heap | largest element | negative values |
| Kth Largest | top k | keep heap size k |
| Top K Frequent | frequency | (count, value) |
| Merge K Lists | sorted lists | heap of first elements |
| Running Median | stream | two heaps |
| Scheduling | priority | execute smallest/largest priority |
| Dijkstra | graph | minimum distance first |

---

# Heap vs Sorting

| Heap | Sorting |
|------|---------|
| O(log n) insertion | O(n log n) |
| Dynamic | Static |
| Best for Top K | Best for full ordering |
| Streaming friendly | Not streaming friendly |

---

# Heap vs Queue vs Stack

| Data Structure | Removal |
|---------------|---------|
| Stack | Last In First Out |
| Queue | First In First Out |
| Heap | Highest / Lowest Priority |

---

# Final Intuition

Heap is about

* always getting smallest/largest quickly
* Top K problems
* scheduling
* greedy algorithms
* streaming data

---

# One-Line Memory Trick

**If the problem repeatedly asks for the smallest/largest element or Top K → think Heap.**

---

## Pro Level Insight (VERY IMPORTANT)

| Situation | Technique |
|-----------|-----------|
| Top K | Min Heap |
| Kth Largest | Min Heap |
| Kth Smallest | Max Heap |
| Running Median | Two Heaps |
| Merge Sorted Lists | Heap |
| Scheduling | Heap |
| Weighted Shortest Path | Heap |
| Dynamic Stream | Heap |

---
```