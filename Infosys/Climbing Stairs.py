'''

Algorithm: Climbing Stairs (Dynamic Programming)

1. Initialize dp = [1, 1] to store the number of ways to reach each step.
2. Set dp[0] = 1 and dp[1] = 1 as base cases.
3. Iterate from i = 2 to n.
4. Calculate the number of ways to reach step i:
   - dp[i] = dp[i - 1] + dp[i - 2].
5. Append the calculated value to the dp array.
6. Repeat until all steps are processed.
7. Return dp[n] as the total number of distinct ways to climb n stairs.

Time Complexity: O(n)
Space Complexity: O(n)
'''


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