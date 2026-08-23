class Solution:
    def rob(self, nums: List[int]) -> int:

        # Only one house
        if len(nums) == 1:
            return nums[0]

        # dp[i] = maximum money that can be robbed
        # from houses 0 to i
        dp = [0] * len(nums)

        # First house
        dp[0] = nums[0]

        # Choose maximum from first two houses
        dp[1] = max(nums[0], nums[1])

        # Calculate maximum money for remaining houses
        for i in range(2, len(nums)):

            # Option 1: Rob current house + dp[i-2]
            # Option 2: Skip current house and take dp[i-1]
            dp[i] = max(
                nums[i] + dp[i - 2],
                dp[i - 1]
            )

        return dp[-1]

'''
1. Use Dynamic Programming.
2. Let `dp[i]` represent the maximum money we can rob from houses `0` to `i`.
3. For every house, we have two choices:
   - **Rob current house** → `nums[i] + dp[i-2]`
   - **Skip current house** → `dp[i-1]`
4. Take the maximum of these two choices.
5. Formula:

   `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`

6. Return the last value of `dp`.

Complexity
Time Complexity: O(n)
Space Complexity: O(n)

'''