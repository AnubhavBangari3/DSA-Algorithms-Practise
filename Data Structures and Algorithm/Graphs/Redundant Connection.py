

class Solution:
    def findRedundantConnection(self,edges: List[List[int]]) -> List[int]:
        # Adjacency list of current graph
        graph = defaultdict(list)

        # Check whether a path already exists
        # between u and target
        def dfs(u, target):

            # Target reached
            if u == target:
                return True

            # Already visited
            if u in visited:
                return False

            # Mark current node visited
            visited.add(u)

            # Explore neighbors
            for nei in graph[u]:

                if dfs(nei, target):
                    return True

            return False

        # Process edges one by one
        for u, v in edges:

            # New visited set for each search
            visited = set()

            # If path already exists,
            # this edge creates a cycle
            if dfs(u, v):
                return [u, v]

            # Otherwise add edge to graph
            graph[u].append(v)
            graph[v].append(u)

        return []
'''
1. Build the graph edge by edge.
2. Before adding a new edge `[u, v]`, check whether `u` and `v` are **already connected**.
3. Use DFS to search for a path from `u` to `v`.
4. If a path already exists:
   - Adding `[u, v]` would create a cycle.
   - So this edge is redundant.
5. Otherwise:
   - Add the edge to the graph.
6. Continue for all edges.
7. Return the redundant edge.

Complexity

Let n be the number of edges.

Time Complexity: O(n²)
For every edge, DFS may traverse up to O(n) nodes/edges.
Space Complexity: O(n)
Adjacency list, visited set, and DFS recursion stack.
'''