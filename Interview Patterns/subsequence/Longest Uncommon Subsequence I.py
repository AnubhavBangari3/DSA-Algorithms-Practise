class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else: 
            return max(len(a), len(b))
        
'''
Check if both strings a and b are equal. If they are, then there is no uncommon subsequence between them, so return -1.
If both strings a and b are not equal, then the longest uncommon subsequence would be the longest string among a and b. Because any subsequence of the longer string that is also a subsequence of the shorter string cannot be uncommon. Hence, return the length of the longest string between a and b.

'''