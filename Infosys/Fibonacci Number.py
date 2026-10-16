'''
Algorithm: Fibonacci Number (Iterative Dynamic Programming)

1. Check the base case:
   - If n <= 1, return n.
2. Initialize prev2 = 0 and prev1 = 1.
3. Iterate from i = 2 to n.
4. Calculate current = prev1 + prev2.
5. Update the previous two values:
   - Set prev2 = prev1.
   - Set prev1 = current.
6. Repeat until the nth Fibonacci number is calculated.
7. Return prev1 as the nth Fibonacci number.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def fib(self, n):

        # Base cases
        if n <= 1:
            return n

        prev2 = 0
        prev1 = 1

        for i in range(2, n + 1):

            current = prev1 + prev2

            prev2 = prev1
            prev1 = current

        return prev1