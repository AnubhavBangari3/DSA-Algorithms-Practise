'''
20. Valid Parentheses
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


Algorithm

1. Initialize an empty stack

2. Create a mapping of closing → opening brackets:
   ) → (
   } → {
   ] → [

3. Traverse each character in string:
   
   If character is opening bracket:
       push it into stack

   Else (closing bracket):
       If stack is empty:
           return False
       
       If top of stack != matching opening bracket:
           return False
       
       Else:
           pop from stack

4. After traversal:
   If stack is empty:
       return True
   Else:
       return False

Complexity

Time Complexity:
O(n) → traverse string once

Space Complexity:
O(n) → stack in worst case (all opening brackets)


'''

class Solution:
    def isValid(self, s):
        # Stack to store opening brackets
        stack = []
        
        # Mapping of closing to opening brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Traverse each character
        for ch in s:
            
            # If opening bracket → push
            if ch in '({[':
                stack.append(ch)
            
            else:
                # If stack empty → no matching opening
                if not stack:
                    return False
                
                # Check if top matches
                if stack[-1] != mapping[ch]:
                    return False
                
                # Pop matched opening
                stack.pop()
        
        # If stack empty → valid
        return len(stack) == 0