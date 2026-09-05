'''
1. Keep two values:
   - `low` → minimum possible open brackets.
   - `high` → maximum possible open brackets.
2. For `(` → increase both.
3. For `)` → decrease both.
4. For `*`:
   - Treat as `)` for `low`.
   - Treat as `(` for `high`.
5. If `high < 0`, there are too many `)` → `False`.
6. Keep `low >= 0`.
7. Finally, `low == 0` means all brackets can be balanced.

Complexity
Time: O(n)
Space: O(1)
'''

class Solution:
    def checkValidString(self, s):

        # Minimum and maximum possible open brackets
        low = 0
        high = 0

        for ch in s:

            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                # '*' can act as ')' for minimum
                low -= 1

                # '*' can act as '(' for maximum
                high += 1

            # Too many closing brackets
            if high < 0:
                return False

            # Open brackets cannot be negative
            low = max(low, 0)

        # Check if all open brackets can be closed
        return low == 0