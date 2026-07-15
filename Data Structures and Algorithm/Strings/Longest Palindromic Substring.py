class Solution:

    # Expand around the given center and return
    # the longest palindrome for that center.
    def isPal(self, s, l, r):

        # Expand while the characters match
        # and both pointers stay within the string.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        # After the loop, l and r have moved one step beyond
        # the valid palindrome, so return the valid substring.
        return s[l + 1:r]

    def longestPalindrome(self, s: str) -> str:

        # Stores the longest palindrome found so far.
        result = ""

        # Treat every index as the center of a palindrome.
        for i in range(len(s)):

            # Case 1: Odd-length palindrome
            # Center is a single character.
            temp = self.isPal(s, i, i)

            # Update the answer if a longer palindrome is found.
            if len(temp) > len(result):
                result = temp

            # Case 2: Even-length palindrome
            # Center lies between two characters.
            temp = self.isPal(s, i, i + 1)

            # Update the answer if a longer palindrome is found.
            if len(temp) > len(result):
                result = temp

        # Return the longest palindromic substring.
        return result
        
'''
Algorithm

1. Initialize an empty string to store the longest palindrome found.

2. Traverse every index of the string.

3. Treat the current index as the center of an odd-length palindrome.
   - Expand outward while both characters are equal.
   - Update the longest palindrome if a longer one is found.

4. Treat the gap between the current index and the next index as the center of an even-length palindrome.
   - Expand outward while both characters are equal.
   - Update the longest palindrome if a longer one is found.

5. Continue until every possible center has been processed.

6. Return the longest palindromic substring.

Pattern:
Expand Around Center

Time Complexity: O(n²)
Space Complexity: O(1)

'''