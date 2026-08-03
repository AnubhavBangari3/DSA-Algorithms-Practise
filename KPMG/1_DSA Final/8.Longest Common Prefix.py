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
1. Find the lexicographically smallest string.

2. Find the lexicographically largest string.

3. Compare both strings character by character.

4. Continue while the characters are the same.

5. Stop at the first mismatch.

6. Return the substring from index 0 to the matched length.

Why does this work?
- After sorting lexicographically, the maximum difference between strings
  is represented by the smallest and largest strings.
- If these two share a prefix, every string in between must also share it.


Time Complexity: O(n * m)

- Finding min() and max() compares strings lexicographically.
- n = number of strings
- m = average length of a string

Space Complexity: O(1)

- No extra data structures are used.
'''