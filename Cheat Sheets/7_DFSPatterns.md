

# DFS and Recursion Patterns (CP + Interview Guide)

This guide covers DFS and Recursion patterns used in Competitive Programming and interviews.

Each pattern includes:

When to use

Core idea

Code in Python

Recognition tricks

Interview intuition

# What is DFS

DFS means Depth First Search.

It goes deep first, then comes back.

It is commonly used in:

trees

graphs

grids

backtracking problems

connected components

cycle detection

path finding

# What is Recursion

Recursion means a function calling itself.

A recursive solution usually has two parts:

base case

recursive case

Example:

```python
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
```

# When to Think of DFS or Recursion

Use DFS or Recursion when you see:

explore all paths

go deep into tree or graph

connected components

subsets or permutations

backtracking

divide problem into smaller same-type problems

tree traversal

flood fill

island problems

# Core Idea

DFS tries one full path first.

Recursion helps write DFS naturally.

Main pattern:

process current node

visit children or neighbors

backtrack if needed

Time complexity is usually O(n) for trees, O(V + E) for graphs, and depends on branching for backtracking problems.

# 1 Basic DFS on Graph

When to use:

traverse graph

visit all connected nodes

Code:

```python
def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    print(node)

    for nei in graph[node]:
        dfs(graph, nei, visited)
```

# 2 Iterative DFS Using Stack

When to use:

same as DFS

useful when recursion depth may be large

Code:

```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for nei in reversed(graph[node]):
            if nei not in visited:
                stack.append(nei)
```

# 3 DFS on Tree

When to use:

tree traversal

subtree problems

depth-based problems

Code:

```python
def dfs_tree(root):
    if not root:
        return

    print(root.val)

    dfs_tree(root.left)
    dfs_tree(root.right)
```

# 4 Tree Traversal Patterns

Preorder means current left right

```python
def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
```

Inorder means left current right

```python
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
```

Postorder means left right current

```python
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

# 5 DFS on Grid

When to use:

islands

flood fill

connected cells

Code:

```python
def dfs_grid(grid, i, j):
    m, n = len(grid), len(grid[0])

    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
        return

    grid[i][j] = "0"

    dfs_grid(grid, i + 1, j)
    dfs_grid(grid, i - 1, j)
    dfs_grid(grid, i, j + 1)
    dfs_grid(grid, i, j - 1)
```

# 6 Connected Components

When to use:

count groups

count islands

find separate components in graph

Code:

```python
def count_components(graph, n):
    visited = set()
    count = 0

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        for nei in graph[node]:
            dfs(nei)

    for node in range(n):
        if node not in visited:
            count += 1
            dfs(node)

    return count
```

# 7 DFS for Path Existence

When to use:

check whether path exists

source to destination problems

Code:

```python
def has_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited.add(src)

    for nei in graph[src]:
        if has_path(graph, nei, dst, visited):
            return True

    return False
```

# 8 DFS with Backtracking

When to use:

subsets

permutations

combinations

N queens

word search

Core idea:

choose

explore

undo

Code template:

```python
def backtrack(path, choices):
    if base_case:
        result.append(path[:])
        return

    for choice in choices:
        if not valid(choice):
            continue

        path.append(choice)
        backtrack(path, next_choices)
        path.pop()
```

# 9 Subsets Pattern

When to use:

generate all subsets

power set

Code:

```python
def subsets(nums):
    result = []

    def dfs(index, path):
        if index == len(nums):
            result.append(path[:])
            return

        dfs(index + 1, path)

        path.append(nums[index])
        dfs(index + 1, path)
        path.pop()

    dfs(0, [])
    return result
