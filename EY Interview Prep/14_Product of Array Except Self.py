'''
238. Product of Array Except Self
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)



'''
'''
1. Create an `answer` array initialized with `1`.
2. First pass from **left to right**:
   - Store the product of all elements to the **left** of `i`.
3. Second pass from **right to left**:
   - Keep track of the product of all elements to the **right** of `i`.
   - Multiply it with the left product already stored in `answer[i]`.
4. Return `answer`.
'''

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        # Result array
        answer = [1] * n
        # Store left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        # Store right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply left and right products
            answer[i] *= right_product
            # Update right product
            right_product *= nums[i]

        return answer

'''
Complexity
Time Complexity: O(n)
We traverse the array twice.
Space Complexity: O(1) extra space
Only left_product and right_product are used.
The answer array does not count as extra space according to the problem.

'''