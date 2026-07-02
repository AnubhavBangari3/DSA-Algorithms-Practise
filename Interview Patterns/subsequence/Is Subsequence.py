class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r=0,0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l+=1
            r+=1
        
        if l== len(s):
            return True
        return False

'''
ALGORITHM

1) Initialize 2 pointers
   One for s and other for t
2) Traverse string t from left to right
3) For each character in t
   Compare each character with s
   If they match, move the pointer in s to next character
   Always move the pointer in t
4) Continue Until
   All characters of s has been matched or
   t has been completely traversed
5) if the pointer in s has reached end , return true
   else return false

'''