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

Algorithm

1. Maintain two stacks:
   stack     -> stores actual values
   minStack  -> stores minimum value till that point
2. Push Operation:
   Push value into stack.
   If minStack is empty:
      push value

   Else:
      push min(value, minStack.top())

3. Pop Operation:
   Pop from both stack and minStack.

4. Top Operation:
   Return stack.top()

5. getMin Operation:
   Return minStack.top()

Since minStack always stores the minimum till that index,
all operations become O(1).
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
Push:
O(1)

Pop:
O(1)

Top:
O(1)

getMin:
O(1)

Space Complexity:
O(n)

Reason:
Two stacks store n elements.

'''