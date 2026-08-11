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


'''
'''
1. Use two pointers:
   - `i` → scans the entire array.
   - `j` → points to the position where the next non-zero element should go.
2. Traverse the array using `i`.
3. Whenever `nums[i]` is non-zero:
   - Swap `nums[i]` with `nums[j]`.
   - Increment `j`.
4. After the traversal, all non-zero elements will be at the beginning and zeroes will automatically move to the end.

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
Complexity
Time Complexity: O(n)
We traverse the array once.
Space Complexity: O(1)
The operation is performed in-place.

'''