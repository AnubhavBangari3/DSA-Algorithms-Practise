class Solution:
    def searchRange(self, nums, target):

        # Helper function to find the lower bound.
        # It returns the first index where nums[index] >= x.
        def search(x):

            lo, hi = 0, len(nums)

            # Perform binary search
            while lo < hi:
                mid = (lo + hi) // 2

                # If current value is smaller than x,
                # discard the left half.
                if nums[mid] < x:
                    lo = mid + 1

                # Otherwise, mid could be the answer.
                # Continue searching on the left.
                else:
                    hi = mid

            # lo is the lower bound.
            return lo

        # Find the first occurrence of target.
        first = search(target)

        # Find the first element greater than target.
        # Subtract 1 to get the last occurrence of target.
        last = search(target + 1) - 1

        # Verify that the target actually exists.
        if first <= last:
            return [first, last]

        return [-1, -1]
    
'''
Algorithm

1. Create a helper function to find the lower bound of a value using binary search.
   - The lower bound is the first index where the array element is greater than or equal to the given value.

2. Use the helper function to find the first occurrence of the target.

3. Use the helper function again to find the first index of target + 1.

4. Subtract 1 from this index to obtain the last occurrence of the target.

5. If the first index is less than or equal to the last index,
   return both indices.

6. Otherwise, return [-1, -1].

Pattern:
Binary Search (Lower Bound)

Time Complexity: O(log n)
Space Complexity: O(1)

'''