class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Create rows filled with 1
        pascal = [
            [1] * (i + 1)
            for i in range(numRows)
        ]

        # Fill middle elements
        for i in range(numRows):

            for j in range(1, i):

                # Sum of two elements above
                pascal[i][j] = (
                    pascal[i - 1][j - 1]
                    + pascal[i - 1][j]
                )

        return pascal

'''
1. Create `numRows` rows.
2. Initialize every value as `1`.
3. The first and last values of every row always remain `1`.
4. For every middle element, use:

   `pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]`

5. Return the completed triangle.

Complexity
Time Complexity: O(n²)
Space Complexity: O(n²) for the output triangle.

'''