'''
153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
premium lock iconCompanies
Hint

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

 

Constraints:

    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
    nums is sorted and rotated between 1 and n times.

'''

'''
1. Use **Binary Search**.
2. Initialize:
   - `left = 0`
   - `right = len(nums) - 1`
3. Find the middle index `mid`.
4. Compare `nums[mid]` with `nums[right]`.
5. If:

   `nums[mid] <= nums[right]`

   then the minimum is in the **left half**, including `mid`.

   So:

   `right = mid`

6. Otherwise, the minimum is in the **right half**.

   So:

   `left = mid + 1`

7. Continue until `left == right`.
8. Return `nums[left]`
'''

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
Complexity
Time Complexity: O(log n)
Search space is reduced by half after every iteration.
Space Complexity: O(1)
Only left, right, and mid are used.
'''