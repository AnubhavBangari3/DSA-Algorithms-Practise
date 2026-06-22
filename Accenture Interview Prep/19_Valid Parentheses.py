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

1. Create an empty stack.

2. Create a hashmap:
   ')' -> '('
   '}' -> '{'
   ']' -> '['

3. Traverse each character:

   If character is an opening bracket:
      push into stack

   Else (closing bracket):

      If stack is empty:
         return False

      Pop top element

      If popped bracket != expected opening bracket:
         return False

4. After traversal:

   If stack is empty:
      return True

   Else:
      return False

'''
class Solution:
    def isValid(self, s):
        # Stack to store opening brackets
        stack = []
        # Mapping of closing to opening brackets
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        # Traverse every character
        for ch in s:
            # Opening bracket
            if ch in "([{":
                stack.append(ch)
            # Closing bracket
            else:
                # No opening bracket available
                if not stack:
                    return False
                # Pop last opening bracket
                top = stack.pop()

                # Check if brackets match
                if top != pairs[ch]:
                    return False
        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0
'''
Time Complexity:
O(n)

Reason:
Each bracket is pushed and popped at most once.

Space Complexity:
O(n)

Reason:
Stack may store all opening brackets.

'''