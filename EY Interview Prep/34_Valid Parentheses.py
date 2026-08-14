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



'''

'''
1. Create a **stack** to store opening brackets.
2. Create a mapping of closing brackets to their matching opening brackets.
3. Traverse every character in the string.
4. If it is an opening bracket:
   - Push it onto the stack.
5. If it is a closing bracket:
   - If the stack is empty, return `False`.
   - Pop the top opening bracket.
   - Check whether it matches the closing bracket.
6. If they don't match, return `False`.
7. At the end, the stack must be empty.
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
Complexity
Time Complexity: O(n)
We traverse the string once.
Space Complexity: O(n)
In the worst case, all characters can be opening brackets.
'''