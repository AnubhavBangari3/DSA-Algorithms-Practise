'''
1. Create a `dp` table of size `(m + 1) x (n + 1)`.
2. `dp[i][j]` represents the LCS length between:
   - first `i` characters of `text1`
   - first `j` characters of `text2`
3. If characters match:

   `dp[i][j] = dp[i-1][j-1] + 1`

4. If characters do not match:

   `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

5. Return `dp[m][n]`.

Complexity
Time Complexity: O(m × n)
Space Complexity: O(m × n)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        # dp[i][j] stores LCS length
        # for text1[:i] and text2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Characters match
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # Characters don't match
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[m][n]