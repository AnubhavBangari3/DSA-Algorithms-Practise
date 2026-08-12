'''
35. Search Insert Position
Solved
Easy
Topics
premium lock iconCompanies

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104




'''
'''
1. Since the array is **sorted**, use Binary Search.
2. Initialize:
   - `left = 0`
   - `right = len(nums) - 1`
3. Find the middle index.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`:
   - Search the right half.
6. If `nums[mid] > target`:
   - Search the left half.
7. If the target is not found, `left` will point to the correct **insertion position**.
8. Return `left`.
'''

class Solution:
    def searchInsert(self, nums, target):
        # Search boundaries
        left = 0
        right = len(nums) - 1
        # Binary Search
        while left <= right:
            # Middle index
            mid = (left + right) // 2
            # Target found
            if nums[mid] == target:
                return mid
            # Search right half
            elif nums[mid] < target:
                left = mid + 1
            # Search left half
            else:
                right = mid - 1
        # Target not found.
        # 'left' is the correct insertion position.
        return left

'''
Complexity
Time Complexity: O(log n)
Search space becomes half after every iteration.
Space Complexity: O(1)
Only left, right, and mid are used.
'''