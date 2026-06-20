'''
209. Minimum Size Subarray Sum
Solved
Medium
Topics
premium lock iconCompanies

Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

 

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


Algorithm

1. Use Sliding Window because all numbers are positive.
2. Maintain:
   left = start of window
   current_sum = sum of current window
   min_len = infinity
3. Expand window using right pointer:
   current_sum += nums[right]
4. While current_sum >= target:
   - Update minimum length:
     min_len = min(min_len, right - left + 1)
   - Shrink window from left:
     current_sum -= nums[left]
     left += 1
5. After traversal:
   If min_len is still infinity:
      return 0
   Else:
      return min_len

'''
class Solution:
    def minSubArrayLen(self, target, nums):
        # Left pointer of sliding window
        left = 0
        # Current window sum
        current_sum = 0
        # Store minimum valid window length
        min_len = float('inf')
        # Expand window using right pointer
        for right in range(len(nums)):
            # Add current element to window sum
            current_sum += nums[right]
            # Shrink window while sum is valid
            while current_sum >= target:
                # Update minimum length
                min_len = min(min_len, right - left + 1)
                # Remove left element and shrink window
                current_sum -= nums[left]
                left += 1
        # If no valid subarray found
        if min_len == float('inf'):
            return 0
        return min_len

'''
Time Complexity:
O(n)
Reason:
Each element is added once and removed once.
Space Complexity:
O(1)
Reason:
Only variables are used.

'''