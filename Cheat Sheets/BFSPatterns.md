
# Queue and BFS Patterns (CP + Interview Guide)

This guide covers Queue and BFS patterns used in Competitive Programming and interviews.

Each pattern includes:

* When to use
* Core idea
* Code (Python)
* Recognition tricks
* Interview intuition

---

# What is a Queue

A Queue follows FIFO (First In First Out)

Example:

push 1, push 2, push 3
pop → 1 comes out first

In Python:

```python
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.popleft()  # removes 1
```

---

# What is BFS

BFS means Breadth First Search

It explores level by level

Used in:

* graphs
* trees
* grids
* shortest path (unweighted)

---

# When to Think of BFS or Queue

Use BFS when you see:

* shortest path in unweighted graph
* minimum steps
* level order traversal
* grid traversal
* multi-source expansion
* nearest distance problem
* spreading problems (fire, infection)

---

# Core Idea

* Use a queue
* process elements level by level
* mark visited
* push neighbors

Time complexity is usually O(n) or O(V + E)

---

# 1) Basic BFS (Graph)

When to use:

* traverse graph
* shortest path in unweighted graph

Code:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()
        print(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

---

# 2) BFS Shortest Path (Unweighted)

When to use:

* minimum distance
* shortest steps

Code:

```python
from collections import deque

def shortest_path(graph, start):
    q = deque([(start, 0)])
    visited = set([start])

    while q:
        node, dist = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                if nei == target:
                    return dist + 1
                visited.add(nei)
                q.append((nei, dist + 1))
```

---

# 3) Level Order Traversal (Tree)

When to use:

* tree level by level

Code:

```python
from collections import deque

def level_order(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result
```

---

# 4) Multi Source BFS

When to use:

* multiple starting points
* nearest distance from many sources

Example:

* rotten oranges
* nearest zero

Code:

```python
from collections import deque

def multi_source_bfs(grid):
    m, n = len(grid), len(grid[0])
    q = deque()

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                q.append((nx, ny))
```

---

# 5) Grid BFS

When to use:

* matrix problems
* shortest path in grid

Code:

```python
from collections import deque

def bfs_grid(grid, start):
    m, n = len(grid), len(grid[0])
    q = deque([start])
    visited = set([start])

    while q:
        x, y = q.popleft()

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
```

---

# 6) BFS with Distance

When to use:

* shortest steps
* layers matter

Code:

```python
from collections import deque

def bfs_distance(start):
    q = deque([(start, 0)])
    visited = set([start])

    while q:
        node, dist = q.popleft()

        # process node

        for nei in get_neighbors(node):
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))
```

---

# 7) Topological Sort (Kahn’s Algorithm)

When to use:

* DAG
* dependencies
* course schedule

Code:

```python
from collections import deque

def topo_sort(n, edges):
    graph = {i: [] for i in range(n)}
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return result
```

---

# 8) Minimum Steps Problems

When to use:

* minimum moves
* transformation problems

Example:

* word ladder
* number transformations

Code idea:

```python
def min_steps(start, target):
    q = deque([(start, 0)])
    visited = set([start])

    while q:
        node, steps = q.popleft()

        if node == target:
            return steps

        for nei in get_neighbors(node):
            if nei not in visited:
                visited.add(nei)
                q.append((nei, steps + 1))
```

---

# 9) BFS with State

When to use:

* extra conditions
* visited depends on state

Example:

* visited with key
* visited with direction

Code:

```python
def bfs_state(start):
    q = deque([(start, 0, state)])
    visited = set([(start, state)])

    while q:
        node, dist, state = q.popleft()

        for nei, new_state in get_neighbors(node, state):
            if (nei, new_state) not in visited:
                visited.add((nei, new_state))
                q.append((nei, dist + 1, new_state))
```

---

# Quick Recognition Guide

| Problem Type             | Use              |
| ------------------------ | ---------------- |
| Shortest path unweighted | BFS              |
| Minimum steps            | BFS              |
| Grid traversal           | BFS              |
| Multi-source spread      | BFS              |
| Level order tree         | BFS              |
| Dependencies (DAG)       | Topological sort |

---

# Master Notes

## 1) Why BFS gives shortest path

Because it explores level by level

First time reaching target = minimum steps

---

## 2) Always use visited

Without visited → infinite loop

---

## 3) Use queue for order

Queue ensures:

* first come
* first processed

---

## 4) Distance trick

Store:

node, distance

or

process level size

---

## 5) Multi-source BFS trick

Push all sources first

Then run BFS

---

# Common Problems

* Number of Islands
* Rotting Oranges
* Word Ladder
* Course Schedule
* Binary Tree Level Order
* Shortest Path in Grid
* Walls and Gates
* Knight Moves

---

# Final Summary Table

| Pattern          | Use Case         | Core Idea            |
| ---------------- | ---------------- | -------------------- |
| BFS              | shortest path    | level traversal      |
| Grid BFS         | matrix problems  | 4-direction movement |
| Multi-source BFS | spread problems  | multiple starts      |
| Topological sort | dependencies     | indegree + queue     |
| BFS with state   | complex problems | state tracking       |

---

# Final Intuition

Queue and BFS is about:

* exploring level by level
* finding shortest path
* expanding uniformly

---

# One-Line Memory Trick

If problem says minimum steps or shortest path in unweighted graph → use BFS

---

