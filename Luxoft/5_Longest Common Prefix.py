class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Find the lexicographically smallest string.
        smallest = min(strs)

        # Find the lexicographically largest string.
        largest = max(strs)

        # Length of the common prefix.
        prefix_length = 0

        # Compare both strings character by character.
        for i in range(min(len(smallest), len(largest))):

            # Stop when characters differ.
            if smallest[i] != largest[i]:
                break

            # Current character matches.
            prefix_length += 1

        # Return the common prefix.
        return smallest[:prefix_length]