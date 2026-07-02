'''
2116. Check if a Parentheses String Can Be Valid
Medium
Topics
premium lock iconCompanies
Hint

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:

Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.

Example 4:

Input: s = "(((())(((())", locked = "111111010111"
Output: true
Explanation: locked permits us to change s[6] and s[8]. 
We change s[6] and s[8] to ')' to make s valid.

 

Constraints:

    n == s.length == locked.length
    1 <= n <= 105
    s[i] is either '(' or ')'.
    locked[i] is either '0' or '1'.


Algorithm

1. If length of string is odd:
   return False
   because a valid parentheses string must have even length

2. Left to Right pass:
   - Maintain balance = 0
   - Traverse string from left to right
   - If current character is '(' or unlocked:
       balance += 1
     Else:
       balance -= 1

   - If balance becomes negative at any point:
       return False

3. Right to Left pass:
   - Reset balance = 0
   - Traverse string from right to left
   - If current character is ')' or unlocked:
       balance += 1
     Else:
       balance -= 1

   - If balance becomes negative at any point:
       return False

4. If both passes succeed:
   return True

Complexity

Time Complexity:
O(n)

Reason:
We traverse the string twice

Space Complexity:
O(1)

Reason:
We only use a few variables
'''
class Solution:
    def canBeValid(self, s, locked):
        n = len(s)
        
        # Valid parentheses string must have even length
        if n % 2 != 0:
            return False
        
        # Pass 1: Left to Right
        # Make sure we never have too many ')'
        balance = 0
        for i in range(n):
            # If current is '(' or can be changed, treat it as '('
            if s[i] == '(' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            
            # Too many closing brackets
            if balance < 0:
                return False
        
        # Pass 2: Right to Left
        # Make sure we never have too many '('
        balance = 0
        for i in range(n - 1, -1, -1):
            # If current is ')' or can be changed, treat it as ')'
            if s[i] == ')' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            
            # Too many opening brackets
            if balance < 0:
                return False
        
        return True