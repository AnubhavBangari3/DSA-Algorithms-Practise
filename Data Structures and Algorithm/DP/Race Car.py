'''
1. Use **BFS** because we need the shortest sequence of instructions.
2. Each state is:

   `(position, speed)`

3. Start from:

   `(0, 1)`

4. From every state, try both instructions:

   - `A`:
     - `new_position = position + speed`
     - `new_speed = speed * 2`

   - `R`:
     - Position stays same.
     - If speed is positive → new speed = `-1`
     - Otherwise → new speed = `1`

5. Store visited states so we don't process the same `(position, speed)` again.
6. Use BFS level by level.
7. The first time we reach `target`, return the number of instructions.
Complexity
Time Complexity: roughly O(target × log target)
Space Complexity: roughly O(target × log target)
'''

from collections import deque

class Solution:
    def racecar(self, target: int) -> int:

        # Queue stores:
        # position, speed, instructions used
        queue = deque([(0, 1, 0)])

        # Avoid processing same state again
        visited = {(0, 1)}

        while queue:

            position, speed, steps = queue.popleft()

            # Target reached
            if position == target:
                return steps

            # -----------------
            # Instruction A
            # -----------------

            new_position = position + speed
            new_speed = speed * 2

            # Keep search within useful range
            if (
                -2 * target <= new_position <= 2 * target
                and (new_position, new_speed) not in visited
            ):
                visited.add((new_position, new_speed))

                queue.append(
                    (new_position, new_speed, steps + 1)
                )

            # -----------------
            # Instruction R
            # -----------------

            # Position stays same
            # Speed changes direction
            reverse_speed = -1 if speed > 0 else 1

            if (position, reverse_speed) not in visited:

                visited.add((position, reverse_speed))

                queue.append(
                    (position, reverse_speed, steps + 1)
                )