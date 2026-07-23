class Solution:
    def carFleet(
        self,
        target: int,
        position: List[int],
        speed: List[int]
    ) -> int:

        # Stack stores the arrival time of each car fleet.
        stack = []

        # Process cars from nearest to the target
        # to farthest from the target.
        for pos, spd in sorted(zip(position, speed), reverse=True):
            # Time required for the current car
            # to reach the target.
            time = (target - pos) / spd
            # First car always forms a new fleet.
            if not stack:
                stack.append(time)
            # If the current car takes longer than the fleet
            # in front, it cannot catch up and forms a new fleet.
            elif time > stack[-1]:
                stack.append(time)
            # Otherwise:
            # time <= stack[-1]
            # The current car catches the fleet ahead,
            # so no new fleet is created.

        # Number of fleets equals the number of
        # arrival times stored in the stack.
        return len(stack)

'''
Algorithm

1. Pair every car's position with its speed.

2. Sort the cars in descending order of position
   (nearest to the target first).

3. Create an empty stack.

4. For each car:
   - Calculate the time required to reach the target.

5. If the stack is empty:
   - Create the first fleet.

6. Otherwise:
   - If the current car takes more time than the fleet ahead:
       - It cannot catch up.
       - Create a new fleet.
   - Otherwise:
       - It catches the fleet ahead.
       - Do not create a new fleet.

7. Return the number of fleets.

Pattern:
Greedy + Monotonic Stack

Time Complexity: O(n log n)

Space Complexity: O(n)

'''