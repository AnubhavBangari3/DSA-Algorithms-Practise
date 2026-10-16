'''
Algorithm: Rotate Image 90° Clockwise (Reverse + Transpose)

1. Initialize two pointers: left = 0 and right = len(matrix) - 1.
2. Reverse the rows of the matrix:
   - Swap matrix[left] with matrix[right].
   - Increment left and decrement right.
   - Repeat until left >= right.
3. Transpose the matrix by swapping rows and columns.
4. Iterate through each row using index i.
5. For each i, iterate j from 0 to i - 1.
6. Swap matrix[i][j] with matrix[j][i].
7. The matrix is now rotated 90° clockwise in place.

Time Complexity: O(n²)
Space Complexity: O(1)
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