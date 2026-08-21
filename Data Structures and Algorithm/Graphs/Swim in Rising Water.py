class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Check if destination is reachable at given time
        def dfs(row, col, time):

            # Out of bounds
            if (
                row < 0
                or col < 0
                or row >= n
                or col >= n
            ):
                return False

            # Already visited
            if (row, col) in visited:
                return False

            # Water level is not high enough
            if grid[row][col] > time:
                return False

            # Mark visited
            visited.add((row, col))

            # Destination reached
            if row == n - 1 and col == n - 1:
                return True

            # Explore 4 directions
            return (
                dfs(row + 1, col, time)
                or dfs(row - 1, col, time)
                or dfs(row, col + 1, time)
                or dfs(row, col - 1, time)
            )

        # Binary search on time
        left = max(grid[0][0], grid[n - 1][n - 1])
        right = n * n - 1

        while left < right:

            mid = (left + right) // 2

            # New visited set for each DFS
            visited = set()

            # Can reach destination at this time
            if dfs(0, 0, mid):
                right = mid

            # Need more water
            else:
                left = mid + 1

        return left

'''
1. Use **Binary Search on time**.
2. Minimum possible time starts from the destination elevation.
3. Maximum possible time is `n² - 1`.
4. For each middle time `mid`, run DFS from `(0,0)`.
5. DFS can only move to cells where:

   `grid[row][col] <= mid`

6. If DFS can reach `(n-1, n-1)`:
   - This time works.
   - Try a smaller time.
7. Otherwise:
   - We need more water.
   - Try a larger time.
8. When binary search ends, return the minimum valid time.

Complexity
Time Complexity: O(n² log(n²))
Space Complexity: O(n²)
'''