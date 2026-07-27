from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        # Store the indices of all Radiant senators.
        rQue = deque()
        # Store the indices of all Dire senators.
        dQue = deque()

        # Separate senators into their respective queues.
        for index, party in enumerate(senate):
            if party == "R":
                rQue.append(index)
            else:
                dQue.append(index)

        # Continue until one party has no senators left.
        while rQue and dQue:

            # The senator with the smaller index
            # gets to act first.
            r = rQue.popleft()
            d = dQue.popleft()

            # Radiant acts first and bans Dire.
            if r < d:
                # Radiant survives to the next round.
                rQue.append(r + n)

            # Dire acts first and bans Radiant.
            else:
                # Dire survives to the next round.
                dQue.append(d + n)

        # The remaining queue is the winner.
        if rQue:
            return "Radiant"
        else:
            return "Dire"

'''
Algorithm

1. Create two queues:
   - One for Radiant senators.
   - One for Dire senators.

2. Store the index of every senator
   in its respective queue.

3. While both queues are not empty:

   a. Remove the front senator
      from both queues.

   b. Compare their indices.

   c. The senator with the smaller index
      gets to act first.

   d. That senator bans the opponent.

   e. The winning senator survives and
      is added back for the next round
      using:
      current index + n

4. When one queue becomes empty,
   the other party wins.

Pattern:
Queue Simulation

Time Complexity: O(n)

Space Complexity: O(n)
'''