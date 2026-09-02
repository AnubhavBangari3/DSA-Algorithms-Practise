'''
1. Use **DFS + Memoization** with two pointers:
   - `i` → current index in string `s`
   - `j` → current index in pattern `p`
2. If we reach the end of pattern:
   - Return `True` only if we also reached the end of string.
3. Check whether current characters match:

   `s[i] == p[j]` or `p[j] == '.'`

4. If the next pattern character is `'*'`, we have two choices:
   - Use `*` as **zero occurrences** → move pattern by 2.
   - Use `*` as **one or more occurrences** → consume one string character and keep pattern at same position.
5. Otherwise:
   - Current characters must match.
   - Move both pointers forward.
6. Memoize `(i, j)` to avoid repeated work.
Complexity
Time Complexity: O(m × n)
Space Complexity: O(m × n)
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Memoization: (string index, pattern index)
        memo = {}

        def dfs(i, j):

            # Already solved
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Check current character match
            first_match = (
                i < len(s)
                and (
                    s[i] == p[j]
                    or p[j] == "."
                )
            )

            # Next pattern character is *
            if j + 1 < len(p) and p[j + 1] == "*":

                # Option 1: Use zero occurrences
                # Option 2: Use one/more occurrences
                result = (
                    dfs(i, j + 2)
                    or (
                        first_match
                        and dfs(i + 1, j)
                    )
                )

            else:

                # Normal character or .
                result = (
                    first_match
                    and dfs(i + 1, j + 1)
                )

            memo[(i, j)] = result
            return result

        return dfs(0, 0)