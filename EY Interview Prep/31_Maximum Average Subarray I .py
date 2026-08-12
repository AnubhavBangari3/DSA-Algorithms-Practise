'''
643. Maximum Average Subarray I
Solved
Easy
Topics
premium lock iconCompanies

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

 

Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104


'''

'''
1. Since we need a subarray of **fixed size `k`**, use **Sliding Window**.
2. Calculate the sum of the first `k` elements.
3. Store it as:
   - `cur` → current window sum.
   - `maxSum` → maximum window sum found.
4. Move the window one position at a time:
   - Add the new element entering the window.
   - Subtract the old element leaving the window.
5. Update `maxSum`.
6. Return `maxSum / k`.

'''

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Sum of the first window of size k
        cur = sum(nums[:k])

        # Maximum sum found so far
        maxSum = cur

        # Slide the window
        for i in range(k, len(nums)):

            # Add incoming element
            # Remove outgoing element
            cur += nums[i] - nums[i - k]

            # Update maximum window sum
            maxSum = max(maxSum, cur)

        # Maximum average
        return maxSum / k

'''
Complexity
Time Complexity: O(n)
We calculate the first window and then traverse the remaining array once.
Space Complexity: O(1)
Only a few variables are used.
'''