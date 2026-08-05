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
1. Traverse every cell in the grid.

2. If the current cell is water ('0'),
   skip it.

3. If the current cell is land ('1'):
   • Increase island count.
   • Run DFS from this cell.

4. During DFS:
   • Mark current land as visited ('0').
   • Visit all four directions:
     - Up
     - Down
     - Left
     - Right

5. Continue scanning the grid.

6. Return the total number of islands.

Key Idea:

Each DFS completely visits one connected island.
Therefore, every new DFS call represents one island.


Time Complexity:

Each cell is visited only once.

DFS never revisits a cell because
visited land is converted to water.

Overall:

O(rows × cols)

--------------------------------

Space Complexity:

Recursive DFS stack can grow up to
the size of one island.

Worst Case:

O(rows × cols)

(When the entire grid is land.)
'''