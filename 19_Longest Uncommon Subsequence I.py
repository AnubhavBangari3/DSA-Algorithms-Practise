'''
521. Longest Uncommon Subsequence I
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a of exactly one of them.

 

Example 1:

Input: a = "aba", b = "cdc"
Output: 3
Explanation: One longest uncommon subsequence is "aba" because "aba" is a subsequence of "aba" but not "cdc".
Note that "cdc" is also a longest uncommon subsequence.

Example 2:

Input: a = "aaa", b = "bbb"
Output: 3
Explanation: The longest uncommon subsequences are "aaa" and "bbb".

Example 3:

Input: a = "aaa", b = "aaa"
Output: -1
Explanation: Every subsequence of string a is also a subsequence of string b. Similarly, every subsequence of string b is also a subsequence of string a. So the answer would be -1.

 

Constraints:

    1 <= a.length, b.length <= 100
    a and b consist of lower-case English letters.


    
Algorithm:

1. Compare the two strings a and b.

2. If both strings are equal:
   - return -1
   - because every subsequence of one string will also be a subsequence of the other

3. If both strings are different:
   - return the length of the longer string
   - because the whole string itself will be an uncommon subsequence


Complexity:

Time Complexity: O(n)
- Comparing the two strings can take O(n)

Space Complexity: O(1)
- No extra space is used


'''

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))