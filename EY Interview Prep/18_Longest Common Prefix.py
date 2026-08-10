'''
14. Longest Common Prefix
Solved
Easy
Topics
premium lock iconCompanies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.




'''

'''
1. Find the lexicographically **smallest** string using `min()`.
2. Find the lexicographically **largest** string using `max()`.
3. Compare both strings character by character.
4. Continue while the characters are the same.
5. Stop when the characters differ.
6. Return the matching prefix.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Lexicographically smallest string
        mi = min(strs)
        # Lexicographically largest string
        ma = max(strs)
        # Length of the common prefix
        longest = 0

        # Compare characters of the smallest and largest strings
        for i in range(min(len(mi), len(ma))):
            # Stop when characters differ
            if mi[i] != ma[i]:
                break
            # Extend the common prefix length
            longest += 1

        # Return the common prefix
        return mi[:longest]

'''
Complexity

Let n = number of strings and m = average string length.

Time Complexity: O(n × m)
min() and max() compare the strings.
Then we compare the smallest and largest strings.
Space Complexity: O(1)
No extra data structure is used.

'''