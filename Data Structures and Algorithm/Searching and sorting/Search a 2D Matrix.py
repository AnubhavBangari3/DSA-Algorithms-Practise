class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):

        # Traverse each row.
        for i in range(len(matrix)):

            # Check if the target can lie in the current row.
            if matrix[i][0] <= target <= matrix[i][-1]:

                # Perform binary search on that row.
                return self.binary_search(matrix[i], 0, len(matrix[i]) - 1, target)

        # Target is not present in any row.
        return False

    def binary_search(self, mat, l, r, target):

        # Continue searching while the search space is valid.
        if r >= l:

            # Find the middle index.
            mid = (l + r) // 2

            # Target found.
            if mat[mid] == target:
                return True

            # Search the left half.
            elif target < mat[mid]:
                return self.binary_search(mat, l, mid - 1, target)

            # Search the right half.
            else:
                return self.binary_search(mat, mid + 1, r, target)

        # Target not found.
        return False
    
'''

Algorithm

1. Traverse each row of the matrix.

2. For every row:
   - Check if the target lies between the first and last element of that row.

3. If the target can belong to the current row:
   - Perform binary search on that row.

4. If the target is found during binary search, return True.

5. If no suitable row contains the target, return False.

Pattern:
Binary Search

Time Complexity: O(m + log n)
Space Complexity: O(log n) (recursive binary search)
'''