class MyQueue:

    def __init__(self):
        # Stores newly pushed elements.
        self.in_stack = []
        # Stores elements in queue-removal order.
        self.out_stack = []

    def push(self, x: int) -> None:
        # Add the new element to the input stack.
        self.in_stack.append(x)

    def pop(self) -> int:
        # Transfer elements only when out_stack is empty.
        if not self.out_stack:
            # Moving all elements reverses their order.
            # The oldest element reaches the top of out_stack.
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Remove and return the oldest element.
        return self.out_stack.pop()

    def peek(self) -> int:
        # Transfer elements only when out_stack is empty.
        if not self.out_stack:
            # Reverse the order so the oldest element
            # reaches the top of out_stack.
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # Return the oldest element without removing it.
        return self.out_stack[-1]

    def empty(self) -> bool:
        # The queue is empty only when both stacks are empty.
        return not self.in_stack and not self.out_stack

'''
1. Create two stacks:
   in_stack:
   - Stores newly pushed elements.

   out_stack:
   - Stores elements in queue-removal order.

2. For push(x):
   - Push x into in_stack.

3. For pop():
   a. If out_stack is empty:
      - Move all elements from in_stack to out_stack.

   b. Moving the elements reverses their order.

   c. The oldest element now reaches the top
      of out_stack.

   d. Pop and return the top of out_stack.

4. For peek():
   a. If out_stack is empty:
      - Move all elements from in_stack to out_stack.

   b. Return the top element of out_stack
      without removing it.

5. For empty():
   - Return true only when both stacks are empty.

Pattern:
Two Stacks

'''