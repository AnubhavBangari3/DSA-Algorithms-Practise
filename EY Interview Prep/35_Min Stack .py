'''
155. Min Stack
Solved
Medium
Topics
premium lock iconCompanies
Hint

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int value) pushes the element value onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 

Constraints:

    -231 <= val <= 231 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 104 calls will be made to push, pop, top, and getMin.



'''

'''
1. Use **two stacks**:
   - `stack` → stores the actual values.
   - `minStack` → stores the minimum value at every position.
2. When `push(val)` is called:
   - Push `val` into the main stack.
   - Push `min(val, current_min)` into `minStack`.
3. When `pop()` is called:
   - Pop from both stacks.
4. `top()`:
   - Return the top of the main stack.
5. `getMin()`:
   - Return the top of `minStack`.
6. Since the current minimum is always at the top of `minStack`, `getMin()` takes `O(1)` time.


'''


class MinStack:
    def __init__(self):
        # Main stack stores actual values
        self.stack = []
        # Min stack stores minimum till current position
        self.minStack = []
    def push(self, val):
        # Push value into main stack
        self.stack.append(val)
        # If minStack is empty,
        # current value becomes minimum
        if not self.minStack:
            self.minStack.append(val)
        else:
            # Store minimum till this point
            self.minStack.append(
                min(val, self.minStack[-1])
            )
    def pop(self):
        # Remove top element from both stacks
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        # Return top element
        return self.stack[-1]
    def getMin(self):
        # Return current minimum
        return self.minStack[-1]

'''
Complexity
push(): O(1)
pop(): O(1)
top(): O(1)
getMin(): O(1)
Space Complexity: O(n)
Two stacks are maintained.
'''