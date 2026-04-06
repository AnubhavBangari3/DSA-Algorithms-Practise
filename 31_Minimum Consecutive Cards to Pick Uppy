'''
Description


You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.

Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

 

Constraints:

    1 <= cards.length <= 105
    0 <= cards[i] <= 106
Algorithm
1. Create a hashmap last_seen
   It will store:
   card value -> last index where it appeared

2. Initialize ans = infinity

3. Traverse the array:
   For each index i and value cards[i]:

   - If cards[i] is already in last_seen:
       length = i - last_seen[cards[i]] + 1
       ans = min(ans, length)

   - Update last_seen[cards[i]] = i

4. If ans is still infinity, return -1
   Otherwise return ans

   Time Complexity
O(n)

Because we scan the array once.

Space Complexity
O(n)
'''

class Solution:
    def minimumCardPickup(self, cards):
        last_seen = {}
        ans = float('inf')

        for i, card in enumerate(cards):
            if card in last_seen:
                ans = min(ans, i - last_seen[card] + 1)

            last_seen[card] = i

        return ans if ans != float('inf') else -1