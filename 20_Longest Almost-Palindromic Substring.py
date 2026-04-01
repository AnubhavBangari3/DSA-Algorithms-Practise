'''
3844. Longest Almost-Palindromic Substring
Medium
Topics
premium lock iconCompanies
Hint

You are given a string s consisting of lowercase English letters.

A is almost-palindromic if it becomes a after removing exactly one character from it.

Return an integer denoting the length of the longest almost-palindromic substring in s.

 

Example 1:

Input: s = "abca"

Output: 4

Explanation:

Choose the substring "abca".

    Remove "abca".
    The string becomes "aba", which is a palindrome.
    Therefore, "abca" is almost-palindromic.

Example 2:

Input: s = "abba"

Output: 4

Explanation:

Choose the substring "abba".

    Remove "abba".
    The string becomes "aba", which is a palindrome.
    Therefore, "abba" is almost-palindromic.

Example 3:

Input: s = "zzabba"

Output: 5

Explanation:

Choose the substring "zzabba".

    Remove "zabba".
    The string becomes "abba", which is a palindrome.
    Therefore, "zabba" is almost-palindromic.

 

Constraints:

    2 <= s.length <= 2500
    s consists of only lowercase English letters.

Algorithm
1. Use Dynamic Programming with two tables:

   A. pal[i][j]:
      - True if substring s[i...j] is a palindrome

   B. almost[i][j]:
      - True if substring s[i...j] becomes a palindrome
        after removing exactly one character

2. Build pal table:
   - Single character is always palindrome
   - For s[i] == s[j]:
       pal[i][j] = True if:
         - length == 2 OR
         - inner substring pal[i+1][j-1] is True

3. Build almost table:

   Case 1: s[i] == s[j]
       - deletion must happen inside
       almost[i][j] = almost[i+1][j-1]

   Case 2: s[i] != s[j]
       - we must delete one of the ends
       almost[i][j] = pal[i+1][j] OR pal[i][j-1]

4. Base cases:
   - length 1 → valid (remove it → empty palindrome)
   - length 2 → valid (remove one → 1-char palindrome)

5. Track maximum valid length

Complexity
Time Complexity: O(n^2)
Space Complexity: O(n^2)

'''
class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)

        # ----------------------------------------
        # Step 1: Build palindrome table
        # pal[i][j] = 1 if s[i..j] is palindrome
        # ----------------------------------------
        pal = [bytearray(n) for _ in range(n)]

        # Fill from bottom to top
        for i in range(n - 1, -1, -1):
            pal[i][i] = 1  # single character is palindrome
            si = s[i]
            row = pal[i]

            for j in range(i + 1, n):
                # Check if characters match and inside is palindrome
                if si == s[j] and (j - i == 1 or pal[i + 1][j - 1]):
                    row[j] = 1

        # ----------------------------------------
        # Step 2: Build almost-palindromic table
        # almost[i][j] = 1 if s[i..j] becomes palindrome
        # after removing exactly one character
        # ----------------------------------------
        almost = [bytearray(n) for _ in range(n)]

        ans = 1  # minimum answer

        # Base case: length 1
        for i in range(n):
            almost[i][i] = 1

        # Base case: length 2
        for i in range(n - 1):
            almost[i][i + 1] = 1
            ans = 2

        # ----------------------------------------
        # Step 3: Fill DP for length >= 3
        # ----------------------------------------
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Case 1: characters match
                if s[i] == s[j]:
                    # deletion must happen inside
                    if almost[i + 1][j - 1]:
                        almost[i][j] = 1
                        ans = length

                # Case 2: characters do not match
                else:
                    # delete one of the ends
                    if pal[i + 1][j] or pal[i][j - 1]:
                        almost[i][j] = 1
                        ans = length

        return ans