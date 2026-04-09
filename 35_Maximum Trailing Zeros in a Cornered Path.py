'''
2245. Maximum Trailing Zeros in a Cornered Path
Medium
Topics
premium lock iconCompanies
Hint

You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

    Horizontal movement means moving in either the left or right direction.
    Vertical movement means moving in either the up or down direction.

 

Example 1:

Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.

Example 2:

Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
Output: 0
Explanation: The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 105
    1 <= m * n <= 105
    1 <= grid[i][j] <= 1000


Algorithm
1. For each cell, count number of 2s and 5s in its value.

2. Build row prefix sums for 2s and 5s.

3. Build column prefix sums for 2s and 5s.

4. For each cell (i, j), calculate counts for:
   - up + left
   - up + right
   - down + left
   - down + right

   For each shape:
      total_2 = vertical_2 + horizontal_2 - current_cell_2
      total_5 = vertical_5 + horizontal_5 - current_cell_5
      zeros = min(total_2, total_5)

5. Return the maximum zeros found.

Time Complexity
O(m * n)

Because:

factor counting for each cell: O(m*n)
prefix sums: O(m*n)
checking all 4 shapes per cell: O(m*n)
Space Complexity
O(m * n)

For factor arrays and prefix sums.


'''
class Solution:
    def maxTrailingZeros(self, grid):
        # Dimensions of grid
        m, n = len(grid), len(grid[0])

        # Helper function to count how many times 'factor' divides x
        # Example: x = 20 -> count_factor(20, 2) = 2, count_factor(20, 5) = 1
        def count_factor(x, factor):
            cnt = 0
            while x % factor == 0:
                x //= factor
                cnt += 1
            return cnt

        # Step 1: Precompute number of 2s and 5s for each cell
        # Because trailing zeros = min(total_2s, total_5s)
        twos = [[0] * n for _ in range(m)]
        fives = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                twos[i][j] = count_factor(grid[i][j], 2)
                fives[i][j] = count_factor(grid[i][j], 5)

        # Step 2: Build row-wise prefix sums
        # row2[i][j] = total 2s in row i from col 0 to j-1
        # row5[i][j] = total 5s in row i from col 0 to j-1
        row2 = [[0] * (n + 1) for _ in range(m)]
        row5 = [[0] * (n + 1) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                row2[i][j + 1] = row2[i][j] + twos[i][j]
                row5[i][j + 1] = row5[i][j] + fives[i][j]

        # Step 3: Build column-wise prefix sums
        # col2[i][j] = total 2s in column j from row 0 to i-1
        # col5[i][j] = total 5s in column j from row 0 to i-1
        col2 = [[0] * n for _ in range(m + 1)]
        col5 = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                col2[i + 1][j] = col2[i][j] + twos[i][j]
                col5[i + 1][j] = col5[i][j] + fives[i][j]

        # Final answer
        ans = 0

        # Step 4: Try every cell as the turning point of the L-shape
        for i in range(m):
            for j in range(n):

                # Current cell's factor counts
                c2 = twos[i][j]
                c5 = fives[i][j]

                # ----- Vertical contributions -----

                # Up: from row 0 to i (inclusive)
                up2 = col2[i + 1][j]
                up5 = col5[i + 1][j]

                # Down: from row i to m-1
                down2 = col2[m][j] - col2[i][j]
                down5 = col5[m][j] - col5[i][j]

                # ----- Horizontal contributions -----

                # Left: from col 0 to j (inclusive)
                left2 = row2[i][j + 1]
                left5 = row5[i][j + 1]

                # Right: from col j to n-1
                right2 = row2[i][n] - row2[i][j]
                right5 = row5[i][n] - row5[i][j]

                # Step 5: Evaluate all 4 L-shaped paths
                # We subtract current cell once because it's counted twice

                # up + left
                ans = max(ans, min(up2 + left2 - c2, up5 + left5 - c5))

                # up + right
                ans = max(ans, min(up2 + right2 - c2, up5 + right5 - c5))

                # down + left
                ans = max(ans, min(down2 + left2 - c2, down5 + left5 - c5))

                # down + right
                ans = max(ans, min(down2 + right2 - c2, down5 + right5 - c5))

        return ans