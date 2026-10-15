'''
Algorithm: Merge Sorted Array (Two Pointers)

1. Initialize last = m + n - 1 to track the last position in nums1.
2. Use m - 1 and n - 1 as pointers to the last valid elements of nums1 and nums2.
3. While m > 0 and n > 0:
   - Compare nums1[m - 1] and nums2[n - 1].
   - Place the larger element at nums1[last].
   - Decrement the pointer (m or n) of the selected element.
   - Decrement last.
4. If nums2 has remaining elements (n > 0):
   - Copy nums2[n - 1] into nums1[last].
   - Decrement n and last.
5. Any remaining elements in nums1 are already in their correct positions.
6. nums1 now contains the merged sorted array.

Time Complexity: O(m + n)
Space Complexity: O(1)
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        # Last position where merged value goes
        last = m + n - 1
        # Compare elements from back
        while m > 0 and n > 0:
            # If nums1 element is bigger
            if nums1[m - 1] > nums2[n - 1]:
                # Place bigger element at end
                nums1[last] = nums1[m - 1]
                # Move nums1 pointer
                m -= 1
            else:
                # Place nums2 element at end
                nums1[last] = nums2[n - 1]
                # Move nums2 pointer
                n -= 1
            # Move merged pointer
            last -= 1
        # If nums2 still has remaining elements
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1