class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the search range.
        left = 0
        right = len(nums) - 1
        # Continue until only one element remains.
        while left < right:
            # Find the middle index.
            mid = (left + right) // 2
            # If the middle element is less than or equal to
            # the rightmost element, the minimum lies in the
            # left half (including mid).
            if nums[mid] <= nums[right]:
                right = mid
           # Otherwise, the minimum lies in the right half.
            else:
                left = mid + 1
        # left points to the minimum element.
        return nums[left]
    
'''
Algorithm

1. Initialize two pointers:
   - left at the beginning.
   - right at the end.

2. While left is less than right:

   - Find the middle index.

   - If the middle element is less than or equal to the rightmost element:
     - The minimum lies in the left half (including mid).
     - Move right to mid.

   - Otherwise:
     - The minimum lies in the right half.
     - Move left to mid + 1.

3. Continue until left equals right.

4. Return the element at index left.

Pattern:
Binary Search

Time Complexity: O(log n)
Space Complexity: O(1)
'''