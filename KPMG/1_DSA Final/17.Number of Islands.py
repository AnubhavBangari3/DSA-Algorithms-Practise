class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Number of rows and columns
        m = len(grid)
        n = len(grid[0])

        # Count of islands
        islands = 0

        # DFS to sink the entire island
        def dfs(row, col):

            # Stop if out of bounds or current cell is water
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
                return

            # Mark current land as visited by converting it to water
            grid[row][col] = "0"

            # Visit all four neighboring cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Traverse every cell in the grid
        for i in range(m):
            for j in range(n):

                # Found a new island
                if grid[i][j] == "1":
                    islands += 1

                    # Mark the complete island as visited
                    dfs(i, j)

        return islands

'''
1. Traverse every cell in the grid.

2. Whenever a land cell ('1') is found:
   - Increment the island count.
   - Perform DFS from that cell.

3. During DFS:
   - Mark the current land as visited by changing it to '0'.
   - Visit all four adjacent cells:
     • Up
     • Down
     • Left
     • Right

4. Continue until the entire connected island has been visited.

5. Resume scanning the grid.

6. Return the total number of islands.

Key Idea:
Every DFS completely visits one island, so each DFS call corresponds to exactly one island.


Time Complexity:

Every cell is visited at most once.

DFS visits each land cell only once.

Overall:

O(m × n)

--------------------------------

Space Complexity:

Recursive DFS call stack can grow up to the size of an island.

Worst Case:

O(m × n)

(A completely land-filled grid.)

If iterative DFS/BFS is used,
the auxiliary space is also O(m × n).

'''