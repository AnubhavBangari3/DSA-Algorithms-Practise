'''
747. Largest Number At Least Twice of Others
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

 

Example 1:

Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.

 

Constraints:

    2 <= nums.length <= 50
    0 <= nums[i] <= 100
    The largest element in nums is unique.


Algorithm

1. Initialize:
   max_val = -inf
   second_max = -inf
   max_index = -1

2. Traverse array:
   
   For each element nums[i]:
   
   If nums[i] > max_val:
       second_max = max_val
       max_val = nums[i]
       max_index = i
   
   Else if nums[i] > second_max:
       second_max = nums[i]

3. After traversal:
   If max_val >= 2 * second_max:
       return max_index
   Else:
       return -1

Complexity

Time Complexity:
O(n)

Reason:
Single traversal

Space Complexity:
O(1)

Reason:
Only variables used


'''

class Solution:
    def dominantIndex(self, nums):
        # Initialize values
        max_val = float('-inf')
        second_max = float('-inf')
        max_index = -1
        
        # Find largest and second largest
        for i in range(len(nums)):
            if nums[i] > max_val:
                second_max = max_val
                max_val = nums[i]
                max_index = i
            elif nums[i] > second_max:
                second_max = nums[i]
        
        # Check condition
        if max_val >= 2 * second_max:
            return max_index
        
        return -1