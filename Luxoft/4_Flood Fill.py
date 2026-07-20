class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Number of rows and columns.
        rows = len(image)
        cols = len(image[0])

        # Original color of the starting pixel.
        original_color = image[sr][sc]

        # If the new color is the same as the original color,
        # no changes are needed.
        if original_color == color:
            return image

        def dfs(row, col):

            # Stop if the current cell is outside the image.
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            # Stop if the current cell does not have
            # the original color.
            if image[row][col] != original_color:
                return

            # Change the current pixel to the new color.
            image[row][col] = color

            # Visit all four neighbouring pixels.
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Start DFS from the given starting pixel.
        dfs(sr, sc)

        return image
        
'''
Algorithm

1. Store the original color of the starting pixel.

2. If the original color is the same as the new color:
   - Return the image immediately.

3. Start DFS from the starting pixel.

4. During DFS:
   - Return if the current cell is outside the image.
   - Return if the current cell does not have the original color.

5. Change the current cell to the new color.

6. Recursively visit all four neighbouring cells:
   - Down
   - Up
   - Right
   - Left

7. Continue until all connected pixels with the original color have been changed.

8. Return the modified image.

Pattern:
DFS (Depth-First Search)

Time Complexity: O(m × n)

Space Complexity: O(m × n) in the worst case (recursion stack)
'''