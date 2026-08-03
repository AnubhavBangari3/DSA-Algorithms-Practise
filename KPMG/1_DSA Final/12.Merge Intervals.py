class Solution:
    def merge(self, intervals):
        # Sort intervals by starting time
        intervals.sort(key=lambda x: x[0])
        # Store merged intervals
        result = []
        # Add first interval
        result.append(intervals[0])
        # Process remaining intervals
        for current in intervals[1:]:
            # Last merged interval
            last = result[-1]
            # If intervals overlap
            if current[0] <= last[1]:
                # Extend the end if needed
                last[1] = max(last[1], current[1])
            else:
                # No overlap, add as new interval
                result.append(current)

        return result

'''
1. Sort all intervals by their starting time.

2. Add the first interval to the result list.

3. Traverse the remaining intervals.

4. For each interval:
   - Compare it with the last interval in the result.
   - If they overlap:
       Merge them by updating the ending time.
   - Otherwise:
       Add the current interval to the result.

5. Return the merged intervals.

Key Idea:
- After sorting, overlapping intervals become adjacent.
- Only compare the current interval with the last merged interval.


Time Complexity: O(n log n)

- Sorting takes O(n log n).
- Traversing intervals takes O(n).

Overall:
O(n log n)

Space Complexity: O(n)

- Result list stores merged intervals.
- Sorting may also use additional space depending on implementation.
'''