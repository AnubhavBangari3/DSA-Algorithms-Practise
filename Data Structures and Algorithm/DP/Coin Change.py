
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum coins needed
        # to create amount i
        dp = [float("inf")] * (amount + 1)
        # 0 coins are required to make amount 0
        dp[0] = 0

        # Calculate answer for every amount
        for i in range(1, amount + 1):
            # Try every coin
            for coin in coins:
                # Coin can be used
                if coin <= i:

                    dp[i] = min(
                        dp[i],
                        dp[i - coin] + 1
                    )

        # Amount cannot be created
        if dp[amount] == float("inf"):
            return -1

        return dp[amount]
'''
1. Use Dynamic Programming.
2. Let `dp[i]` represent the minimum number of coins required to make amount `i`.
3. Initialize:
   - `dp[0] = 0`
   - All other values as infinity.
4. For every amount from `1` to `amount`, try every coin.
5. If the coin can be used:

   `dp[i] = min(dp[i], dp[i - coin] + 1)`

6. `dp[i - coin]` gives the best answer before adding the current coin.
7. If `dp[amount]` remains infinity, return `-1`.
8. Otherwise return `dp[amount]`.

Complexity
Time Complexity: O(amount × n)
Space Complexity: O(amount)
'''