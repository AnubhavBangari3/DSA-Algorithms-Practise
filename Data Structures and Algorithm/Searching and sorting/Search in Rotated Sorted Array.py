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
Algorithm

1. Initialize two pointers:
   - left at the beginning.
   - right at the end.

2. While left is less than or equal to right:

   - Find the middle index.

   - If the middle element is the target,
     return its index.

3. Determine which half of the array is sorted.

4. If the left half is sorted:
   - Check whether the target lies within the left half.
   - If yes, search the left half.
   - Otherwise, search the right half.

5. If the right half is sorted:
   - Check whether the target lies within the right half.
   - If yes, search the right half.
   - Otherwise, search the left half.

6. Continue until the target is found or the search space becomes empty.

7. If the target is not found, return -1.

Pattern:
Binary Search on Rotated Sorted Array

Time Complexity: O(log n)
Space Complexity: O(1)

'''