class Solution:
    def moveZeroes(self, nums):
        # Position where next non-zero should be placed
        j = 0
        # Traverse entire array
        for i in range(len(nums)):
            # Process only non-zero elements
            if nums[i] != 0:
                # Place non-zero at correct position
                nums[i], nums[j] = nums[j], nums[i]
                # Move placement pointer forward
                j += 1

'''
1. Initialize a pointer j = 0.
   - j represents the position where the next non-zero element should be placed.

2. Traverse the array using pointer i.

3. For every non-zero element:
   - Swap nums[i] with nums[j].
   - Increment j.

4. Zeroes automatically move to the end because non-zero elements are shifted to the front while maintaining their relative order.

5. The array is modified in-place without using extra space.

Time Complexity: O(n)
- Traverse the array once.

Space Complexity: O(1)
- Only two pointers are used; no extra array is created.
'''