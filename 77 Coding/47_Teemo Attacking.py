'''
495. Teemo Attacking
Solved
Easy
Topics
premium lock iconCompanies

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

 

Constraints:

    1 <= timeSeries.length <= 104
    0 <= timeSeries[i], duration <= 107
    timeSeries is sorted in non-decreasing order.


1. If there is only one attack:
   return duration

2. Initialize total_poison = 0

3. Traverse the array from 0 to n - 2:
   
   For each attack at timeSeries[i]:
   - Find the gap between current attack and next attack:
       gap = timeSeries[i + 1] - timeSeries[i]

   - Add minimum of:
       gap and duration

   Reason:
   - If next attack happens after poison ends,
     current attack contributes full duration
   - If next attack happens before poison ends,
     only gap contributes because poison overlaps

4. After loop, add duration for the last attack

5. Return total_poison

Time complexity
Time Complexity:
O(n)

Reason:
We traverse the array once

Space Complexity:
O(1)

Reason:
We use only a few variables
'''

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        # Total poisoned time
        total_poison = 0
        
        # Traverse all attacks except the last one
        for i in range(len(timeSeries) - 1):
            # Time gap between current and next attack
            gap = timeSeries[i + 1] - timeSeries[i]
            
            # Add only non-overlapping contribution
            total_poison += min(gap, duration)
        
        # Last attack always contributes full duration
        total_poison += duration
        
        return total_poison