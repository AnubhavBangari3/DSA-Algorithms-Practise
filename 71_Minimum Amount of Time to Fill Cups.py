'''

2335. Minimum Amount of Time to Fill Cups
Solved
Easy
Topics
premium lock iconCompanies
Hint

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

 

Example 1:

Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.

Example 2:

Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.

Example 3:

Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.

 

Constraints:

    amount.length == 3
    0 <= amount[i] <= 100


    
Algorithm

1. Let:
   total = sum of all cups
   max_cups = maximum cups among the 3 types

2. In one second:
   - We can fill at most 2 cups
   - But only if they are different types

3. Minimum time depends on two cases:

   Case 1:
   If one type has too many cups,
   it becomes the bottleneck.

   Example:
   [5,0,0]
   We must spend 5 seconds.

   Case 2:
   Otherwise,
   we can efficiently pair different types.

   Example:
   total = 10
   We can fill 2 cups/sec
   so minimum = ceil(10 / 2)

4. Final answer:
   max(max_cups, ceil(total / 2))


Complexity

Time Complexity:
O(1)

Reason:
Only 3 elements.

Space Complexity:
O(1)
'''

class Solution:
    def fillCups(self, amount):
        # Total cups to fill
        total = sum(amount)

        # Maximum cups of one type
        max_cups = max(amount)

        # Minimum seconds required
        # Either:
        # 1. Dominated by largest type
        # 2. Or by total cups / 2
        return max(max_cups, (total + 1) // 2)