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
1. Initialize two pointers:
   left = 0
   right = n - 1

2. While left <= right:
   - Find mid = (left + right) // 2

   - If nums[mid] == target:
         return mid

   - If nums[mid] < target:
         search in right half
         left = mid + 1

   - Else:
         search in left half
         right = mid - 1

3. If loop ends:
   return -1 (target not found)

Complexity
Time Complexity:
O(log n)

Reason:
Search space is halved every iteration

Space Complexity:
O(1)

Reason:
No extra space used

'''
class Solution:
    def search(self, nums, target):
        # Initialize pointers
        left = 0
        right = len(nums) - 1
        
        # Binary search loop
        while left <= right:
            mid = (left + right) // 2
            
            # If target found
            if nums[mid] == target:
                return mid
            
            # If target is greater → go right
            elif nums[mid] < target:
                left = mid + 1
            
            # If target is smaller → go left
            else:
                right = mid - 1
        
        # Target not found
        return -1