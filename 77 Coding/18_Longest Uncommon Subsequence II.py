'''
522. Longest Uncommon Subsequence II
Medium
Topics
premium lock iconCompanies

Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

    For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

 

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1

 

Constraints:

    2 <= strs.length <= 50
    1 <= strs[i].length <= 10
    strs[i] consists of lowercase English letters.


1. Sort the strings in descending order of length.

2. For each string strs[i]:
   - Assume it is uncommon
   - Compare it with every other string strs[j], where i != j
   - Check if strs[i] is a subsequence of strs[j]

3. If strs[i] is not a subsequence of any other string,
   return its length immediately

4. If no such string exists, return -1

Time Complexity: O(n^2 * L)
- n = number of strings
- L = maximum length of a string
- For every pair of strings, subsequence check takes O(L)

Since n <= 50 and L <= 10, this is efficient enough.

Space Complexity: O(1)
- Ignoring sorting space

'''

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(a: str, b: str) -> bool:
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            uncommon = True

            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    uncommon = False
                    break

            if uncommon:
                return len(strs[i])

        return -1