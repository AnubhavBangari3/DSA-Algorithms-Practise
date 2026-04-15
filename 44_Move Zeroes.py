'''
283. Move Zeroes
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?


Algorithm


1. Initialize j = 0

2. Traverse array with i from 0 to n-1:

   If nums[i] != 0:
       swap nums[i] with nums[j]
       increment j

3. End
   → array modified in-place

Time Complexity:
O(n) → single pass

Space Complexity:
O(1) → in-place, no extra space

'''

class Solution:
    def moveZeroes(self, nums):
        # Pointer for next non-zero position
        j = 0
        
        # Traverse array
        for i in range(len(nums)):
            
            # If current element is non-zero
            if nums[i] != 0:
                
                # Swap current with position j
                nums[i], nums[j] = nums[j], nums[i]
                
                # Move j forward
                j += 1