from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)

        for s in strs:
            k="".join(sorted(s))
            d[k].append(s)
        return list(d.values())

        
'''
1) Create an empty hash map where:
2) Key = canonical representation of a string.
3) Value = list of strings belonging to that group.
4) Traverse each string in the input array.
5) Sort the characters of the current string to create its canonical form.
6) Use the sorted string as the key and append the original string to its corresponding list.
7) After processing all strings, return all the grouped lists.
'''