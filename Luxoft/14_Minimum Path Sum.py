class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # DP table where dp[row][col] stores the minimum
        # path sum required to reach that cell.
        dp = [[0] * cols for _ in range(rows)]

        # Starting point.
        dp[0][0] = grid[0][0]

        # Fill the first column.
        # We can only come from the cell above.
        for row in range(1, rows):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        # Fill the first row.
        # We can only come from the left cell.
        for col in range(1, cols):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        # Fill the remaining cells.
        for row in range(1, rows):
            for col in range(1, cols):

                # Choose the minimum cost path
                # from the top or left.
                dp[row][col] = (
                    min(dp[row - 1][col], dp[row][col - 1])
                    + grid[row][col]
                )

        # Bottom-right cell contains the answer.
        return dp[rows - 1][cols - 1]
    
'''
Algorithm

1. Create a DP table of the same size as the grid.
2. Store the starting cell value.
3. Fill the first column:
   - A cell can only be reached from the cell above.
4. Fill the first row:
   - A cell can only be reached from the left.
5. For every remaining cell:
   - Take the minimum of:
       - Top cell
       - Left cell
   - Add the current grid value.
6. The bottom-right cell contains the minimum path sum.

Pattern:
Dynamic Programming (Grid DP)

Time Complexity: O(m × n)

Space Complexity: O(m × n)

'''