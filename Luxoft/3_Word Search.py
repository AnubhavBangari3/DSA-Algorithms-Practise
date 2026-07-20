class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, index):
            # All characters of the word have been matched.
            if index == len(word):
                return True

            # Stop if the current cell is outside the board.
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False

            # Stop if the current cell does not match
            # the required character.
            if board[row][col] != word[index]:
                return False

            # Store the current character before marking it visited.
            original = board[row][col]

            # Mark the current cell as visited so it cannot
            # be reused in the current path.
            board[row][col] = "#"

            # Search for the next character in all four directions.
            found = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # Restore the cell before returning.
            # This allows the cell to be used in another search path.
            board[row][col] = original

            return found

        # Try every cell as the starting position of the word.
        for row in range(rows):
            for col in range(cols):
                # Start DFS only when the first character matches.
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True

        return False
    
'''
Algorithm

1. Traverse every cell of the board.

2. If a cell matches the first character of the word:
   - Start DFS from that cell.

3. During DFS:
   - If index equals the length of the word,
     return True because every character has been matched.

4. Return False if:
   - The current cell is outside the board.
   - The current cell does not match word[index].

5. Temporarily mark the current cell as visited.

6. Search for the next character in four directions:
   - Down
   - Up
   - Right
   - Left

7. Restore the current cell after checking all directions.

8. If any direction returns True, return True.

9. If no starting cell forms the complete word, return False.

Pattern:
DFS + Backtracking

Time Complexity: O(m × n × 4^L)

Space Complexity: O(L)
'''