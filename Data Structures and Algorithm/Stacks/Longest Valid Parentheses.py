class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Push -1 as a dummy index.
        # It acts as the starting point for the first valid substring.
        stack = [-1]

        # Stores the maximum valid parentheses length found.
        max_len = 0

        # Traverse every character.
        for i in range(len(s)):

            # If it is an opening bracket,
            # store its index.
            if s[i] == "(":
                stack.append(i)

            else:
                # Try to match this ')' with
                # the latest '('.
                stack.pop()

                # If the stack becomes empty,
                # this ')' has no matching '('.
                # Make this index the new base.
                if len(stack) == 0:
                    stack.append(i)

                else:
                    # Current valid substring starts
                    # after the index at the top of the stack.
                    current_length = i - stack[-1]

                    # Update the maximum length.
                    max_len = max(max_len, current_length)

        return max_len

'''
Algorithm

1. Create a stack and push -1 into it.
2. Initialize max_length = 0.
3. Traverse the string.
4. If the current character is '(':
   - Push its index onto the stack.
5. Otherwise, the character is ')':
   - Pop one index from the stack.
6. If the stack becomes empty:
   - Push the current index.
   - This becomes the new starting point.
7. Otherwise:
   - Calculate the current valid length as:
       current index - stack top.
   - Update the maximum length.
8. Return the maximum length.

Pattern:
Stack

Time Complexity: O(n)

Space Complexity: O(n)

'''