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
1. Initialize:
   current_price = prices[0]
   ans = 0

2. Traverse the prices array from index 1.

3. For each day:
   - Update the minimum buying price seen so far.
   - Calculate the profit if selling today.
   - Update the maximum profit.

4. Return the maximum profit.

Key Idea:
- Always buy at the lowest price seen before today.
- At every day, calculate the profit if you sell on that day.
- Keep track of the maximum profit.

Time Complexity: O(n)

- Traverse the array once.

Space Complexity: O(1)

- Only a few variables are used.

'''