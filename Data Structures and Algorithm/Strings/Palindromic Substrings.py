class Solution:
    def isPal(self,s,l,r):
        ans=0
        while l>=0 and r <len(s) and s[l] == s[r]:
            l-=1
            r+=1
            ans+=1
        return ans

    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            #Odd
            ans+=self.isPal(s,i,i)
            #Even
            ans+=self.isPal(s,i,i+1)
        return ans        
    
'''
Algorithm

1. Initialize the total palindrome count as 0.
2. Treat every index as the center of a possible odd-length palindrome.
3. For each index i:
   - Set left = i and right = i.
   - Expand both pointers outward while:
     - left and right remain inside the string.
     - s[left] == s[right].
   - Count every valid expansion as one palindromic substring.

4. Treat every gap between two characters as the center of a possible even-length palindrome.
5. For each index i:
   - Set left = i and right = i + 1.
   - Expand outward while both characters are equal and indices are valid.
   - Count every valid expansion.
6. Add the odd-length and even-length palindrome counts.
7. Return the total count.

Pattern:
Expand Around Center

Time Complexity: O(n²)
Space Complexity: O(1)

'''