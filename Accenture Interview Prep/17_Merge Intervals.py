'''
56. Merge Intervals
Solved
Medium
Topics
premium lock iconCompanies

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

 

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

Algorithm

1. Sort intervals based on start time.

2. Create result list.

3. Add first interval to result.

4. Traverse remaining intervals:

   Let:
   last = last interval in result
   current = current interval

5. If current.start <= last.end:
      Overlap exists

      Merge:
      last.end = max(last.end, current.end)

6. Else:
      No overlap

      Append current interval to result

7. Return result.
'''
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
Time Complexity:
O(n log n)

Reason:
Sorting dominates the complexity.

Space Complexity:
O(n)

Reason:
Result list stores merged intervals.

'''