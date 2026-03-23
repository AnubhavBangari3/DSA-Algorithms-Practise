'''
287. Find the Duplicate Number
Solved
Medium
Topics
premium lock iconCompanies

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

 

Constraints:

    1 <= n <= 105
    nums.length == n + 1
    1 <= nums[i] <= n
    All the integers in nums appear only once except for precisely one integer which appears two or more times.

 

Follow up:

    How can we prove that at least one duplicate number must exist in nums?
    Can you solve the problem in linear runtime complexity?


    
Algorithm

1. Initialize two pointers:
   slow = nums[0]
   fast = nums[0]

2. Move:
   slow = nums[slow]
   fast = nums[nums[fast]]

3. Continue until slow == fast
   This confirms intersection inside the cycle.

4. Reset one pointer to nums[0]
   ptr1 = nums[0]
   ptr2 = slow

5. Move both one step at a time:
   ptr1 = nums[ptr1]
   ptr2 = nums[ptr2]

6. When they meet, that value is the duplicate number.

Complexity
Time Complexity: O(n)
Reason:
In phase 1, slow and fast pointers meet inside the cycle in linear time.
In phase 2, both pointers move to the cycle entrance in linear time.
Total is O(n).
Space Complexity: O(1)
Reason:
Only a few pointers are used.
No extra data structure like set, hashmap, or array is used.

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find entrance to the cycle
        ptr1 = nums[0]
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1