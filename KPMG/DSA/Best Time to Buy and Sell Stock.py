class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_price=prices[0]
        ans=0
        for i in range(1,len(prices)):
            current_price=min(current_price,prices[i])
            profit=prices[i]-current_price
            ans=max(ans,profit)
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

