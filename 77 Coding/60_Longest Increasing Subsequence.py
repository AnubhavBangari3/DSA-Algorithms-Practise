'''
300. Longest Increasing Subsequence
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums, return the length of the longest strictly increasing .

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

 

Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104

 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


Algorithm

1. Create an empty list called tails.

2. Traverse every number in nums:

   For current number num:
   
   - Use binary search to find the first index
     in tails where value >= num

   - If such index does not exist:
         append num to tails
         (extend increasing subsequence)

   - Else:
         replace tails[index] with num
         (keep smaller tail for future subsequences)

3. Length of tails = length of LIS


Algorithm

1. Create an empty list called tails.

2. Traverse every number in nums:

   For current number num:
   
   - Use binary search to find the first index
     in tails where value >= num

   - If such index does not exist:
         append num to tails
         (extend increasing subsequence)

   - Else:
         replace tails[index] with num
         (keep smaller tail for future subsequences)

3. Length of tails = length of LIS


Key Idea

tails[i] stores the smallest possible tail
of an increasing subsequence of length i + 1

Smaller tail is always better because
it gives more chances to extend subsequence later.


Complexity

Time Complexity:
O(n log n)

Reason:
For every element, binary search takes O(log n)

Space Complexity:
O(n)


'''

import bisect

class Solution:
    def lengthOfLIS(self, nums):
        # tails[i] = smallest tail of LIS of length i+1
        tails = []

        # Traverse all numbers
        for num in nums:

            # Find first index where tails[index] >= num
            index = bisect.bisect_left(tails, num)

            # If num is greater than all elements,
            # extend the LIS
            if index == len(tails):
                tails.append(num)

            else:
                # Replace existing tail with smaller value
                # to improve future possibilities
                tails[index] = num

        # Length of tails = LIS length
        return len(tails) 