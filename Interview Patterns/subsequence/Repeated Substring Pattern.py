class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:]+s[:-1]

'''
Algorithm
Create a new string by concatenating the original string with itself.
Remove the first and last characters from this doubled string.
Search for the original string inside the modified string.
If the original string is found, return True; otherwise, return False.

'''