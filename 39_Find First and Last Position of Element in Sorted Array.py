'''
34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
premium lock iconCompanies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109

Algorithm

1. Create a helper function search(x):
   - It returns first index where nums[i] >= x

2. Initialize:
   lo = 0, hi = n

3. While lo < hi:
   mid = (lo + hi) // 2

   If nums[mid] < x:
       → move right
       lo = mid + 1
   Else:
       → possible answer, move left
       hi = mid

4. Return lo

5. Use helper:
   start = search(target)
   end = search(target + 1) - 1

6. If start <= end:
       return [start, end]
   Else:
       return [-1, -1]

Complexity

Time Complexity:
O(log n) + O(log n) = O(log n)

Space Complexity:
O(1)

'''

class Solution:
    def searchRange(self, nums, target):        
        # Helper function to find lower bound
        # Returns first index where nums[i] >= x
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                # If mid value is smaller, move right
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    # Possible answer, move left to find first occurrence
                    hi = mid
            return lo
        
        # First occurrence of target
        lo = search(target)
        # Last occurrence of target
        #search(target+1) gives first element greater than target,
        #so subtracting 1 gives last occurrence.
        hi = search(target + 1) - 1
        # Check if target exists
        if lo <= hi:
            return [lo, hi]
        return [-1, -1]