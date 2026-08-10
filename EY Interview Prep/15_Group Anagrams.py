'''
49. Group Anagrams
Solved
Medium
Topics
premium lock iconCompanies

Given an array of strings strs, group the together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.



'''
'''
1. Create a dictionary where:
   - **Key** = sorted version of the string.
   - **Value** = list of strings having that sorted form.
2. Loop through every string.
3. Sort each string to create a common key.
4. Add the original string to that key's list.
5. Return all the groups.

'''


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
Complexity

Let n = number of strings and k = maximum length of a string.

Time Complexity: O(n × k log k)
Sorting each string takes O(k log k).
Space Complexity: O(n × k)
Dictionary stores all the strings.

'''