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
    
'''
Algorithm

1. Sort the array.

2. Initialize two pointers:
   - left = 0
   - right = n - 1

3. While left <= right:
   - Find the middle index.
   - If nums[mid] == mid:
       - Search the right half.
   - Otherwise:
       - Search the left half.

4. After the loop, 'left' represents the missing number.

5. Return left.

Pattern:
Binary Search on Index

Time Complexity:
O(n log n)

Space Complexity:
O(1)

'''