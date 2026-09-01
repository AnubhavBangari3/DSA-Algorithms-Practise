
'''
1. Use **DFS + Memoization**.
2. At every step, try each word from `wordDict`.
3. If the current string starts with that word:
   - Remove that prefix.
   - Recursively check the remaining suffix.
4. If any recursive call returns `True`, return `True`.
5. If the string becomes empty, return `True`.
6. Store results in `memo` so the same substring is not solved again.
7. If no word works, return `False`.

Complexity
Time Complexity: approximately O(n × m × k)
Space Complexity: O(n)
'''


class Solution:

    def helper(self, s, wordDict, memo):

        # Entire string successfully segmented
        if not s:
            return True

        # Already calculated
        if s in memo:
            return memo[s]

        # Try every dictionary word
        for word in wordDict:

            # Current string starts with this word
            if s[:len(word)] == word:

                # Remaining part of string
                suffix = s[len(word):]

                # Recursively check remaining suffix
                if self.helper(suffix, wordDict, memo):
                    memo[s] = True
                    return True

        # No valid segmentation found
        memo[s] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Memoization dictionary
        memo = {}

        return self.helper(s, wordDict, memo)