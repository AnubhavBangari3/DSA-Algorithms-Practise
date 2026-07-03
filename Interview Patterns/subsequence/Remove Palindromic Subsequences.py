class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
    
'''
1) Check if the whole string s is already a palindrome.
2) If yes, return 1.
3) Otherwise, return 2.

'''