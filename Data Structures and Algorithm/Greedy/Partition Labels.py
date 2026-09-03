'''
1. Store the **last occurrence** of every character.
2. Keep:
   - `start` → starting index of current partition.
   - `end` → farthest last occurrence needed by current partition.
3. Traverse the string.
4. For every character:

   `end = max(end, last[c])`

5. If `i == end`, all characters in the current partition end here.
6. Store the partition size:

   `end - start + 1`

7. Start the next partition from `i + 1`.

Complexity
Time Complexity: O(n)
Space Complexity: O(1) because there are only 26 lowercase letters.
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # Store last occurrence of each character
        last = {
            c: i
            for i, c in enumerate(s)
        }

        start = 0
        end = 0

        output = []

        # Traverse the string
        for i, c in enumerate(s):

            # Extend partition if current character
            # appears later in the string
            end = max(end, last[c])

            # Current partition is complete
            if i == end:

                # Store partition length
                output.append(end - start + 1)

                # Start next partition
                start = i + 1

        return output