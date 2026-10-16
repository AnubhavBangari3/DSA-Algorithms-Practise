'''
Algorithm: Missing Number (Sorting + Binary Search)

1. Sort the array nums in ascending order.
2. Initialize left = 0 and right = len(nums) - 1.
3. Repeat while left <= right.
4. Calculate the middle index: mid = (left + right) // 2.
5. If nums[mid] == mid:
   - Update left = mid + 1 to search the right half.
6. Otherwise:
   - Update right = mid - 1 to search the left half.
7. Repeat until left > right.
8. Return left as the missing number.

Time Complexity: O(n log n) - Sorting takes O(n log n), and binary search takes O(log n).
Space Complexity: O(n) worst-case auxiliary space for Python's sorting implementation.
'''

class Solution:
    def missingNumber(self, nums):
        # Step 1: Sort the array (skip if already sorted)
        nums.sort()       
        # Step 2: Initialize pointers
        left = 0
        right = len(nums) - 1
        
        # Step 3: Binary Search
        while left <= right:
            mid = (left + right) // 2
            
            # If value matches index → missing is on right side
            if nums[mid] == mid:
                left = mid + 1
            else:
                # If mismatch → missing is on left side
                right = mid - 1
        
        # Step 4: 'left' is the missing number
        return left