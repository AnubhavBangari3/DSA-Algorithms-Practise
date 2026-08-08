from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary where sorted string -> list of anagrams
        groups = defaultdict(list)

        # Traverse every string
        for s in strs:

            # Sort the string to create a common key
            key = "".join(sorted(s))

            # Add original string to its anagram group
            groups[key].append(s)

        # Return all groups
        return list(groups.values())

'''
1. Create a dictionary where each key stores a list of anagrams.
2. Traverse every string.
3. Sort the characters of the string.
4. Use the sorted string as the dictionary key.
5. Add the original string to that key's list.
6. Return all the dictionary values.

- **Space:** O(n × k)
- **Time:** O(n × k log k)

'''