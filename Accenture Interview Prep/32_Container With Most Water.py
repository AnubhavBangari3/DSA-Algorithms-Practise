'''
11. Container With Most Water
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

Algorithm

1. Use Two Pointers.
2. Initialize:
   left = 0
   right = len(height) - 1
   max_area = 0
3. While left < right:
   width = right - left
   current_height = min(height[left], height[right])
   area = width * current_height
   Update:
   max_area = max(max_area, area)

4. Move the pointer with smaller height:
   If height[left] < height[right]:
      left += 1
   Else:
      right -= 1
5. Return max_area.

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

'''
Time Complexity:
O(n)

Reason:
Each pointer moves at most n times.

Space Complexity:
O(1)

Reason:
Only variables are used.

'''