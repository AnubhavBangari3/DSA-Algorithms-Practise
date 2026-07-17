class Solution:
    def minEatingSpeed(self, piles, h):
        # Minimum possible speed
        left = 1
        # Maximum needed speed
        right = max(piles)
        # Binary Search on speed
        while left < right:
            mid = (left + right) // 2
            # Calculate hours needed with speed = mid
            hours = 0
            for pile in piles:
                # ceil(pile / mid)
                hours += (pile + mid - 1) // mid
            # If Koko can finish within h hours,
            # try to find a smaller valid speed
            if hours <= h:
                right = mid
            # If Koko cannot finish,
            # speed is too slow, increase it
            else:
                left = mid + 1
        # Minimum valid speed
        return left
    
'''
Algorithm
1. Set the minimum possible eating speed to 1.
2. Set the maximum possible eating speed to the largest pile.
3. Perform binary search on the possible eating speed.
4. For each middle speed:
   - Calculate the total hours needed to finish all piles.
   - For each pile, required hours are:
     ceil(pile / speed)
5. If the total hours are less than or equal to h:
   - The speed is valid.
   - Try a smaller speed by moving right to mid.
6. Otherwise:
   - The speed is too slow.
   - Move left to mid + 1.
7. Continue until left equals right.
8. Return left as the minimum valid eating speed.
Pattern:
Binary Search on Answer
Time Complexity: O(n log(max(piles)))
Space Complexity: O(1)
'''