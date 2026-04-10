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

1. Initialize:
   left = 1
   right = n

2. While left < right:
   a. Find mid = (left + right) // 2

   b. Count how many numbers in nums are <= mid

   c. If count > mid:
         duplicate lies in left half
         right = mid
      Else:
         duplicate lies in right half
         left = mid + 1

3. When loop ends, left will be the duplicate number

4. Return left


Time Complexity:
O(n log n)

Reason:
- Binary search runs for log n steps
- In each step, we scan the array once to count

Space Complexity:
O(1)

Reason:
- Only a few variables are used
- Array is not modified

'''