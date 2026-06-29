'''
33. Search in Rotated Sorted Array
Solved
Medium
Topics
premium lock iconCompanies

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104


Algorithm

1. Use modified Binary Search.

2. Initialize:
   left = 0
   right = len(nums) - 1

3. While left <= right:

   mid = (left + right) // 2

4. If nums[mid] == target:
      return mid

5. Check which half is sorted:

   If nums[left] <= nums[mid]:
      Left half is sorted.

      Check if target lies inside left half:
      nums[left] <= target < nums[mid]

      If yes:
         right = mid - 1
      Else:
         left = mid + 1

6. Else:
      Right half is sorted.

      Check if target lies inside right half:
      nums[mid] < target <= nums[right]

      If yes:
         left = mid + 1
      Else:
         right = mid - 1

7. If not found:
   return -1
'''

class Solution:
    def search(self, nums, target):
        # Binary search boundaries
        left = 0
        right = len(nums) - 1
        while left <= right:
            # Middle index
            mid = (left + right) // 2
            # Target found
            if nums[mid] == target:
                return mid
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # If target lies inside sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise search right half
                else:
                    left = mid + 1
            # Otherwise right half is sorted
            else:
                # If target lies inside sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise search left half
                else:
                    right = mid - 1
        return -1

'''
Time Complexity:
O(log n)

Reason:
Every step removes half of the search space.

Space Complexity:
O(1)

Reason:
Only pointers are used.
'''