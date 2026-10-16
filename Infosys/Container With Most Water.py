'''
Algorithm: Container With Most Water (Two Pointers)

1. Initialize left = 0 and right = len(height) - 1.
2. Initialize max_area = 0 to store the maximum water area.
3. Repeat while left < right.
4. Calculate width = right - left.
5. Calculate current_height = min(height[left], height[right]).
6. Calculate area = width * current_height.
7. Update max_area = max(max_area, area).
8. Move the pointer with the smaller height:
   - If height[left] < height[right], increment left.
   - Otherwise, decrement right.
9. Repeat until both pointers meet.
10. Return max_area as the maximum water area.

Time Complexity: O(n)
Space Complexity: O(1)
'''

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