# The Complete DSA & Competitive Programming Cheatsheet

A single reference covering pattern recognition, ready-to-use code templates (Python + C++), complexity guidance, and the mistakes that cost people the most points/interviews.

---

## 1. How to Use This Sheet

1. See a problem → check **Section 3 (Pattern Recognition)** to identify the family.
2. Jump to **Section 4 (Templates)** for a working skeleton in that family.
3. Before coding, sanity-check with **Section 2 (Complexity-to-Input-Size Map)** to pick the right approach.
4. After coding, scan **Section 6 (Pitfalls)** for your language before submitting.

---

## 2. Complexity-to-Input-Size Map (the fastest way to know what algorithm to use)

| Constraint (n or n·m) | Required complexity | What that usually means |
|---|---|---|
| n ≤ 10 | O(n!) or O(2ⁿ · n) | Brute force permutations, full backtracking |
| n ≤ 20 | O(2ⁿ) | Bitmask DP, subset enumeration |
| n ≤ 500 | O(n³) | Floyd-Warshall, simple 3D DP |
| n ≤ 5,000 | O(n²) | DP over pairs, simple two-loop simulation |
| n ≤ 10⁵–10⁶ | O(n log n) | Sorting, binary search, heaps, segment trees, DSU |
| n ≤ 10⁷–10⁸ | O(n) | Single pass, two pointers, prefix sums, sieve |
| n ≤ 10¹⁸ | O(log n) or O(1) | Binary search on answer, matrix exponentiation, math formula |

Rule of thumb: most judges allow ~10⁸ simple operations/sec. If your complexity × n exceeds ~10⁸–10⁹, it will likely TLE.

---

## 3. Pattern Recognition Table (expanded)

| # | Pattern | Recognize When | Core Idea | Typical Complexity | Trigger Words | Classic Problems |
|---|---|---|---|---|---|---|
| 1 | Hashing (Map/Set) | Need fast lookup, duplicates, frequency | Store while traversing instead of re-searching | O(n) | duplicate, frequency, pair exists | Two Sum, Contains Duplicate, Longest Consecutive |
| 2 | Two Pointers | Two indices over array/string, often sorted | Move pointers based on condition | O(n) | sorted, pair, palindrome | 3Sum, Container With Most Water |
| 3 | Sliding Window | Contiguous subarray/substring, longest/shortest | Expand right, shrink left | O(n) | substring, subarray, at most/least | Longest Substring w/o Repeat, Min Window Substring |
| 4 | Prefix Sum | Multiple range sum queries | Precompute cumulative sums | O(n) build, O(1) query | range sum, cumulative | Subarray Sum = K, Range Sum Query |
| 5 | Binary Search | Sorted data or monotonic answer space | Halve search space | O(log n) | sorted, minimum possible, kth | Search Rotated Array, Binary Search on Answer |
| 6 | Stack | Reverse processing / LIFO | Push while processing, pop on break condition | O(n) | parentheses, expression | Valid Parentheses, Min Stack |
| 7 | Monotonic Stack | Nearest greater/smaller element | Keep stack increasing/decreasing | O(n) | next greater, previous smaller | Daily Temperatures, Largest Rectangle |
| 8 | BFS | Level order, shortest path unweighted | Queue, visit level by level | O(V+E) | minimum steps, shortest path | Rotting Oranges, Word Ladder |
| 9 | DFS/Recursion | Explore every path/node | Go deep, backtrack | O(V+E) | connected components, path sum | Number of Islands, Flood Fill |
| 10 | Backtracking | Every combination/permutation needed | Choose → Recurse → Undo | O(2ⁿ) or O(n!) | all combinations, generate | Subsets, N-Queens, Combination Sum |
| 11 | Trees | Hierarchical structure | Recursive DFS / iterative BFS | O(n) | ancestor, depth, diameter | Max Depth, LCA |
| 12 | BST | Left < root < right matters | Inorder traversal = sorted | O(log n) avg | kth smallest, validate | Validate BST, Kth Smallest |
| 13 | Heap / Priority Queue | Repeated smallest/largest/top-K | Maintain only relevant elements | O(n log k) | top k, kth largest, merge lists | Top K Frequent, Merge K Sorted Lists |
| 14 | Greedy | Local best → global optimum (provable) | Sort + take best now | O(n log n) | intervals, scheduling, min jumps | Merge Intervals, Jump Game |
| 15 | Dynamic Programming | Overlapping subproblems | Memoize / tabulate | varies | ways, min cost, max profit | Coin Change, House Robber |
| 16 | Graph Basics | Vertices/edges, connectivity | Build adjacency list, BFS/DFS | O(V+E) | graph, network | Number of Provinces, Clone Graph |
| 17 | Topological Sort | DAG with dependencies | Process indegree-0 nodes first | O(V+E) | prerequisite, order | Course Schedule, Alien Dictionary |
| 18 | Union-Find (DSU) | Dynamic connectivity | Union + path-compressed find | ~O(α(n)) | connected, redundant edge | Redundant Connection, Provinces |
| 19 | Shortest Path (weighted) | Min cost/distance, weighted edges | Dijkstra / Bellman-Ford / Floyd-Warshall | O(E log V) | shortest path, min cost | Network Delay Time |
| 20 | Bit Manipulation | Binary tricks simplify solution | XOR/AND/OR/shifts | O(1)/O(n) | single number, bitmask | Single Number, Counting Bits |
| 21 | Trie | Prefix-based string search | Character tree | O(L) per op | prefix, autocomplete | Implement Trie, Word Search II |
| 22–23 | Monotonic Deque | Window max/min, changing window | Keep deque monotonic | O(n) | sliding window max | Sliding Window Maximum |
| 24 | Advanced DP | Multi-dimension / optimization DP | Careful state design | O(n·k) etc | knapsack, LIS, edit distance | LIS, Edit Distance, Knapsack |
| 25 | Segment Tree / BIT | Range queries + updates | Store aggregated interval data | O(log n) | range update/query, mutable array | Range Sum Query (Mutable) |
| 26 | Number Theory | Primes, GCD/mod, divisibility | Sieve, modular exponentiation | O(n log log n) etc | prime, mod, divisors | Sieve of Eratosthenes, Modular Inverse |
| 27 | Combinatorics | Counting arrangements/selections | Precompute factorials + inverse mod | O(n) precompute | ways to arrange/choose, mod 1e9+7 | nCr mod p |
| 28 | MST | Cheapest way to connect all nodes | Kruskal (DSU) / Prim (heap) | O(E log E) | minimum spanning tree | Min Cost to Connect Points |
| 29 | Bitmask DP | Small n (≤20), subset states | dp[mask][i] | O(2ⁿ · n) | assign, TSP-like, subsets | Traveling Salesman, Assign Tasks |
| 30 | String Matching | Pattern search in text | KMP / Z-function / rolling hash | O(n+m) | find pattern, occurrences | Implement strStr, Repeated Substring |
| 31 | Binary Lifting / LCA | Repeated ancestor queries on tree | Precompute 2ᵏ-th ancestors | O(log n) query | kth ancestor, LCA queries | LCA in tree |
| 32 | Game Theory | Two-player optimal play | Nim/Sprague-Grundy, parity | O(1)–O(n) | win/lose, take stones | Nim Game, Stone Game |

