'''
136. Single Number
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.


Algorithm

1. Initialize result = 0

2. Traverse the array:
   For each number num:
       result = result ^ num

3. Return result

Reason:
- Same numbers cancel each other (num ^ num = 0)
- Only the unique number remains


Complexity
Time Complexity:
O(n) → traverse array once

Space Complexity:
O(1) → no extra space used

'''
class Solution:
    def singleNumber(self, nums):
        # Initialize result to 0
        result = 0
        
        # Traverse all numbers
        for num in nums:
            # XOR operation cancels duplicates
            result ^= num
        
        # Remaining value is the single number
        return result