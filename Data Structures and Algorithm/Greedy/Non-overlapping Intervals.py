'''
1. Sort intervals by their **ending time**.
2. Keep the interval that ends earliest.
3. Traverse the remaining intervals.
4. If the next interval starts before the current interval ends:

   `start < end`

   then they overlap, so remove the next interval.

5. Otherwise, keep the interval and update `end`.
6. Return the number of removed intervals.

Complexity
Time: O(n log n)
Space: O(1) extra space, ignoring sorting implementation.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # Sort intervals by ending time
        intervals.sort(key=lambda x: x[1])

        # Number of intervals removed
        remove = 0

        # End of last selected interval
        end = intervals[0][1]

        # Process remaining intervals
        for i in range(1, len(intervals)):

            start = intervals[i][0]

            # Overlapping interval
            if start < end:
                remove += 1

            else:
                # Keep current interval
                end = intervals[i][1]

        return remove