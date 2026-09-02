'''
1. Use **Kadane's Algorithm / Dynamic Programming**.
2. `dp[i]` stores the maximum subarray sum **ending at index `i`**.
3. For every element, we have two choices:
   - Continue the previous subarray.
   - Start a new subarray from the current element.
4. Store the maximum of these two choices in `dp[i]`.
5. Return the maximum value from `dp`.
Complexity
Time Complexity: O(n)
Space Complexity: O(n)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # dp[i] = maximum subarray sum ending at index i
        dp = [0] * len(nums)

        # Base case
        dp[0] = nums[0]

        for i in range(1, len(nums)):

            # Either extend previous subarray
            # or start a new subarray
            dp[i] = max(
                nums[i] + dp[i - 1],
                nums[i]
            )

        # Largest sum among all subarrays
        return max(dp)