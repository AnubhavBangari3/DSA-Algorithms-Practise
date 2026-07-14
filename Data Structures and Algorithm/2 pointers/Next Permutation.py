class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1:
        # Find the start index i of the longest non-increasing suffix.
        #
        # After this loop:
        # - nums[i:] is in non-increasing order.
        # - nums[i - 1] is the pivot, if i > 0.
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # If i == 0, the entire array is in non-increasing order.
        # This is the largest possible permutation.
        # Reverse it to get the smallest possible permutation.
        if i == 0:
            nums.reverse()
            return

        # The pivot is located at index i - 1.
        pivot_index = i - 1

        # Step 2:
        # Since nums[i:] is in non-increasing order,
        # scan from the end to find the first element
        # that is strictly greater than the pivot.
        j = len(nums) - 1

        while nums[j] <= nums[pivot_index]:
            j -= 1

        # Step 3:
        # Swap the pivot with the smallest value greater than it.
        nums[pivot_index], nums[j] = nums[j], nums[pivot_index]

        # Step 4:
        # Reverse the suffix to make it as small as possible.
        nums[i:] = reversed(nums[i:])

'''
Algorithm

1. Start from the end of the array and find the longest suffix that is in non-increasing order.
2. Let i be the starting index of this suffix.
3. If i is 0:
   - The entire array is in non-increasing order.
   - It is already the largest permutation.
   - Reverse the whole array to obtain the smallest permutation.
   - Return.
4. Otherwise, the pivot is at index i - 1.
5. Starting from the end of the array, find the first element greater than the pivot.
6. Swap that element with the pivot.
7. Reverse the suffix starting at index i to make it the smallest possible arrangement.
8. The array is now the next lexicographically greater permutation.

Pattern:
Pivot + Successor + Reverse Suffix

Time Complexity: O(n)
Space Complexity: O(1)
'''