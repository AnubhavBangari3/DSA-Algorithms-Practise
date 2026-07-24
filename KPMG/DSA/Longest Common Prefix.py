class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mi=min(strs)
        ma=max(strs)
        ans=0

        for i in range(min(len(mi),len(ma))):
            if mi[i] != ma[i]:
                break
            else:
                ans+=1
        return mi[:ans]
        
'''
Algorithm

1. Find the lexicographically smallest string in the array.

2. Find the lexicographically largest string in the array.

3. Compare both strings character by character from the beginning.

4. Continue while the characters are the same.

5. Stop when:
   - A mismatch is found, or
   - The end of either string is reached.

6. Return the common prefix formed up to that point.

Pattern:
String Comparison + Lexicographical Ordering

Time Complexity: O(n × m)
Space Complexity: O(1)
'''