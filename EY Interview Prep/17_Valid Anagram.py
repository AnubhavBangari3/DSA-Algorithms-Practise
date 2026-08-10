'''
242. Valid Anagram
Solved
Easy
Topics
premium lock iconCompanies

Given two strings s and t, return true if t is an of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


'''

'''
1. If the lengths of `s` and `t` are different, return `False`.
2. Create two dictionaries to store character frequencies.
3. Count the frequency of every character in `s`.
4. Count the frequency of every character in `t`.
5. Compare both dictionaries.
6. If they are equal, the strings are anagrams.

'''

class Solution:
    def isAnagram(self, s, t):

        # Different lengths can never be anagrams
        if len(s) != len(t):
            return False

        # Store character frequencies
        count_s = {}
        count_t = {}

        # Count characters in both strings
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        # Compare frequency maps
        return count_s == count_t

'''
Complexity
Time Complexity: O(n)
We traverse both strings once.
Space Complexity: O(n)
Dictionaries store character frequencies.
For only lowercase English letters, it can also be considered O(1) because there are only 26 possible characters.

'''