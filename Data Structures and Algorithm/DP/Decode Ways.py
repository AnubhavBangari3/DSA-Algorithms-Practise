class Solution:
    def numDecodings(self, s: str) -> int:

        # Memoization dictionary
        dp = {}

        def dfs(s):

            # Successfully decoded complete string
            if not s:
                return 1

            # Already calculated
            if s in dp:
                return dp[s]

            single = 0
            double = 0

            # Take one digit
            if 1 <= int(s[:1]) <= 9:
                single = dfs(s[1:])

            # Take two digits
            if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
                double = dfs(s[2:])

            # Total decoding combinations
            dp[s] = single + double

            return dp[s]

        return dfs(s)

'''
1. Use **DFS + Memoization**.
2. At every position, we have two choices:
   - Take **1 digit** if it is between `1` and `9`.
   - Take **2 digits** if it is between `10` and `26`.
3. Recursively solve the remaining string.
4. If the string becomes empty, return `1` because one valid decoding is completed.
5. Store results in a dictionary so the same substring is not calculated again.
6. Return the total of:
   - Single-digit decoding ways.
   - Double-digit decoding ways.

Complexity
Time Complexity: O(n)
Space Complexity: O(n)

'''