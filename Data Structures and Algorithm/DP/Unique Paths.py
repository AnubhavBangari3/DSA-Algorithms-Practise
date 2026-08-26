class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[i][j] = number of ways
        # to reach cell (i, j)
        dp = [[0] * n for _ in range(m)]

        # First column can only be reached by moving down
        for i in range(m):
            dp[i][0] = 1

        # First row can only be reached by moving right
        for j in range(n):
            dp[0][j] = 1

        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):

                # Paths from above + paths from left
                dp[i][j] = (
                    dp[i - 1][j]
                    + dp[i][j - 1]
                )

        return dp[m - 1][n - 1]

'''
1. Use a 2D DP array where:

   `dp[i][j]` = number of ways to reach cell `(i, j)`.

2. The robot can only move **right** or **down**.
3. Therefore, a cell can only be reached from:
   - The cell above → `dp[i-1][j]`
   - The cell on the left → `dp[i][j-1]`
4. So the formula is:

   `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

5. The first row and first column have only `1` possible path.
6. Return the bottom-right value.

Complexity
Time Complexity: O(m × n)
Space Complexity: O(m × n)
'''