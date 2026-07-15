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

'''
Algorithm

1. Set last = m + n - 1.
   - This is the last available index in nums1.

2. While both nums1 and nums2 still have unprocessed elements:

   - Compare nums1[m - 1] and nums2[n - 1].

   - If nums1[m - 1] is greater:
     - Place it at nums1[last].
     - Decrease m by 1.

   - Otherwise:
     - Place nums2[n - 1] at nums1[last].
     - Decrease n by 1.

   - Decrease last by 1.

3. After the main loop, if nums2 still has unprocessed elements:

   - Copy nums2[n - 1] into nums1[last].
   - Decrease n and last.
   - Continue until n becomes 0.

4. If nums1 still has elements remaining, no copying is required because
   those elements are already present in their correct positions.

Pattern:
Two Pointers + Backward Merge

Time Complexity: O(m + n)
Space Complexity: O(1)
'''