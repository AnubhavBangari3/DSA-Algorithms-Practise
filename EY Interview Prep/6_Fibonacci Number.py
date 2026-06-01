"""
509. Fibonacci Number

Problem:

Fibonacci sequence:

F(0) = 0
F(1) = 1

F(n) = F(n-1) + F(n-2)

Given n, return F(n).

Examples:

Input: n = 2
Output: 1

Input: n = 3
Output: 2

Input: n = 4
Output: 3

Constraints:
- 0 <= n <= 30
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: Dynamic Programming (Bottom-Up)
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Handle base cases:
      if n <= 1:
          return n

2. Initialize:

      prev2 = 0
      prev1 = 1

3. Iterate from 2 to n:

      current = prev1 + prev2

      Shift values:

      prev2 = prev1
      prev1 = current

4. Return prev1
"""

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


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Single loop from 2 to n

Space Complexity: O(1)

Explanation:
- Only few variables used
- No extra array or recursion stack
"""