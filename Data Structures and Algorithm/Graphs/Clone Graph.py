# Definition for a Node.
# class Node:
#     def __init__(self, val=0, neighbors=None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # Original node -> cloned node
        clones = {}

        def dfs(node):

            # Node already cloned
            if node in clones:
                return clones[node]

            # Create clone of current node
            copy = Node(node.val)

            # Store clone before visiting neighbors
            # to handle cycles
            clones[node] = copy

            # Clone every neighbor
            for neighbor in node.neighbors:

                # Add cloned neighbor
                copy.neighbors.append(
                    dfs(neighbor)
                )

            return copy

        # Empty graph
        if node is None:
            return None

        # Clone graph starting from given node
        return dfs(node)

'''
1. If the graph is empty, return `None`.
2. Use a dictionary `clones` to store:

   `original node → cloned node`

3. Start DFS from the given node.
4. If a node has already been cloned:
   - Return its existing clone.
5. Otherwise:
   - Create a new node with the same value.
   - Store it in the dictionary **before visiting neighbors**.
6. Traverse every neighbor:
   - Recursively clone the neighbor.
   - Add the cloned neighbor to the current cloned node.
7. Return the cloned starting node.

Complexity
Time Complexity: O(V + E)
Every vertex is cloned once.
Every edge is visited.
Space Complexity: O(V)
Dictionary stores every cloned node.
DFS recursion stack can contain up to V nodes.

'''