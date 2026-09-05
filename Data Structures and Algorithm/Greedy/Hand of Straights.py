'''
1. Count the frequency of every card using `Counter`.
2. Process cards in sorted order.
3. If a card still exists, it must be the start of a consecutive group.
4. Take one card from:

   `i, i+1, i+2 ... i+groupSize-1`

5. If any required card has frequency below `0`, return `False`.
6. If all cards can be grouped, return `True`.

Complexity
Time: O(n log n + n × groupSize) in this implementation
Space: O(n)
'''

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # Count frequency of each card
        count = Counter(hand)

        # Process cards from smallest to largest
        for card in sorted(count):

            # Create groups starting with this card
            while count[card] > 0:

                # Need groupSize consecutive cards
                for next_card in range(card, card + groupSize):

                    # Use one card
                    count[next_card] -= 1

                    # Required card was not available
                    if count[next_card] < 0:
                        return False

        return True