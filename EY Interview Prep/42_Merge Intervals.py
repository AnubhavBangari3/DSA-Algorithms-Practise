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



'''
'''
1. Sort all intervals by their **starting time**.
2. Add the first interval to `result`.
3. Traverse the remaining intervals.
4. Compare the current interval with the last interval in `result`.
5. If they overlap:

   `current_start <= last_end`

   merge them by updating the end:

   `last_end = max(last_end, current_end)`

6. If they do not overlap, add the current interval to `result`.
7. Return `result`.
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
Complexity
Time Complexity: O(n log n)
Sorting takes O(n log n).
Traversing intervals takes O(n).
Space Complexity: O(n)
The result array can contain up to n intervals.

'''