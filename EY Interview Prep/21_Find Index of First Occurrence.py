'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
premium lock iconCompanies

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

Constraints:

    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.



'''
'''
1. Traverse the `haystack` from left to right.
2. At every index `i`, take a substring having the same length as `needle`.
3. Compare that substring with `needle`.
4. If they are equal, return `i`.
5. Since we traverse from left to right, the first match is automatically the **first occurrence**.
6. If no match is found, return `-1`.

'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Check every possible starting position
        for i in range(len(haystack) - len(needle) + 1):

            # Take substring of same length as needle
            if haystack[i:i + len(needle)] == needle:

                # First occurrence found
                return i

        # Needle not found
        return -1

'''
Complexity

Let:

n = length of haystack
m = length of needle
Time Complexity: O(n × m)
At each position, we may compare up to m characters.
Space Complexity: O(m) in Python
Slicing haystack[i:i+m] creates a new substring.

'''