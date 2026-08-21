
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Manhattan distance
        def distance(p1, p2):
            return (
                abs(p1[0] - p2[0])
                + abs(p1[1] - p2[1])
            )

        n = len(points)

        # Graph: node -> (cost, neighbor)
        graph = defaultdict(list)

        # Build all edges
        for i in range(n):
            for j in range(i + 1, n):

                cost = distance(points[i], points[j])

                graph[i].append((cost, j))
                graph[j].append((cost, i))

        # Start MST from node 0
        visited = [False] * n
        visited[0] = True

        # Number of connected points
        count = 1

        # Total MST cost
        total_cost = 0

        # Min heap of available edges
        heap = graph[0]
        heapq.heapify(heap)

        while heap and count < n:

            # Pick cheapest edge
            cost, node = heapq.heappop(heap)

            # Skip already visited nodes
            if visited[node]:
                continue

            # Add node to MST
            visited[node] = True
            count += 1
            total_cost += cost

            # Add its edges to heap
            for edge in graph[node]:
                heapq.heappush(heap, edge)

        return total_cost
'''
1. Treat every point as a node in a graph.
2. The cost between two points is their Manhattan distance:

   `|x1 - x2| + |y1 - y2|`

3. Build edges between every pair of points.
4. Use **Prim's Algorithm** to build a Minimum Spanning Tree.
5. Start from point `0`.
6. Use a min-heap to always choose the cheapest edge leading to an unvisited point.
7. When a new point is added:
   - Add its edge cost to the answer.
   - Mark it visited.
   - Push all its edges into the heap.
8. Stop when all points are connected.
9. Return the total cost.

Complexity
Time Complexity: O(n² log n)
Space Complexity: O(n²)
'''