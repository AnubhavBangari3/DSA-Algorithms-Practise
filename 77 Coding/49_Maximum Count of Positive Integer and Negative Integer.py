'''
2529. Maximum Count of Positive Integer and Negative Integer
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

    In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.

Note that 0 is neither positive nor negative.

 

Example 1:

Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:

Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:

Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

 

Constraints:

    1 <= nums.length <= 2000
    -2000 <= nums[i] <= 2000
    nums is sorted in a non-decreasing order.

 

Follow up: Can you solve the problem in O(log(n)) time complexity?

Algorithm

1. Since array is sorted, use binary search.

2. Find first index where value >= 0.
   This gives count of negative numbers.

3. Find first index where value > 0.
   This gives starting index of positive numbers.

4. positive_count = n - first_positive_index

5. Return max(negative_count, positive_count)

Complexity

Time Complexity:
O(log n)

Space Complexity:
O(1)


'''

class Solution:
    def maximumCount(self, nums):
        n = len(nums)

        # Finds first index where nums[index] >= target
        def lower_bound(target):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        # Count of negative numbers = first index where value >= 0
        negative_count = lower_bound(0)

        # First positive index = first index where value >= 1
        first_positive_index = lower_bound(1)

        # Count of positive numbers
        positive_count = n - first_positive_index

        return max(negative_count, positive_count)