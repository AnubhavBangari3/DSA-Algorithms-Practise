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
    
'''
Algorithm

1. Create a mapping of each digit to its corresponding letters.
2. Initialize an empty list to store all combinations.
3. Start backtracking from the first digit.
4. For the current digit:
   - Try every possible letter mapped to that digit.
5. Append the chosen letter to the current combination.
6. Recursively process the next digit.
7. If the current combination length equals the number of digits:
   - Add it to the result.

8. Return all generated combinations.

Pattern:
Backtracking

Time Complexity: O(4^n × n)

Space Complexity: O(n) (excluding the output)

'''