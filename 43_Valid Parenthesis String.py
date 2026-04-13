'''
678. Valid Parenthesis String
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

 

Constraints:

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.


Algorithm
1. Initialize two variables:
   low = 0   → minimum possible open brackets
   high = 0  → maximum possible open brackets

2. Traverse each character in string:

   If character == '(':
       low += 1
       high += 1

   If character == ')':
       low -= 1
       high -= 1

   If character == '*':
       # '*' can be '(', ')' or empty
       low -= 1      (treat as ')')
       high += 1     (treat as '(')

   If high < 0:
       return False   (too many closing brackets)

   If low < 0:
       low = 0        (we cannot have negative open brackets)

3. After traversal:
   If low == 0:
       return True
   Else:
       return False

Time Complexity:
O(n) → single pass

Space Complexity:
O(1) → no extra space

'''

class Solution:
    def checkValidString(self, s):
        # low = minimum open brackets possible
        # high = maximum open brackets possible
        low = 0
        high = 0
        
        for ch in s:
            
            if ch == '(':
                # Must increase both
                low += 1
                high += 1
            
            elif ch == ')':
                # Must decrease both
                low -= 1
                high -= 1
            
            else:  # ch == '*'
                # '*' can be ')', '(' or empty
                low -= 1      # treat as ')'
                high += 1     # treat as '('
            
            # If too many closing brackets
            if high < 0:
                return False
            
            # low should not go below 0
            if low < 0:
                low = 0
        
        # Valid if we can close all open brackets
        return low == 0