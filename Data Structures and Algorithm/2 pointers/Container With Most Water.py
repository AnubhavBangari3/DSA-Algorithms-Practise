class Solution:
    def maxArea(self, height):
        # Left and right pointers
        left = 0
        right = len(height) - 1
        # Store maximum water area
        max_area = 0
        # Move pointers until they meet
        while left < right:
            # Width between two lines
            width = right - left
            # Height is limited by the shorter line
            current_height = min(height[left], height[right])
            # Calculate area
            area = width * current_height
            # Update max area
            max_area = max(max_area, area)
            # Move the smaller height pointer
            # because smaller line limits the water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
'''
Algorithm

1. Initialize two pointers:
   - left at the beginning
   - right at the end

2. Initialize max_area as 0.

3. While left is less than right:
   - Calculate width = right - left.
   - Calculate height = minimum of height[left] and height[right].
   - Calculate area = width * height.
   - Update max_area if current area is larger.

4. Move the pointer with the smaller height:
   - If height[left] < height[right], move left forward.
   - Otherwise, move right backward.

5. Continue until both pointers meet.

6. Return max_area.

Pattern:
Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
'''