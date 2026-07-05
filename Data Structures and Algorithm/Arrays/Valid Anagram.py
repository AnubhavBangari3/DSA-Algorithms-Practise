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
1) Compare the lengths of both strings.
2) If the lengths are different, return False since they cannot be anagrams.
3) Create two hash maps to store the frequency of each character.
4) Traverse the first string and count the occurrences of each character.
5) Traverse the second string and count the occurrences of each character.
6) Compare the two frequency maps.
7) If both maps are identical, return True; otherwise, return False.

'''