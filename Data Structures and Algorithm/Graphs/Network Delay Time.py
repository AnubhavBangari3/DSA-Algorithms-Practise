class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]

        for source, dest, time in times:
            adj[source].append((dest, time))

        # Shortest distance from k to every node
        dist = [float("inf")] * (n + 1)

        # Distance to source itself is 0
        dist[k] = 0

        # Unvisited nodes
        unvisited = set(range(1, n + 1))

        while unvisited:

            # Find unvisited node with smallest distance
            node = min(
                unvisited,
                key=lambda x: dist[x]
            )

            # Remaining nodes are unreachable
            if dist[node] == float("inf"):
                break

            # Mark node as processed
            unvisited.remove(node)

            # Relax all outgoing edges
            for neighbor, time in adj[node]:

                new_dist = dist[node] + time

                # Found a shorter path
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist

        # Some node cannot receive the signal
        if float("inf") in dist[1:]:
            return -1

        # Last node to receive signal determines answer
        return max(dist[1:])

'''

1. Build an adjacency list:

   `source -> [neighbor, travel_time]`

2. Use **Dijkstra's Algorithm** because all edge weights are non-negative.
3. Store the shortest known distance to every node.
4. Start from node `k` with distance `0`.
5. Repeatedly choose the node with the smallest current distance.
6. For each neighbor:
   - Calculate the new distance.
   - If it is smaller than the existing distance, update it.
7. After processing:
   - If any node is still unreachable, return `-1`.
   - Otherwise, return the maximum shortest distance.

Complexity
Time Complexity: O(V² + E)
Space Complexity: O(V + E)

Where V = number of nodes and E = number of edges.
'''