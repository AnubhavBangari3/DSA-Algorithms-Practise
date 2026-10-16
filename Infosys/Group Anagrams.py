'''
Algorithm: Group Anagrams (Hash Map + Sorting)

1. Initialize a defaultdict(list) named groups to store anagram groups.
2. Iterate through each string s in strs.
3. Sort the characters of s and join them to create a key.
4. Use the sorted string as the dictionary key.
5. Append the original string s to groups[key].
6. Repeat until all strings are processed.
7. Return list(groups.values()) containing all grouped anagrams.

Time Complexity: O(n * k log k), where n is the number of strings and k is the maximum string length.
Space Complexity: O(n * k) for storing the grouped strings and keys.
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())