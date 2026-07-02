'''
2460. Apply Operations to an Array
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

    If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.

    For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].

Return the resulting array.

Note that the operations are applied sequentially, not all at once.

 

Example 1:

Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
Explanation: We do the following operations:
- i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
- i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
- i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
- i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
- i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].

Example 2:

Input: nums = [0,1]
Output: [1,0]
Explanation: No operation can be applied, we just shift the 0 to the end.

 

Constraints:

    2 <= nums.length <= 2000
    0 <= nums[i] <= 1000

Algorithm

1. Traverse the array from left to right till n - 2

2. For each index i:
   If nums[i] == nums[i + 1]:
       nums[i] = nums[i] * 2
       nums[i + 1] = 0

3. After applying all operations, move all non-zero elements to the front

4. Fill remaining positions with 0

5. Return the modified array

Complexity
Time Complexity:
O(n)

Reason:
- One pass to apply operations
- One pass to move non-zero elements

Space Complexity:
O(1) extra space

'''
class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        
        # Step 1: Apply the given operations sequentially
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Move all non-zero elements to the front
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Step 3: Fill remaining positions with 0
        while j < n:
            nums[j] = 0
            j += 1
        
        return nums