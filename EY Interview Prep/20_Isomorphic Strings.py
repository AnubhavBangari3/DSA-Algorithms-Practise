'''
205. Isomorphic Strings
Solved
Easy
Topics
premium lock iconCompanies

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

    Mapping 'e' to 'a'.
    Mapping 'g' to 'd'.

Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

   

'''

'''
1. Create a dictionary to map characters from `s` to `t`.
2. Traverse both strings together.
3. If a character from `s` is not mapped:
   - Check whether the character from `t` is already mapped by another character.
   - If yes, return `False`.
   - Otherwise, create the mapping.
4. If the character from `s` is already mapped:
   - Check whether it maps to the current character in `t`.
   - If not, return `False`.
5. If all characters follow the same mapping, return `True`.

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionary: character in s -> character in t
        mapping = {}
        # Traverse both strings
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            # If c1 is not mapped yet
            if c1 not in mapping:
                # c2 cannot already belong to another character
                if c2 in mapping.values():
                    return False
                # Create mapping
                mapping[c1] = c2

            # Existing mapping must remain consistent
            elif mapping[c1] != c2:
                return False

        return True

'''
Complexity
Time Complexity: O(n²) in this exact implementation
c2 in mapping.values() may take O(n) and is done inside the loop.
Space Complexity: O(n)
Dictionary stores character mappings.
'''