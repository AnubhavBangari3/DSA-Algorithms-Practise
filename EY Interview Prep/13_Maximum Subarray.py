'''
53. Maximum Subarray
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums, find the with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.




'''

'''
1. Use **Dynamic Programming (Kadane's Algorithm)**.
2. Create a `dp` array where:
   - `dp[i]` = maximum subarray sum **ending at index `i`**.
3. For every element, we have two choices:
   - Extend the previous subarray.
   - Start a new subarray from the current element.
4. Therefore:

   `dp[i] = max(nums[i], nums[i] + dp[i - 1])`

5. Return the maximum value from the `dp` array.

### Interview Trick

At every element, ask:

**"Should I continue the previous subarray or start fresh from here?"**

```text
dp[i] = max(
    nums[i],               # Start new
    nums[i] + dp[i - 1]    # Continue previous
)

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = Maximum subarray sum ending at index i
        dp = [0] * len(nums)

        # Base case: first element
        dp[0] = nums[0]

        # Build the DP array
        for i in range(1, len(nums)):

            # Either:
            # 1. Extend the previous subarray
            # 2. Start a new subarray from the current element
            dp[i] = max(nums[i] + dp[i - 1], nums[i])

        # The answer is the maximum value in dp
        return max(dp)

'''
Time Complexity: O(n)
We traverse the array once.
Space Complexity: O(n)
We use a DP array of size n.

'''