'''
1. Find triplets that **cannot be used**.
2. A triplet is invalid if any value is greater than its corresponding target value.
3. Store the indices of invalid triplets in `check`.
4. For all valid triplets, take the maximum of each position.
5. Finally check whether `[a, b, c]` equals `target`.

Complexity
Time Complexity: O(n)
Space Complexity: O(n) because of the check set.
'''

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        # Store indices of unusable triplets
        check = set()

        # Find triplets that exceed target
        for i, [x, y, z] in enumerate(triplets):

            if (
                x > target[0]
                or y > target[1]
                or z > target[2]
            ):
                check.add(i)

        # Store merged maximum values
        a, b, c = 0, 0, 0

        # Merge only valid triplets
        for i, (x, y, z) in enumerate(triplets):

            if i not in check:

                a = max(a, x)
                b = max(b, y)
                c = max(c, z)

        # Check whether target was formed
        return [a, b, c] == target