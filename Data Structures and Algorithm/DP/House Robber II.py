class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Only one house
        if n == 1:
            return nums[0]

        # Case 1:
        # Include first house, exclude last house
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n - 1):

            # Rob current OR skip current
            dp[i] = max(
                nums[i] + dp[i - 2],
                dp[i - 1]
            )

        # Case 2:
        # Exclude first house, allow last house
        dp2 = [0] * n

        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, n):

            # Rob current OR skip current
            dp2[i] = max(
                nums[i] + dp2[i - 2],
                dp2[i - 1]
            )

        # Best of both cases
        return max(
            dp[n - 2],
            dp2[n - 1]
        )

'''
1. Houses are arranged in a **circle**, so the first and last houses are adjacent.
2. Therefore, we cannot rob both the first and last house.
3. Break the problem into two normal House Robber cases:

   - Case 1: Rob houses from `0` to `n-2` → exclude last house.
   - Case 2: Rob houses from `1` to `n-1` → exclude first house.

4. Solve both cases using the House Robber DP formula:

   `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`

5. Return the maximum of both cases.

Complexity
Time Complexity: O(n)
Space Complexity: O(n)

'''