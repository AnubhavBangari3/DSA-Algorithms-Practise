class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert the string into a list because
        # strings are immutable in Python.
        s = list(s)
        # Stack stores the indices of unmatched '('.
        stack = []
        # Traverse every character.
        for index, char in enumerate(s):
            # Store the index of every opening bracket.
            if char == '(':
                stack.append(index)
            # Process every closing bracket.
            elif char == ')':
                # If there is a matching '(',
                # remove it from the stack.
                if stack:
                    stack.pop()
                # Otherwise, this ')' is invalid.
                # Mark it for removal.
                else:
                    s[index] = ''
        # Any '(' left in the stack are unmatched.
        # Mark them for removal.
        while stack:
            s[stack.pop()] = ''

        # Join the remaining characters
        # to form the valid string.
        return ''.join(s)

'''
Algorithm

1. Convert the string into a list.

2. Create an empty stack to store the indices
   of opening parentheses '('.

3. Traverse every character in the string.

4. If the character is '(':
   - Push its index onto the stack.

5. If the character is ')':
   - If the stack is not empty:
       - Pop one opening parenthesis because
         a valid pair is formed.
   - Otherwise:
       - Mark this ')' for removal.

6. After the traversal,
   all indices left in the stack represent
   unmatched '('.

7. Mark all unmatched '(' for removal.

8. Join the remaining characters
   and return the final string.

Pattern:
Stack

Time Complexity: O(n)

Space Complexity: O(n)

'''