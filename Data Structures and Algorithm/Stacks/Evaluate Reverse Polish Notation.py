class Solution:

    # Performs the arithmetic operation.
    def helper(self, a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        # Division truncates toward zero.
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        # Stack stores operands.
        stack = []
        # Traverse every token.
        for token in tokens:
            # If the token is an operator.
            if len(token) == 1 and ord(token) < ord("0"):
                # Pop the last two operands.
                second = stack.pop()
                first = stack.pop()
                # Evaluate the expression.
                result = self.helper(first, second, token)
                # Push the result back onto the stack.
                stack.append(result)
            # Otherwise, the token is a number.
            else:
                stack.append(int(token))
        # The final result remains on the stack.
        return stack.pop()

'''
Algorithm

1. Create an empty stack.

2. Traverse each token.

3. If the token is a number:
   - Convert it to an integer.
   - Push it onto the stack.

4. If the token is an operator:
   - Pop the second operand.
   - Pop the first operand.
   - Perform the operation.
   - Push the result back onto the stack.

5. Continue until all tokens are processed.

6. The last remaining element in the stack is the answer.

Pattern:
Stack

Time Complexity: O(n)

Space Complexity: O(n)
'''