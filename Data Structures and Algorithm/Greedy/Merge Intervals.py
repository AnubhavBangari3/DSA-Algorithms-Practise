'''
1. Sort intervals by their starting value.
2. Add the first interval to `result`.
3. Compare every interval with the last interval in `result`.
4. If they overlap, merge them.
5. Otherwise, add the current interval to `result`.


Complexity
Time: O(n log n)
Space: O(n)
'''

class Solution:
    def merge(self, intervals):

        # Sort by starting value
        intervals.sort(key=lambda x: x[0])

        # Add first interval
        result = [intervals[0]]

        for current in intervals[1:]:

            # Last merged interval
            last = result[-1]

            # Overlapping intervals
            if current[0] <= last[1]:

                # Merge by extending the ending value
                last[1] = max(last[1], current[1])

            else:
                # No overlap
                result.append(current)

        return result