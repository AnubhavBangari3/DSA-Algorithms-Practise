class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Store deadends for O(1) lookup.
        deadEndSet = set(deadends)
        # Queue stores (current lock state, number of moves).
        queue = deque([("0000", 0)])
        # Stores all visited lock states.
        visited = {"0000"}

        # Perform BFS.
        while queue:
            # Visit the next lock state.
            curStr, curSteps = queue.popleft()
            # Target found.
            if curStr == target:
                return curSteps
            # Ignore deadend states.
            if curStr in deadEndSet:
                continue
            # Try rotating each of the four wheels.
            for i in range(4):
                digit = int(curStr[i])
                # Rotate the wheel forward and backward.
                for direction in [1, -1]:
                    # Circular rotation (9→0 and 0→9).
                    newDigit = (digit + direction) % 10
                    # Create the new lock state.
                    newStr = curStr[:i] + str(newDigit) + curStr[i + 1:]
                 # Visit the new state only once.
                    if newStr not in visited:
                        visited.add(newStr)
                        queue.append((newStr, curSteps + 1))

        # Target cannot be reached.
        return -1

'''
Algorithm

1. Store all deadends in a set.
2. Create a queue and insert:
   ("0000", 0)
3. Create a visited set and add "0000".
4. While the queue is not empty:
   a. Remove the front lock state.
   b. If it is the target:
      Return the number of moves.
   c. If it is a deadend:
      Skip it.
   d. For each of the 4 wheels:
      - Rotate one step forward.
      - Rotate one step backward.
      This creates 2 new states.
   e. If a new state has not been visited:
      - Mark it visited.
      - Add it to the queue with
        moves + 1.
5. If the queue becomes empty,
   return -1.

Pattern:
Breadth First Search (BFS)

Time Complexity:
O(10⁴)

Space Complexity:
O(10⁴)

'''