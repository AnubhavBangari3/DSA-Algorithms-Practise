"""
88. Merge Sorted Array

Problem:

Given two sorted arrays nums1 and nums2,

Merge nums2 into nums1 in sorted order.

nums1 has extra space at the end.

Modify nums1 in-place.

Examples:

Input:
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3

Output:
[1,2,2,3,5,6]

Constraints:
- nums1 length = m + n
- 0 <= m,n <= 200
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: Two Pointers (Backward Traversal)
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Create pointer at end of nums1:
      last = m + n - 1

2. Compare elements from back:

      nums1[m-1]
      nums2[n-1]

3. Put larger element at nums1[last]

4. Move pointers backward

5. Continue until one array finishes

6. If nums2 still has elements:
      copy remaining values

7. nums1 remaining elements are already correct
"""

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


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(m + n)

Explanation:

Each element processed once

Space Complexity: O(1)

Explanation:

In-place modification only
No extra array used
"""