class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Maximum island area found
        max_area = 0

        # Traverse every cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                # Found land → calculate island area
                if grid[i][j] == 1:

                    area = self.dfs(grid, i, j)

                    # Update maximum area
                    max_area = max(max_area, area)

        return max_area


    def dfs(self, grid, i, j):

        # Stop if out of bounds or not land
        if (
            i < 0
            or j < 0
            or i >= len(grid)
            or j >= len(grid[0])
            or grid[i][j] != 1
        ):
            return 0

        # Count current land cell
        area = 1

        # Mark current cell as visited
        grid[i][j] = 0

        # Add area from all 4 directions
        area += self.dfs(grid, i + 1, j)  # Down
        area += self.dfs(grid, i - 1, j)  # Up
        area += self.dfs(grid, i, j - 1)  # Left
        area += self.dfs(grid, i, j + 1)  # Right

        return area
'''

1. Traverse every cell in the grid.
2. Whenever we find `1`, start a **DFS**.
3. DFS calculates the area of that complete island.
4. For every land cell:
   - Count the current cell as `1`.
   - Mark it as visited.
   - Explore all 4 directions.
5. Add the areas returned by:
   - Down
   - Up
   - Left
   - Right
6. Compare the island area with `maxArea`.
7. Return the maximum area found.


Complexity
Time Complexity: O(m × n)
Every cell is visited at most once.
Space Complexity: O(m × n) worst case
The DFS recursion stack can contain all land cells if the whole grid is one island.
'''