```

# 10 Permutations Pattern

When to use:

all arrangements

ordering matters

Code:

```python
def permute(nums):
    result = []
    used = [False] * len(nums)

    def dfs(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            dfs(path)

            path.pop()
            used[i] = False

    dfs([])
    return result
```

# 11 Combination Sum Pattern

When to use:

pick numbers to reach target

repeated picking allowed

Code:

```python
def combination_sum(candidates, target):
    result = []

    def dfs(index, path, total):
        if total == target:
            result.append(path[:])
            return

        if total > target or index == len(candidates):
            return

        path.append(candidates[index])
        dfs(index, path, total + candidates[index])
        path.pop()

        dfs(index + 1, path, total)

    dfs(0, [], 0)
    return result
```

# 12 DFS for Cycle Detection in Graph

When to use:

detect cycle in directed graph

course schedule type problems

Code:

```python
def has_cycle(graph, n):
    visiting = set()
    visited = set()

    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False

        visiting.add(node)

        for nei in graph[node]:
            if dfs(nei):
                return True

        visiting.remove(node)
        visited.add(node)
        return False

    for node in range(n):
        if dfs(node):
            return True

    return False
```

# 13 DFS for Tree Height or Depth

When to use:

maximum depth

height of tree

Code:

```python
def max_depth(root):
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)
```

# 14 DFS Returning Values

When to use:

subtree sum

height

diameter helper

balanced tree helper

Code:

```python
def subtree_sum(root):
    if not root:
        return 0

    left_sum = subtree_sum(root.left)
    right_sum = subtree_sum(root.right)

    return root.val + left_sum + right_sum
```

# 15 Memoized Recursion

When to use:

overlapping subproblems

DP with recursion

Code:

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

Interview note:

In production or interviews, better write memo as a separate dictionary to avoid mutable default issues.

Better version:

```python
def fib(n):
    memo = {}

    def dfs(x):
        if x in memo:
            return memo[x]
        if x <= 1:
            return x

        memo[x] = dfs(x - 1) + dfs(x - 2)
        return memo[x]

    return dfs(n)
```

# Quick Recognition Guide

| Problem Type             | Use                |
| ------------------------ | ------------------ |
| Tree traversal           | DFS                |
| Connected components     | DFS                |
| Islands or flood fill    | DFS                |
| Explore all paths        | DFS                |
| Subsets and permutations | Backtracking       |
| Cycle detection          | DFS                |
| Height or subtree info   | Recursive DFS      |
| Repeated subproblems     | Memoized recursion |

# Master Notes

## 1 Why DFS works well

DFS explores one full branch before moving to the next.

That makes it very useful when you want full exploration.

## 2 Base case is everything in recursion

Always define stopping condition clearly.

Without base case, recursion never stops.

## 3 Backtracking means undo your choice

This is the most important idea in recursion problems like subsets and permutations.

Do work

go deeper

undo work

## 4 DFS on graph needs visited

Without visited, graph DFS may loop forever.

## 5 DFS on tree usually does not need visited

Because trees do not have cycles if handled normally.

## 6 Return values carefully

Some recursive functions only traverse.

Some recursive functions calculate and return a value.

You must know which one the problem needs.

# Common Problems

Number of Islands

Max Area of Island

Clone Graph

Path Sum

Same Tree

Symmetric Tree

Maximum Depth of Binary Tree

Subsets

Permutations

Combination Sum

Word Search

Course Schedule

Flood Fill

Diameter of Binary Tree

# Interview Intuition

If the question says traverse deeply, explore all possibilities, or solve using smaller similar subproblems, think of DFS or Recursion.

If the question says generate all possible answers, think of backtracking.

If the question asks for something from left subtree and right subtree, think recursive tree DFS.

If the question is about grid groups or islands, think DFS on grid.

# One Line Memory Trick

If the problem wants deep exploration, all possibilities, subtree logic, or connected components, think DFS and Recursion.

# Final Summary Table

| Pattern            | Use Case                 | Core Idea                      |
| ------------------ | ------------------------ | ------------------------------ |
| Graph DFS          | traversal                | visit deeply                   |
| Tree DFS           | tree problems            | recurse on children            |
| Grid DFS           | islands and flood fill   | explore directions             |
| Backtracking       | subsets and permutations | choose explore undo            |
| Cycle detection    | directed graph           | visiting and visited sets      |
| Recursive return   | tree DP style problems   | combine left and right answers |
| Memoized recursion | DP problems              | store repeated results         |


