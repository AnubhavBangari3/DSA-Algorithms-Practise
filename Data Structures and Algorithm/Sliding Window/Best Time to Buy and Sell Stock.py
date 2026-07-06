class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 'current' will store the minimum stock price seen so far.
        # This represents the best possible day to buy before the current day.
        current = prices[0]

        # 'ans' will store the maximum profit found so far.
        ans = 0

        # Start from day 1 because day 0 is already considered as initial buy price
        for i in range(1, len(prices)):

            # Update the minimum price seen so far
            # If today's price is lower, it becomes the new best buying price
            current = min(current, prices[i])

            # Calculate profit if we sell today
            # profit = selling price today - minimum buying price seen earlier
            profit = prices[i] - current

            # Update maximum profit if today's profit is better
            ans = max(ans, profit)

        # Return the best profit possible from one transaction
        # If no profit was possible, ans remains 0
        return ans

'''
Algorithm

1. Initialize the minimum stock price as the price on the first day.
2. Initialize the maximum profit as 0.
3. Traverse the array from the second day to the last day.
4. For each day's price:
   - Update the minimum price seen so far if the current price is lower.
   - Calculate the profit by selling on the current day using the minimum buying price seen so far.
   - Update the maximum profit if the current profit is greater.
5. After traversing all prices, return the maximum profit found.

Pattern:
Single Pass Traversal + Running Minimum

Time Complexity: O(n)
Space Complexity: O(1)
'''