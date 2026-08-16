'''
54. Spiral Matrix

Solved

Medium

Topics

Companies

Hint

Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


 

Constraints:

m == matrix.length

n == matrix[i].length

1 <= m, n <= 10

-100 <= matrix[i][j] <= 100



'''
'''
1. Maintain four boundaries:
   - `top` → first remaining row.
   - `bottom` → last remaining row.
   - `left` → first remaining column.
   - `right` → last remaining column.
2. Traverse the matrix layer by layer:
   - **Left → Right** across the top.
   - **Top → Bottom** along the right.
   - **Right → Left** across the bottom.
   - **Bottom → Top** along the left.
3. After completing one layer, move all boundaries inward.
4. Continue while a complete rectangular layer exists.
5. If any row or column remains in the center, add those remaining elements.
6. Return the result.
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        # Four boundaries
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        # Store spiral order
        ans = []

        # Process complete layers
        while top < bottom and left < right:

            # 1. Left → Right
            for j in range(left, right):
                ans.append(matrix[top][j])

            # 2. Top → Bottom
            for i in range(top, bottom):
                ans.append(matrix[i][right])

            # 3. Right → Left
            for j in range(right, left, -1):
                ans.append(matrix[bottom][j])

            # 4. Bottom → Top
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])

            # Shrink boundaries
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # Add remaining middle row/column if any
        if len(ans) < rows * cols:

            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    ans.append(matrix[i][j])

        return ans

'''
Complexity
Time Complexity: O(m × n)
Every matrix element is visited exactly once.
Space Complexity: O(1) extra space
Excluding the output array, only four boundary variables are used.
'''