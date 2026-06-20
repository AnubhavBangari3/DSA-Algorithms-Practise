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
 
Algorithm
1. If lengths of s and t are different:
   return False

2. Count frequency of each character in s.

3. Count frequency of each character in t.

4. Compare both frequency maps.

5. If maps are equal:
   return True

6. Otherwise:
   return False

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
Time Complexity:
O(n)

Reason:
We traverse both strings once.

Space Complexity:
O(1)

Reason:
Only 26 lowercase English letters.
(Technically O(26))

'''