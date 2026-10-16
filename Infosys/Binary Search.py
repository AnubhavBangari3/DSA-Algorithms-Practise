'''
Algorithm: Binary Search (Two Pointers)

1. Initialize left = 0 and right = len(nums) - 1.
2. Repeat while left <= right.
3. Calculate the middle index: mid = (left + right) // 2.
4. If nums[mid] == target, return mid.
5. If nums[mid] < target:
   - Update left = mid + 1 to search the right half.
6. Otherwise:
   - Update right = mid - 1 to search the left half.
7. Repeat until the target is found or the search range becomes empty.
8. Return -1 if the target is not present.

Time Complexity: O(log n)
Space Complexity: O(1)
'''

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1