---

## 4. Code Templates

### 4.1 Two Pointers
```python
def two_pointer(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1
```
```cpp
int l = 0, r = n - 1;
while (l < r) {
    int s = arr[l] + arr[r];
    if (s == target) { /* found */ break; }
    else if (s < target) l++;
    else r--;
}
```

### 4.2 Sliding Window (variable size)
```python
def sliding_window(s):
    left = 0
    freq = {}
    best = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1
        while not valid(freq):          # shrink while invalid
            freq[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### 4.3 Binary Search (including "search on answer")
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1

def search_on_answer(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid          # shrink toward smallest feasible
        else:
            lo = mid + 1
    return lo
```

### 4.4 BFS / DFS
```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    q = deque([start])
    dist = {start: 0}
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return dist

def dfs(graph, node, visited):
    visited.add(node)
    for nxt in graph[node]:
        if nxt not in visited:
            dfs(graph, nxt, visited)
```

### 4.5 Backtracking
```python
def backtrack(path, choices):
    if is_solution(path):
        results.append(path[:])
        return
    for c in choices:
        if not valid(c, path):
            continue
        path.append(c)
        backtrack(path, next_choices(choices, c))
        path.pop()          # undo
```

### 4.6 Dynamic Programming (top-down + bottom-up)
```python
from functools import lru_cache

@lru_cache(None)
def dp(state):
    if base_case(state):
        return base_value
    best = float('inf')
    for choice in options(state):
        best = min(best, cost(choice) + dp(next_state(state, choice)))
    return best

# Bottom-up
dp_arr = [0] * (n + 1)
dp_arr[0] = base_value
for i in range(1, n + 1):
    dp_arr[i] = compute_from(dp_arr, i)
```

### 4.7 Union-Find (DSU) with path compression + union by rank
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        return True
```

### 4.8 Dijkstra (shortest path, weighted, non-negative)
```python
import heapq

def dijkstra(graph, src, n):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

### 4.9 Sieve of Eratosthenes + Modular Exponentiation
```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def power_mod(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = result * a % mod
        a = a * a % mod
        b >>= 1
    return result
```

