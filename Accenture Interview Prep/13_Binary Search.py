'''
704. Binary Search
Solved
Easy
Topics
premium lock iconCompanies

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

Algorithm

1. Initialize:
   left = 0
   right = len(nums) - 1
2. While left <= right:
   a. Find middle:
      mid = (left + right) // 2

   b. If nums[mid] == target:
         return mid

   c. If nums[mid] < target:
         search right half
         left = mid + 1

   d. Else:
         search left half
         right = mid - 1
3. If target not found:
   return -1

'''
class Solution:
    def search(self, nums, target):
        # Search space boundaries
        left = 0
        right = len(nums) - 1
        # Continue while search space exists
        while left <= right:
            # Find middle index
            mid = (left + right) // 2
            # Target found
            if nums[mid] == target:
                return mid
            # Target lies on right side
            elif nums[mid] < target:
                left = mid + 1
            # Target lies on left side
            else:
                right = mid - 1
        # Target not present
        return -1
'''
Time Complexity:
O(log n)

Reason:
Every iteration eliminates half of the search space.

Space Complexity:
O(1)

Reason:
Only pointers are used.
'''