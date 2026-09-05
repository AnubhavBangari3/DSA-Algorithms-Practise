'''
1. Add all intervals that come completely **before** `newInterval`.
2. Merge all intervals that **overlap** with `newInterval`.
3. Add the merged `newInterval` to the result.
4. Add all remaining intervals that come completely **after** it.
5. Return the result.


Complexity
Time: O(n)
Space: O(n) for the result array.
'''

class Solution:
    def insert(self, intervals, newInterval):

        result = []
        i = 0
        n = len(intervals)

        # Step 1:
        # Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2:
        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:

            # Update start
            newInterval[0] = min(
                newInterval[0],
                intervals[i][0]
            )

            # Update end
            newInterval[1] = max(
                newInterval[1],
                intervals[i][1]
            )

            i += 1

        # Step 3:
        # Add merged newInterval
        result.append(newInterval)

        # Step 4:
        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result