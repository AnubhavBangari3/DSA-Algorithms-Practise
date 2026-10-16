'''
Algorithm: Longest Common Prefix (Lexicographical Min-Max)

1. Find the lexicographically smallest string: mi = min(strs).
2. Find the lexicographically largest string: ma = max(strs).
3. Initialize longest = 0 to track the common prefix length.
4. Iterate up to min(len(mi), len(ma)).
5. Compare characters at the same index:
   - If mi[i] != ma[i], break the loop.
   - Otherwise, increment longest by 1.
6. Return mi[:longest] as the longest common prefix.

Time Complexity: O(n * m), where n is the number of strings and m is the maximum string length.
Space Complexity: O(m) for the returned prefix; O(1) auxiliary space.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        mi = min(strs)
        ma = max(strs)

        longest = 0


        for i in range(min(len(mi), len(ma))):
            if mi[i] != ma[i]:
                break
            longest += 1

        return mi[:longest]