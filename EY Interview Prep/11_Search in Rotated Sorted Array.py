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


'''



'''
Algorithm

1. Use **Binary Search** with two pointers: `left` and `right`.
2. Find the middle index `mid`.
3. If `nums[mid] == target`, return `mid`.
4. Determine which half is sorted:
   - If `nums[left] <= nums[mid]`, the **left half is sorted**.
   - Otherwise, the **right half is sorted**.
5. Check whether the target lies inside the sorted half:
   - If yes, search that half.
   - Otherwise, search the other half.
6. Continue until `left > right`.
7. If the target is not found, return `-1`.
'''

class Solution:
    def search(self, nums: List[int], target: int):
        # Initialize the search range.
        left, right = 0, len(nums) - 1

        # Continue searching while the search space is valid.
        while left <= right:

            # Find the middle index.
            mid = (left + right) // 2
            # Target found.
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted.
            if nums[left] <= nums[mid]:
                # If the target lies within the sorted left half,
                # search the left half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Otherwise, search the right half.
                else:
                    left = mid + 1

            # Otherwise, the right half must be sorted.
            else:
                # If the target lies within the sorted right half,
                # search the right half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Otherwise, search the left half.
                else:
                    right = mid - 1

        # Target not found.
        return -1



'''
Complexity
Time Complexity: O(log n)
We discard half of the search space after every iteration.
Space Complexity: O(1)
Only left, right, and mid variables are used.
'''