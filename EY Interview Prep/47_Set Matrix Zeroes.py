'''
73. Set Matrix Zeroes
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

 

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

 

Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?


'''
'''
1. Use the **first row and first column as markers**.
2. First, check whether:
   - The first column originally contains any `0`.
   - The first row originally contains any `0`.
3. Traverse the remaining matrix starting from `(1,1)`.
4. If `matrix[i][j] == 0`:
   - Mark its row using `matrix[i][0] = 0`.
   - Mark its column using `matrix[0][j] = 0`.
5. Traverse the matrix again:
   - If `matrix[i][0] == 0`, set that row to `0`.
   - If `matrix[0][j] == 0`, set that column to `0`.
6. Finally, handle the first row and first column using the saved flags.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # Flags for first column and first row
        first_col_zero = False
        first_row_zero = False

        # Check if first column originally contains zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Check if first row originally contains zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):

                if matrix[i][j] == 0:

                    # Mark entire row
                    matrix[i][0] = 0

                    # Mark entire column
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, m):

            if matrix[i][0] == 0:

                for j in range(1, n):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, n):

            if matrix[0][j] == 0:

                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

'''
Complexity
Time Complexity: O(m × n)
The matrix is traversed a constant number of times.
Space Complexity: O(1)
The first row and first column are used as marker storage.
'''