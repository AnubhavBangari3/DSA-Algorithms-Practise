'''
977. Squares of a Sorted Array
Solved
Easy
Topics
premium lock iconCompanies

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.

 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''
'''
1. Since the array is sorted, the **largest square** will come from either:
   - The leftmost negative number, or
   - The rightmost positive number.
2. Use two pointers:
   - `left = 0`
   - `right = len(nums) - 1`
3. Create a result array of the same size.
4. Fill the result array **from right to left**.
5. Compare:

   `abs(nums[left])` and `abs(nums[right])`

6. Square the larger absolute value and place it at the current result position.
7. Move the corresponding pointer.
8. Continue until the result array is filled.
'''

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Result array
        res = [0] * len(nums)

        # Two pointers
        left = 0
        right = len(nums) - 1

        # Fill result from largest position to smallest
        for i in range(len(nums) - 1, -1, -1):

            # Left value has larger absolute value
            if abs(nums[left]) > abs(nums[right]):

                # Square and place it
                res[i] = nums[left] ** 2

                # Move left pointer
                left += 1

            else:

                # Right value has larger absolute value
                res[i] = nums[right] ** 2

                # Move right pointer
                right -= 1

        return res

'''
Complexity
Time Complexity: O(n)
Every element is processed exactly once.
Space Complexity: O(n)
A result array of size n is created.
'''