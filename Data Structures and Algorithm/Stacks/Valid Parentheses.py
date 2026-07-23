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

