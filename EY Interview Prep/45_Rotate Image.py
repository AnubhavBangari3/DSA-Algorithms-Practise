'''
48. Rotate Image
Solved
Medium
Topics
premium lock iconCompanies

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

 

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000



'''
'''
To rotate the matrix **90° clockwise in-place**:

1. **Reverse the rows** of the matrix.
2. **Transpose the matrix**:
   - Swap `matrix[i][j]` with `matrix[j][i]`.
3. The matrix is now rotated 90° clockwise.
'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # Step 1: Reverse the rows
        left = 0
        right = len(matrix) - 1

        while left < right:

            # Swap top and bottom rows
            matrix[left], matrix[right] = matrix[right], matrix[left]

            left += 1
            right -= 1

        # Step 2: Transpose the matrix
        for i in range(len(matrix)):

            # Only process below diagonal
            # to avoid swapping twice
            for j in range(i):

                # Swap row and column positions
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i],
                    matrix[i][j]
                )
'''
Complexity
Time Complexity: O(n²)
We process the elements of the n × n matrix.
Space Complexity: O(1)
The matrix is modified in-place.
'''
        