'''
2500. Delete Greatest Value in Each Row
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given an m x n matrix grid consisting of positive integers.

Perform the following operation until grid becomes empty:

    Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
    Add the maximum of deleted elements to the answer.

Note that the number of columns decreases by one after each operation.

Return the answer after performing the operations described above.

 

Example 1:

Input: grid = [[1,2,4],[3,3,1]]
Output: 8
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
- In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
- In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
The final answer = 4 + 3 + 1 = 8.

Example 2:

Input: grid = [[10]]
Output: 10
Explanation: The diagram above shows the removed values in each step.
- In the first operation, we remove 10 from the first row. We add 10 to the answer.
The final answer = 10.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    1 <= grid[i][j] <= 100


Algorithm

1. Sort each row in ascending order.

2. After sorting, greatest values will be at the end of each row.

3. For each column from left to right:
   - Find the maximum value in that column across all rows.
   - Add it to answer.

4. Return answer.

Complexity

Time Complexity:
O(m * n log n)

Reason:
Each row is sorted.

Space Complexity:
O(1)

Reason:
Sorting is done in-place.



'''

class Solution:
    def deleteGreatestValue(self, grid):
        # Sort each row so values are in increasing order
        for row in grid:
            row.sort()

        answer = 0

        # Number of columns
        n = len(grid[0])

        # For each column, find max among all rows
        for col in range(n):
            max_deleted = 0

            for row in grid:
                max_deleted = max(max_deleted, row[col])

            # Add maximum deleted value of this operation
            answer += max_deleted

        return answer