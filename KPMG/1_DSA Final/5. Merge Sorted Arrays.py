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
1. Initialize three pointers:
   - m-1 → last valid element in nums1.
   - n-1 → last element in nums2.
   - last → last position of nums1.

2. Compare the current elements from the end of both arrays.

3. Place the larger element at nums1[last].

4. Move the corresponding pointer and decrement last.

5. Repeat until one array is exhausted.

6. If nums2 still has remaining elements, copy them into nums1.

7. Remaining elements in nums1 (if any) are already in their correct positions.

Time Complexity: O(m + n)
- Each element is processed exactly once.

Space Complexity: O(1)
- Merging is done in-place using constant extra space.
'''