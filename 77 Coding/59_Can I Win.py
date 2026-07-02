'''

Topics
premium lock iconCompanies

In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

 

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true

 

Constraints:

    1 <= maxChoosableInteger <= 20
    0 <= desiredTotal <= 300


Algorithm

1. If desiredTotal <= 0:
   return True

2. Find total sum of numbers from 1 to maxChoosableInteger.

3. If total sum < desiredTotal:
   return False
   because even using all numbers cannot reach desiredTotal.

4. Use DFS + memoization.

5. Represent used numbers using bitmask:
   - bit 0 represents number 1
   - bit 1 represents number 2
   - bit i represents number i + 1

6. In each DFS state:
   - Try every unused number.
   - If choosing that number reaches desiredTotal:
       return True
   - Otherwise, check if opponent loses after this move.
       If opponent loses:
           return True

7. If no move can force opponent to lose:
   return False.

Compleity

Time Complexity:
O(n * 2^n)

Where:
n = maxChoosableInteger

Reason:
There are 2^n possible used-number states,
and for each state we may try up to n numbers.

Space Complexity:
O(2^n)

Reason:
Memoization stores result for each bitmask state.

'''

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        n = maxChoosableInteger

        # If target is already reached, first player wins
        if desiredTotal <= 0:
            return True

        # If total sum of all numbers is still less than target,
        # nobody can reach desiredTotal, so first player cannot win
        total_sum = n * (n + 1) // 2
        if total_sum < desiredTotal:
            return False

        memo = {}

        def dfs(used_mask, remaining):
            # If this state is already solved, return cached answer
            if used_mask in memo:
                return memo[used_mask]

            # Try choosing every unused number
            for i in range(n):
                num = i + 1

                # Check if num is unused
                if not (used_mask & (1 << i)):

                    # If current player reaches target now, current player wins
                    if num >= remaining:
                        memo[used_mask] = True
                        return True

                    # Mark this number as used
                    next_mask = used_mask | (1 << i)

                    # If opponent cannot win after this move,
                    # current player can force a win
                    if not dfs(next_mask, remaining - num):
                        memo[used_mask] = True
                        return True

            # No winning move found
            memo[used_mask] = False
            return False

        return dfs(0, desiredTotal)