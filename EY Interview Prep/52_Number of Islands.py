'''
200. Number of Islands
Solved
Medium
Topics
premium lock iconCompanies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

1. Traverse every cell in the grid.
2. Whenever we find `"1"`:
   - We found a **new island**.
   - Increment `islands`.
3. Run **DFS** from that cell.
4. DFS visits all connected land cells:
   - Up
   - Down
   - Left
   - Right
5. Mark every visited land cell as `"0"` so we don't count it again.
6. Continue scanning the grid.
7. Return the total number of islands.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Number of rows and columns
        m = len(grid)
        n = len(grid[0])

        # Count of islands
        islands = 0

        # DFS to sink the entire island
        def dfs(row, col):

            # Stop if out of bounds or current cell is water
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
                return

            # Mark current land as visited by converting it to water
            grid[row][col] = "0"

            # Visit all four neighboring cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Traverse every cell in the grid
        for i in range(m):
            for j in range(n):

                # Found a new island
                if grid[i][j] == "1":
                    islands += 1

                    # Mark the complete island as visited
                    dfs(i, j)

        return islands

'''
Complexity
Time Complexity: O(m × n)
Every cell is visited at most once.
Space Complexity: O(m × n) worst case
The recursion stack can contain many cells if the entire grid is one island.
'''