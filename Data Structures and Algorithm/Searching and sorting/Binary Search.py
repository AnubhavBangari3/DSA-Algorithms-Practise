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