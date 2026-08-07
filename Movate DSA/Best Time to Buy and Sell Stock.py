class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Minimum price seen so far (best day to buy)
        current_price = prices[0]

        # Maximum profit found so far
        ans = 0

        # Traverse all days starting from day 2
        for i in range(1, len(prices)):

            # Update the minimum buying price
            current_price = min(current_price, prices[i])

            # Profit if we sell today
            profit = prices[i] - current_price

            # Update the maximum profit
            ans = max(ans, profit)

        # Return the maximum profit
        return ans

'''
1. Assume the first day's price is the minimum buying price.
2. Initialize maximum profit as `0`.
3. Traverse the remaining prices.
4. Update the minimum buying price if a lower price is found.
5. Calculate the profit if you sell on the current day.
6. Update the maximum profit.
7. Return the maximum profit.

- **Time:** O(n)
- **Space:** O(1)

'''