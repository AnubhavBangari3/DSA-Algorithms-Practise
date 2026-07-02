'''
Q3. Minimum XOR Path in a Grid
Medium
5 pt.

You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

 

Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

    (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
    (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

    (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
    (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

    (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

 

Constraints:

    1 <= m == grid.length <= 1000
    1 <= n == grid[i].length <= 1000
    m * n <= 1000
    0 <= grid[i][j] <= 1023​


    
Algorithm
1. Let dp[i][j] store all XOR values possible when reaching cell (i, j).

2. Base case:
   dp[0][0] = {grid[0][0]}

3. For every cell (i, j):
   - If coming from top:
       for each xor_value in dp[i-1][j]:
           add xor_value ^ grid[i][j] into dp[i][j]

   - If coming from left:
       for each xor_value in dp[i][j-1]:
           add xor_value ^ grid[i][j] into dp[i][j]

4. At the end, bottom-right cell will contain all possible XOR values.
   Return the minimum of them.

Time Complexity
O(m * n * 1024)
Because:
each cell may process up to 1024 XOR states
Space Complexity
O(m * n * 1024)

Because:
we may store up to 1024 XOR states for each cell
Since:
m * n <= 1000
this is acceptable.
'''

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ grid[i][j])

                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ grid[i][j])

        return min(dp[m - 1][n - 1])