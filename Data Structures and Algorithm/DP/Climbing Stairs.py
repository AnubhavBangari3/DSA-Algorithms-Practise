class Solution:
    def climbStairs(self, n: int) -> int:

        # dp[i] = number of ways to reach step i
        dp = [1, 1]

        # Calculate ways for each step
        for i in range(2, n + 1):

            # Reach current step from
            # previous 1-step or 2-step position
            dp.append(
                dp[i - 1] + dp[i - 2]
            )

        return dp[n]

'''
1. To reach step `i`, we can come from:
   - Step `i - 1` by taking `1` step.
   - Step `i - 2` by taking `2` steps.
2. Therefore:

   `dp[i] = dp[i - 1] + dp[i - 2]`

3. Base cases:
   - `dp[0] = 1`
   - `dp[1] = 1`
4. Calculate the number of ways from step `2` to `n`.
5. Return `dp[n]`.

Complexity
Time Complexity: O(n)
Space Complexity: O(n)

'''