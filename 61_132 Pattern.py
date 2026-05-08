'''
456. 132 Pattern
Solved
Medium
Topics
premium lock iconCompanies

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

 

Constraints:

    n == nums.length
    1 <= n <= 2 * 105
    -109 <= nums[i] <= 109

Algorithm

1. Create left_min array:
   left_min[j] = minimum element from index 0 to j

2. Maintain a sorted list of elements on the right side of j.

3. For every j from 1 to n - 2:
   We need to find nums[k] such that:

   left_min[j - 1] < nums[k] < nums[j]

   This means:
   nums[i] < nums[k] < nums[j]

4. Since right side elements are sorted:
   Use binary search to find if any number exists
   greater than left_min[j - 1] and smaller than nums[j].

5. If such number exists:
   return True

6. Otherwise continue.

7. Return False.


Complexity

Using balanced sorted structure:

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Note:
In Python list, insertion/removal is O(n),
so practical complexity becomes O(n^2).
For interview, this is a Binary Search + Sorted Set approach.


'''

from bisect import bisect_right, bisect_left, insort

class Solution:
    def find132pattern(self, nums):
        n = len(nums)

        if n < 3:
            return False

        # left_min[i] = minimum value from nums[0] to nums[i]
        left_min = [0] * n
        left_min[0] = nums[0]

        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])

        # Sorted list of elements on right side
        right = []

        # Initially add elements from index 2 to n-1
        for i in range(2, n):
            insort(right, nums[i])

        # Treat nums[j] as the "3" in 132 pattern
        for j in range(1, n - 1):

            first = left_min[j - 1]   # nums[i], the "1"
            third = nums[j]           # nums[j], the "3"

            # We need some nums[k] such that:
            # first < nums[k] < third
            if first < third:
                # Find first element greater than first
                idx = bisect_right(right, first)

                # If that element exists and is smaller than third,
                # then 132 pattern exists
                if idx < len(right) and right[idx] < third:
                    return True

            # Remove nums[j + 1] from right side
            remove_idx = bisect_left(right, nums[j + 1])
            right.pop(remove_idx)

        return False