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
1. Initialize:
   left = 0
   right = n - 1

2. While left <= right:
   - Calculate the middle index.
   - If nums[mid] == target:
       Return mid.
   - If nums[mid] < target:
       Search the right half.
       left = mid + 1
   - Otherwise:
       Search the left half.
       right = mid - 1

3. If the loop ends, the target is not present.

4. Return -1.

Key Idea:
- Since the array is sorted, eliminate half of the search space after every comparison.

Time Complexity: O(log n)

- The search space is reduced by half after every iteration.

Space Complexity: O(1)

- Only a few variables are used.

'''