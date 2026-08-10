'''
169. Majority Element
Solved
Easy
Topics
premium lock iconCompanies

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.

 
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

'''
1. Create a dictionary `freq` to store the frequency of each number.
2. Loop through `nums`.
3. Increase the frequency of the current number.
4. After increasing the count, check if it is greater than `n / 2`.
5. If yes, return that number because it is the **majority element**.

'''

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Dictionary to store frequency of each element
        freq = defaultdict(int)

        # Count the occurrences
        for num in nums:
            freq[num] += 1

            # Return immediately if count exceeds n/2
            if freq[num] > len(nums) // 2:
                return num

'''
Time Complexity: O(n)
We traverse the array once.
Space Complexity: O(n)
The dictionary may store up to n different elements.
'''