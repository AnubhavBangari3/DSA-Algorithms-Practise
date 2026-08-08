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
1. Start three pointers from the end of `nums1`, valid elements of `nums1`, and `nums2`.
2. Compare the last valid elements of both arrays.
3. Put the larger element at the last available position in `nums1`.
4. Move the corresponding pointer backward.
5. Continue until one array is exhausted.
6. If `nums2` still has elements, copy them into `nums1`.
7. We don't need to copy remaining `nums1` elements because they are already in the correct positions.


- **Time:** O(m + n)
- **Space:** O(1)
'''