class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m = len(board)
        n = len(board[0])

        # DFS to mark border-connected O's as safe
        def dfs(r, c):

            # Stop if out of bounds
            # or current cell is not O
            if ( r < 0 or c < 0 or r >= m or c >= n or board[r][c] != "O"
            ):
                return

            # Mark as safe / visited
            board[r][c] = "V"

            # Visit all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1:
        # Mark all border-connected O's as safe
        for i in range(m):
            for j in range(n):

                if (
                    board[i][j] == "O"
                    and ( i == 0 or i == m - 1  or j == 0 or j == n - 1
                    )
                ):
                    dfs(i, j)

        # Step 2:
        # Remaining O's are surrounded → change to X
        for i in range(m):
            for j in range(n):

                if board[i][j] == "O":
                    board[i][j] = "X"

        # Step 3:
        # Restore safe cells back to O
        for i in range(m):
            for j in range(n):

                if board[i][j] == "V":
                    board[i][j] = "O"


'''
1. Any `'O'` connected to the **border** cannot be surrounded.
2. Start DFS from every border cell containing `'O'`.
3. During DFS, temporarily mark these safe cells as `'V'`.
4. After marking all border-connected regions:
   - Any remaining `'O'` is surrounded, so change it to `'X'`.
5. Finally, change all `'V'` cells back to `'O'`.
6. Modify the board in-place.

Complexity
Time Complexity: O(m × n)
Every cell is visited a constant number of times.
Space Complexity: O(m × n) worst case
Due to DFS recursion stack.
'''