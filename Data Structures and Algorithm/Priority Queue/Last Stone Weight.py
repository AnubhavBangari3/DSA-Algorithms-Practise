class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Continue until only one or no stone remains.
        while len(stones) > 1:

            # Sort the stones so the two heaviest
            # stones are at the end.
            stones.sort()

            # Pick the two heaviest stones.
            x = stones[-2]
            y = stones[-1]

            # Remove the two heaviest stones.
            stones = stones[:-2]

            # If their weights are different,
            # add the remaining weight back.
            if x != y:
                stones.append(y - x)

        # Return the last remaining stone,
        # or 0 if no stones remain.
        return stones[0] if stones else 0
'''
Algorithm
1. While more than one stone exists:
   a. Sort the stones.
   b. Pick the two heaviest stones.
   c. Remove both stones.
   d. If their weights are different:
      - Insert the difference back.

2. Repeat until one or no stone remains.
3. If one stone remains:
   - Return its weight.
4. Otherwise:
   - Return 0.

Pattern:
Simulation

Time Complexity:
O(n² log n)

Space Complexity:
O(1)

'''