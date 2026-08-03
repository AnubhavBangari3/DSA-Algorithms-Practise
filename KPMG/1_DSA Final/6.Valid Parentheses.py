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
1. Create an empty stack.

2. Create a mapping of each closing bracket to its matching opening bracket.

3. Traverse every character in the string.

4. If the character is an opening bracket:
   - Push it onto the stack.

5. Otherwise, it is a closing bracket:
   - If the stack is empty, return False.
   - Pop the top opening bracket.
   - If it does not match the current closing bracket, return False.

6. After processing all characters:
   - If the stack is empty, return True.
   - Otherwise, return False.


Time Complexity: O(n)
- Each bracket is pushed and popped at most once.

Space Complexity: O(n)
- In the worst case, all opening brackets are stored in the stack.

'''