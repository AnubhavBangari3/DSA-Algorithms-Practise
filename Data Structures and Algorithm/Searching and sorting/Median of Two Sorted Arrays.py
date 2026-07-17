class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        # Always perform binary search on the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            # Partition index in nums1.
            partitionX = (left + right) // 2
            # Corresponding partition in nums2.
            partitionY = (m + n + 1) // 2 - partitionX
            # Maximum value on the left side of nums1.
            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            # Minimum value on the right side of nums1.
            minRightX = float("inf") if partitionX == m else nums1[partitionX]
            # Maximum value on the left side of nums2.
            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            # Minimum value on the right side of nums2.
            minRightY = float("inf") if partitionY == n else nums2[partitionY]
            # Correct partition found.
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If total length is even.
                if (m + n) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY)
                        + min(minRightX, minRightY)
                    ) / 2

                # If total length is odd.
                return float(max(maxLeftX, maxLeftY))

            # Move towards the left.
            elif maxLeftX > minRightY:
                right = partitionX - 1

            # Move towards the right.
            else:
                left = partitionX + 1

'''
Algorithm

1. Perform binary search on the smaller array.
2. Choose a partition in the first array.
3. Calculate the corresponding partition in the second array.
4. Find:
   - Maximum value on both left partitions.
   - Minimum value on both right partitions.
5. Check whether:
   - Left values are less than or equal to right values.
6. If the partition is correct:
   - For an odd total length, return the maximum left value.
   - For an even total length, return the average of the maximum left and minimum right values.
7. If the left value of the first array is greater than the right value of the second array:
   - Move the partition to the left.
8. Otherwise:
   - Move the partition to the right.
Pattern:
Binary Search on Partition
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)

'''