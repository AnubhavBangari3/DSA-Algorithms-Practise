'''
97. Interleaving String
Solved
Medium
Topics
premium lock iconCompanies

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

 

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

 

Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

    
Algorithm

1. First check length:
   If len(s1) + len(s2) != len(s3):
       return False

2. Use DP where:
   dp[i][j] = True if s3[0 : i + j] can be formed
              using s1[0 : i] and s2[0 : j]

3. Base case:
   dp[0][0] = True

4. For every i and j:
   We can reach dp[i][j] in two ways:

   From s1:
   If dp[i-1][j] is True
   and s1[i-1] == s3[i+j-1]
   then dp[i][j] = True

   From s2:
   If dp[i][j-1] is True
   and s2[j-1] == s3[i+j-1]
   then dp[i][j] = True

5. Return dp[len(s1)][len(s2)]


Complexity

Time Complexity:
O(m * n)

Where:
m = length of s1
n = length of s2

Space Complexity:
O(m * n)

Reason:
We use a 2D DP table
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)

        # Length must match
        if m + n != len(s3):
            return False

        # dp[i][j] means:
        # Can s3[0 : i + j] be formed using
        # s1[0 : i] and s2[0 : j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty s1 and empty s2 can form empty s3
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                # Take character from s1
                if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = True

                # Take character from s2
                if j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = True

        return dp[m][n]