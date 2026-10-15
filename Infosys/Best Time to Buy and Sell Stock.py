'''

Algorithm: Best Time to Buy and Sell Stock (One Pass)

1. Initialize current_price = prices[0] to track the minimum buying price.
2. Initialize ans = 0 to store the maximum profit.
3. Iterate through the prices array starting from index 1.
4. Update current_price = min(current_price, prices[i]).
5. Calculate profit = prices[i] - current_price.
6. Update ans = max(ans, profit).
7. Return ans as the maximum possible profit.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_price=prices[0]

        ans=0

        for i in range(1,len(prices)):
            current_price=min(current_price,prices[i])
            profit=prices[i]-current_price

            ans=max(ans,profit)
        return ans



        