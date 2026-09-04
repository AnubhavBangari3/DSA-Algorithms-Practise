'''
1. `trip_tank` → total gas remaining for the complete journey.
2. `curr_tank` → gas remaining from the current starting station.
3. Traverse every station and calculate:

   `gas[i] - cost[i]`

4. If `curr_tank < 0`, we cannot start from the current `start`.
5. Set the next station as the new starting point and reset `curr_tank`.
6. If total `trip_tank >= 0`, return `start`. Otherwise return `-1`.


Complexity
Time: O(n)
Space: O(1)
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        trip_tank = 0
        curr_tank = 0
        start = 0
        n = len(gas)

        for i in range(n):

            # Gas remaining after travelling from station i
            trip_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # Cannot continue from current starting point
            if curr_tank < 0:

                # Try starting from next station
                start = i + 1
                curr_tank = 0

        # Total gas must be enough for total cost
        return start if trip_tank >= 0 else -1