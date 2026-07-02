'''
1267. Count Servers that Communicate
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 250
    1 <= n <= 250
    grid[i][j] == 0 or 1

Algorithm

1. Count how many servers are present in each row.

2. Count how many servers are present in each column.

3. Traverse the grid again.

4. For every cell grid[i][j] == 1:
   If row_count[i] > 1 OR col_count[j] > 1:
       this server can communicate
       count += 1

5. Return count

Complexity

Time Complexity:
O(m * n)

Reason:
We traverse the grid twice.

Space Complexity:
O(m + n)

Reason:
We store row counts and column counts.

'''
class Solution:
    def countServers(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Count servers in each row
        row_count = [0] * m

        # Count servers in each column
        col_count = [0] * n

        # First pass: fill row_count and col_count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count servers that can communicate
        answer = 0

        # Second pass: check each server
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if row_count[i] > 1 or col_count[j] > 1:
                        answer += 1

        return answer