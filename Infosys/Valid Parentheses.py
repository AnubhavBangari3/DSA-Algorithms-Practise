'''
Algorithm: Valid Parentheses (Stack)

1. Initialize an empty stack to store opening brackets.
2. Create a dictionary 'pairs' mapping closing brackets to opening brackets.
3. Iterate through each character ch in the string.
4. If ch is an opening bracket, push it onto the stack.
5. Otherwise, if the stack is empty, return False.
6. Pop the top element from the stack.
7. If the popped element does not match pairs[ch], return False.
8. After traversal, return True if the stack is empty, otherwise False.

Time Complexity: O(n)
Space Complexity: O(n)

'''


class Solution:
    def isValid(self, s):

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()

                if top != pairs[ch]:
                    return False
        return len(stack) == 0