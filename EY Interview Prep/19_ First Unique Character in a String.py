'''
387. First Unique Character in a String
Solved
Easy
Topics
premium lock iconCompanies

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.


    


'''
'''
1. Create a dictionary to store the frequency of each character.
2. Traverse the string and count every character.
3. Traverse the string again from left to right.
4. Find the first character whose frequency is `1`.
5. Return its index.
6. If no unique character exists, return `-1`.

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Dictionary to store character frequencies
        freq = {}

        # First pass: count every character
        for ch in s:

            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        # Second pass: find first unique character
        for i in range(len(s)):

            # Character appears only once
            if freq[s[i]] == 1:
                return i

        # No unique character found
        return -1

'''
Complexity
Time Complexity: O(n)
We traverse the string twice.
Space Complexity: O(1)
The string contains only lowercase English letters, so the dictionary can contain at most 26 characters.

'''