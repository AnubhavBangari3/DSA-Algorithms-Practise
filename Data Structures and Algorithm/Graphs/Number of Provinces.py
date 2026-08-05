class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Edge case: empty graph
        if not isConnected:
            return 0
        # Total number of cities
        n = len(isConnected)
        # Stores visited cities
        visited = set()
        # DFS to visit all cities in the same province
        def dfs(city):
            # Traverse every possible neighboring city
            for neighbor, connected in enumerate(isConnected[city]):
                # If connected and not visited
                if connected == 1 and neighbor not in visited:
                    # Mark as visited
                    visited.add(neighbor)
                    # Visit all connected cities
                    dfs(neighbor)
        # Number of provinces
        provinces = 0
        # Visit every city
        for city in range(n):
            # New province found
            if city not in visited:
                # Explore the entire province
                dfs(city)
                # Increase province count
                provinces += 1

        return provinces
'''
1. Create an empty visited set.

2. Traverse every city.

3. If the city is not visited:
   • Perform DFS.
   • Mark every reachable city as visited.
   • Increment the province count.

4. Continue until all cities are processed.

5. Return the number of provinces.

Key Idea:

Every DFS completely explores one connected component (province).
Each new DFS call represents one new province.

Time Complexity:

There are n cities.

For each DFS call,
we scan one entire row of the adjacency matrix.

Total work:

O(n²)

--------------------------------

Space Complexity:

Visited set:

O(n)

Recursive DFS stack:

O(n)

Overall:

O(n)

'''