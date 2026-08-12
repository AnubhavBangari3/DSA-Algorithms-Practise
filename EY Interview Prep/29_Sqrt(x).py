'''
69. Sqrt(x)
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

Constraints:

    0 <= x <= 231 - 1
   

'''
'''
1. Use **Binary Search** between `0` and `x`.
2. Find the middle value `mid`.
3. Check whether:

   `mid² <= x < (mid + 1)²`

4. If true, `mid` is the square root rounded down.
5. If `mid² > x`:
   - Search the left half.
6. Otherwise:
   - Search the right half.
7. Return `mid` when the condition is satisfied.
'''

class Solution:
    def mySqrt(self, x: int) -> int:

        # Binary search range
        left = 0
        right = x

        while left <= right:

            # Find middle value
            mid = (left + right) // 2

            # Check if mid is the rounded-down square root
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid

            # mid is too large → search left
            elif mid * mid > x:
                right = mid - 1

            # mid is too small → search right
            else:
                left = mid + 1

'''
Complexity
Time Complexity: O(log x)
Search space is reduced by half after every iteration.
Space Complexity: O(1)
Only left, right, and mid are used.
'''