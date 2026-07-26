from collections import deque
class MyStack:
    def __init__(self):
        # The front of the queue always represents
        # the top of the stack.
        self.queue = deque()

    def push(self, x: int) -> None:
        # Create a new queue with the new element first.
        temp = deque([x])
        # Place all previous elements after it.
        temp.extend(self.queue)
        # Update the queue.
        self.queue = temp

    def pop(self) -> int:
        # Remove the front element,
        # which is the stack's top.
        return self.queue.popleft()

    def top(self) -> int:
        # Return the front element
        # without removing it.
        return self.queue[0]

    def empty(self) -> bool:
        # The stack is empty if the queue is empty.
        return len(self.queue) == 0

'''
Algorithm

1. Create one queue.
2. Keep the top of the stack
   at the front of the queue.
3. For push(x):
   a. Create a temporary queue
      containing x.

   b. Append all existing elements
      after x.

   c. Replace the original queue
      with the temporary queue.
4. For pop():
   - Remove and return the front element.
5. For top():
   - Return the front element.
6. For empty():
   - Return whether the queue is empty.

Pattern:
Queue Simulation

'''