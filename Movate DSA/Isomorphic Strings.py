class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Store mapping from s character -> t character
        mapping = {}

        # Traverse both strings
        for i in range(len(s)):

            c1 = s[i]
            c2 = t[i]

            # If c1 is not mapped yet
            if c1 not in mapping:

                # Two different characters cannot map to same character
                if c2 in mapping.values():
                    return False

                # Create mapping
                mapping[c1] = c2

            # If c1 already maps to a different character
            elif mapping[c1] != c2:
                return False

        return True
'''


'''