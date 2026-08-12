'''
704. Binary Search

Solved

Easy

Topics

Companies

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


 

Constraints:

1 <= nums.length <= 104

-104 < nums[i], target < 104

All the integers in nums are unique.

nums is sorted in ascending order.



'''

'''
# 704. Binary Search

## Algorithm

1. Since the array is **sorted**, use Binary Search.
2. Initialize:
   - `left = 0`
   - `right = len(nums) - 1`
3. Find the middle index:

   `mid = (left + right) // 2`

4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`:
   - Target must be on the right side.
   - Move `left = mid + 1`.
6. If `nums[mid] > target`:
   - Target must be on the left side.
   - Move `right = mid - 1`.
7. If the target is not found, return `-1`.

### Interview Trick

Because the array is sorted, after every comparison we can **discard half of the array**.

```text
nums[mid] < target → Search RIGHT
nums[mid] > target → Search LEFT
nums[mid] = target → Found

'''


class Solution:
    def search(self, nums, target):
        # Search space boundaries
        left = 0
        right = len(nums) - 1
        # Continue while search space exists
        while left <= right:
            # Find middle index
            mid = (left + right) // 2
            # Target found
            if nums[mid] == target:
                return mid
            # Target lies on right side
            elif nums[mid] < target:
                left = mid + 1
            # Target lies on left side
            else:
                right = mid - 1
        # Target not present
        return -1

'''
Complexity
Time Complexity: O(log n)
Search space becomes half after every iteration.
Space Complexity: O(1)
Only left, right, and mid are used.

'''