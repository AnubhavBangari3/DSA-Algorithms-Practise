class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m = len(board)
        n = len(board[0])

        # DFS to mark border-connected O's as safe
        def dfs(r, c):

            # Stop if out of bounds
            # or current cell is not O
            if (r < 0 or c < 0 or r >= m  or c >= n  or board[r][c] != "O"
            ):
                return

            # Mark current O as safe / visited
            board[r][c] = "V"

            # Visit all 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Step 1:
        # Find all border-connected O's
        for i in range(m):
            for j in range(n):

                # Start DFS only from border O's
                if (
                    board[i][j] == "O"
                    and (   i == 0 or i == m - 1  or j == 0  or j == n - 1
                    )
                ):
                    dfs(i, j)

        # Step 2:
        # Remaining O's are surrounded
        for i in range(m):
            for j in range(n):

                if board[i][j] == "O":
                    board[i][j] = "X"

        # Step 3:
        # Restore safe cells
        for i in range(m):
            for j in range(n):

                if board[i][j] == "V":
                    board[i][j] = "O"

'''
1. Any `'O'` connected to the **border** cannot be surrounded.
2. Traverse all border cells.
3. If a border cell is `'O'`, run DFS from it.
4. Mark every connected safe `'O'` as `'V'`.
5. After DFS:
   - Remaining `'O'` cells are surrounded → convert them to `'X'`.
6. Convert all temporary `'V'` cells back to `'O'`.
7. Modify the board in-place.

'''