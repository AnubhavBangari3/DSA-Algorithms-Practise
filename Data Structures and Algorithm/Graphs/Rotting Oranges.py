from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        # Queue stores: row, column, time
        queue = deque()

        # Count of fresh oranges
        fresh = 0

        # Add all rotten oranges to queue
        # and count fresh oranges
        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    queue.append((i, j, 0))

                elif grid[i][j] == 1:
                    fresh += 1

        # 4 directions
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        # Maximum time required
        ans = 0

        # Multi-source BFS
        while queue:

            row, col, time = queue.popleft()

            # Update total time
            ans = max(ans, time)

            # Check all 4 neighbors
            for dr, dc in directions:

                new_row = row + dr
                new_col = col + dc

                # Neighbor must be inside grid
                # and contain a fresh orange
                if (
                    0 <= new_row < m
                    and 0 <= new_col < n
                    and grid[new_row][new_col] == 1
                ):

                    # Make orange rotten
                    grid[new_row][new_col] = 2

                    # One less fresh orange
                    fresh -= 1

                    # This orange rots at next minute
                    queue.append(
                        (new_row, new_col, time + 1)
                    )

        # If all fresh oranges became rotten
        if fresh == 0:
            return ans

        # Some fresh orange could not be reached
        return -1

'''

1. Use **BFS** because all rotten oranges spread at the same time level by level.
2. Traverse the grid:
   - Add every rotten orange (`2`) to the queue.
   - Count all fresh oranges (`1`).
3. Store each rotten orange as:

   `(row, col, time)`

4. Remove oranges from the queue one by one.
5. Check all 4 neighboring cells.
6. If a neighbor is fresh:
   - Make it rotten.
   - Decrease `fresh`.
   - Add it to the queue with `time + 1`.
7. Track the maximum time taken.
8. At the end:
   - If `fresh == 0`, return the time.
   - Otherwise, return `-1`.


Complexity
Time Complexity: O(m × n)
Every cell is processed at most once.
Space Complexity: O(m × n)
In the worst case, the queue can contain many cells.
'''