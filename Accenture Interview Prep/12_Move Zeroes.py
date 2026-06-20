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

1. Use two pointers.

2. Maintain:
   j = position where next non-zero element should go.

3. Traverse array using i.

4. If nums[i] is non-zero:
   - Swap nums[i] and nums[j]
   - Increment j

5. After traversal:
   - All non-zero elements are at front.
   - All zeros automatically move to end.

6. Modify array in-place.

'''

class Solution:
    def moveZeroes(self, nums):
        # Position where next non-zero should be placed
        j = 0
        # Traverse entire array
        for i in range(len(nums)):
            # Process only non-zero elements
            if nums[i] != 0:
                # Place non-zero at correct position
                nums[i], nums[j] = nums[j], nums[i]
                # Move placement pointer forward
                j += 1
'''
Time Complexity:
O(n)

Reason:
Single traversal of array.

Space Complexity:
O(1)

Reason:
No extra array is used.

'''