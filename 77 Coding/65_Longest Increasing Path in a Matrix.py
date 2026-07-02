'''
329. Longest Increasing Path in a Matrix
Solved
Hard
Topics
premium lock iconCompanies

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1

1. Use DFS from every cell.

2. For each cell, find the longest increasing path starting from that cell.

3. From current cell, try moving in 4 directions:
   - up
   - down
   - left
   - right

4. Move only if:
   next cell is inside matrix
   and matrix[next_row][next_col] > matrix[row][col]

5. Use memoization:
   memo[row][col] stores longest increasing path starting from that cell.

6. If memo[row][col] is already calculated:
   return memo[row][col]

7. For each cell:
   answer = max(answer, dfs(row, col))

8. Return answer.

Algorithm

Time Complexity:
O(m * n)

Reason:
Each cell is computed once.
For each cell, we check 4 directions.

Space Complexity:
O(m * n)

Reason:
Memoization table stores answer for each cell.
Recursion stack can also go up to O(m * n).

'''

class Solution:
    def longestIncreasingPath(self, matrix):

        # Number of rows
        m = len(matrix)

        # Number of columns
        n = len(matrix[0])

        # memo[row][col]
        # Stores longest increasing path starting from (row, col)
        memo = [[0] * n for _ in range(m)]

        # 4 possible movement directions
        # Down, Up, Right, Left
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # DFS function
        def dfs(row, col):

            # If answer already calculated,
            # return stored result
            if memo[row][col] != 0:
                return memo[row][col]

            # Minimum path length is 1
            # (the current cell itself)
            best = 1

            # Explore all 4 directions
            for dr, dc in directions:

                # Calculate next cell position
                new_row = row + dr
                new_col = col + dc

                # Check if next cell is inside matrix
                if 0 <= new_row < m and 0 <= new_col < n:

                    # Move only if next value is greater
                    # because path must be increasing
                    if matrix[new_row][new_col] > matrix[row][col]:

                        # Try extending the path
                        best = max(
                            best,
                            1 + dfs(new_row, new_col)
                        )

            # Store result in memo table
            memo[row][col] = best

            # Return longest path from current cell
            return best

        # Final answer
        answer = 0

        # Start DFS from every cell
        for i in range(m):
            for j in range(n):

                # Update global maximum path
                answer = max(answer, dfs(i, j))

        # Return longest increasing path
        return answer