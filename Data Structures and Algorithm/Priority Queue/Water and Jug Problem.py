from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        # The two jugs cannot hold more than x + y liters.
        if target > x + y:
            return False

        # Bézout's identity:
        # target is measurable only when it is divisible
        # by the GCD of the two jug capacities.
        return target % gcd(x, y) == 0

'''
Algorithm

1. Check whether target is greater than
   the total capacity of both jugs.

2. If target > x + y:
   - Return False.

3. Find the GCD of x and y.

4. If target is divisible by gcd(x, y):
   - Return True.

5. Otherwise:
   - Return False.

Pattern:
Math + GCD + Bézout's Identity

Time Complexity:
O(log(min(x, y)))

Space Complexity:
O(1)

'''