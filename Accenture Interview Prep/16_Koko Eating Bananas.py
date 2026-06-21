'''
875. Koko Eating Bananas
Solved
Medium
Topics
premium lock iconCompanies

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

 

Constraints:

    1 <= piles.length <= 104
    piles.length <= h <= 109
    1 <= piles[i] <= 109

Algorithm

1. This is Binary Search on Answer.

2. Search space:
   Minimum speed = 1
   Maximum speed = max(piles)

3. For a given speed mid:
   Calculate total hours needed.

   For each pile:
   hours += ceil(pile / mid)

4. If total hours <= h:
   - Koko can finish with this speed.
   - Try smaller speed.
   - right = mid

5. Else:
   - Speed is too slow.
   - Need bigger speed.
   - left = mid + 1

6. When loop ends:
   left is the minimum valid speed.

7. Return left.
'''
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
Time Complexity:
O(n log(max(piles)))

Reason:
Binary search runs over speed range.
For every speed, we scan all piles.

Space Complexity:
O(1)

Reason:
Only variables are used.

'''