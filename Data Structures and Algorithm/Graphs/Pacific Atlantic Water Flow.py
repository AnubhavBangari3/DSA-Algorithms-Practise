class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        # Cells reachable from each ocean
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):

            # Mark current cell visited
            visited.add((r, c))

            # Explore 4 directions
            directions = [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1)
            ]

            for nr, nc in directions:

                # Move only inside grid,
                # to higher/equal cells,
                # and unvisited cells
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and heights[nr][nc] >= heights[r][c]
                    and (nr, nc) not in visited
                ):
                    dfs(nr, nc, visited)

        # Left edge → Pacific
        # Right edge → Atlantic
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        # Top edge → Pacific
        # Bottom edge → Atlantic
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        # Cells that can reach both oceans
        return [list(cell) for cell in pacific & atlantic]

'''
1. Instead of checking water flow from every cell to both oceans, work **backwards from the oceans**.
2. Create two sets:
   - `pacific` → cells that can reach the Pacific.
   - `atlantic` → cells that can reach the Atlantic.
3. Run DFS from all Pacific border cells:
   - Top row
   - Left column
4. Run DFS from all Atlantic border cells:
   - Bottom row
   - Right column
5. While moving backwards from an ocean, only move to a cell with height:

   `next_height >= current_height`

6. This means water from that higher/equal cell can flow down to the current cell and eventually reach the ocean.
7. Return the intersection:

   `pacific & atlantic`

   Complexity
Time Complexity: O(m × n)
Space Complexity: O(m × n)
'''