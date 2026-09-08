'''
1. Create a mapping from each digit to its letters.
2. Use **Backtracking**.
3. Start from the first digit.
4. For the current digit, try every possible letter.
5. Add that letter to the current combination and move to the next digit.
6. When the combination length equals the number of digits, add it to `result`.
7. Return all combinations.

Complexity
Time: O(4^n × n)
Space: O(n) recursion space, excluding output.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Mapping of digits to their corresponding letters.
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Stores all possible letter combinations.
        result = []

        # Backtracking function.
        # index -> current digit being processed.
        # current -> current combination being built.
        def backtrack(index, current):

            # If a letter has been chosen for every digit,
            # store the completed combination.
            if len(current) == len(digits):
                result.append(current)
                return

            # Try every possible letter corresponding
            # to the current digit.
            for letter in phone[digits[index]]:
                backtrack(index + 1, current + letter)

        # Handle the empty input case.
        if digits:
            backtrack(0, "")

        return result