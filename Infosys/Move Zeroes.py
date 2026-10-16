'''
Algorithm: Move Zeroes (Two Pointers)

1. Initialize j = 0 to track the position of the next non-zero element.
2. Iterate through the array using pointer i.
3. Check if nums[i] != 0.
4. If the current element is non-zero:
   - Swap nums[i] with nums[j].
   - Increment j by 1.
5. If the current element is zero, continue to the next element.
6. Repeat until all elements are processed.
7. All non-zero elements are moved to the front in their original order, and zeroes are moved to the end.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def moveZeroes(self, nums):

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[i], nums[j] = nums[j], nums[i]
                j += 1