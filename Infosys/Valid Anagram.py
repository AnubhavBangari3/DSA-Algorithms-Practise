'''
Algorithm: Valid Anagram (Hash Map / Frequency Counting)

1. Check if the lengths of s and t are different.
   - If yes, return False.
2. Initialize two empty dictionaries: count_s and count_t.
3. Iterate through string s:
   - Count the frequency of each character in count_s.
4. Iterate through string t:
   - Count the frequency of each character in count_t.
5. Compare both dictionaries.
6. Return True if both dictionaries are equal, otherwise False.

Time Complexity: O(n)
Space Complexity: O(k), where k is the number of distinct characters.

'''

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t