### 4.10 Combinatorics (nCr mod p, precomputed factorials)
```python
MOD = 10**9 + 7
MAXN = 200005
fact = [1] * MAXN
for i in range(1, MAXN):
    fact[i] = fact[i-1] * i % MOD
inv_fact = [1] * MAXN
inv_fact[MAXN-1] = power_mod(fact[MAXN-1], MOD-2, MOD)
for i in range(MAXN-2, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def nCr(n, r):
    if r < 0 or r > n: return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD
```

### 4.11 Segment Tree (range sum, point update)
```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, pos, val):
        pos += self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2*pos] + self.tree[2*pos+1]

    def query(self, l, r):        # sum on [l, r)
        res = 0
        l += self.n; r += self.n
        while l < r:
            if l & 1: res += self.tree[l]; l += 1
            if r & 1: r -= 1; res += self.tree[r]
            l //= 2; r //= 2
        return res
```

### 4.12 Trie
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.is_end
```

### 4.13 Bitmask DP skeleton
```python
n = len(items)
dp = [[float('inf')] * n for _ in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = cost(i)

for mask in range(1 << n):
    for last in range(n):
        if not (mask & (1 << last)): continue
        for nxt in range(n):
            if mask & (1 << nxt): continue
            new_mask = mask | (1 << nxt)
            dp[new_mask][nxt] = min(dp[new_mask][nxt], dp[mask][last] + cost(last, nxt))
```

---

## 5. Language Cheat Sheet (built-ins that save you time)

**Python**
- `heapq` → min-heap only; push `-x` for max-heap
- `bisect.bisect_left/right` → binary search on sorted list
- `collections.deque` → O(1) append/pop both ends
- `collections.Counter` → frequency map
- `collections.defaultdict(list)` → adjacency lists
- `itertools.permutations/combinations` → brute-force enumeration
- `functools.lru_cache` → instant memoization

**C++**
- `priority_queue<int, vector<int>, greater<int>>` → min-heap
- `lower_bound/upper_bound` → binary search on sorted container
- `unordered_map/unordered_set` → O(1) avg hashing (watch adversarial TLE)
- `__builtin_popcount(x)` → count set bits
- `set/multiset` → sorted structure with O(log n) ops

---

## 6. Common Pitfalls (the ones that actually cost submissions/interviews)

**General**
- Off-by-one errors in loop bounds, especially binary search (`<` vs `<=`) and sliding window shrink conditions.
- Forgetting edge cases: empty input, single element, all duplicates, negative numbers.
- Assuming input is sorted when it isn't (or vice versa).
- Not clarifying "distinct" vs "with repetition" before writing backtracking code.

**Python-specific**
- Mutable default arguments (`def f(x, seen=[])`) persist across calls — use `None` and initialize inside.
- Recursion limit (~1000 by default) — raise with `sys.setrecursionlimit()` for deep recursion, or convert to iterative.
- Integer division: `//` floors toward negative infinity, not toward zero — matters with negative numbers.
- Slicing creates copies — can silently blow up complexity if done inside a loop (`O(n)` per slice).

**C++-specific**
- Integer overflow: `int` is 32-bit; use `long long` for sums that can exceed ~2·10⁹.
- Uninitialized variables contain garbage — always initialize.
- Passing large containers by value instead of by reference — silent O(n) copies.
- `unordered_map` can be forced to O(n) worst case by adversarial inputs on some judges — use `map` or a custom hash if TLE is suspicious.

**Complexity/strategy**
- Nesting loops without checking the resulting complexity against Section 2's table before coding.
- Recomputing the same subproblem (should be memoized) — the #1 cause of "correct but TLE."
- Using recursion for DP on large `n` without memoization — silent exponential blowup.
- Ignoring modulo arithmetic requirements ("answer mod 1e9+7") until the very end, causing negative-mod bugs — always mod after every addition/multiplication, and add `MOD` before taking `%` if a subtraction could go negative.

**Interview-specific**
- Jumping to code before stating the approach and its complexity out loud.
- Not asking about constraints (n size, negative numbers, duplicates) before choosing a pattern.
- Silently assuming a greedy approach works without justifying why the local choice is optimal.

---

## 7. Suggested Practice Order

1. Hashing → Two Pointers → Sliding Window → Prefix Sum (array fundamentals)
2. Binary Search → Stack/Monotonic Stack (search & ordering)
3. BFS/DFS → Trees → BST → Graph Basics (traversal fundamentals)
4. Backtracking → Greedy → DP → Advanced DP (decision-making)
5. Heap → Union-Find → Topological Sort → Shortest Path → MST (graph algorithms)
6. Trie → Bit Manipulation → Segment Tree/BIT (specialized structures)
7. Number Theory → Combinatorics → Bitmask DP → String Matching → Game Theory (CP-specific extras)
