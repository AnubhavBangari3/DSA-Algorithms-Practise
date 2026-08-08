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
1. If the lengths are different, return `False`.
2. Create two dictionaries for character frequencies.
3. Count each character in `s`.
4. Count each character in `t`.
5. Compare both dictionaries.
6. If they are equal, return `True`; otherwise return `False`.

- **Time:** O(n)
- **Space:** O(n)

'''