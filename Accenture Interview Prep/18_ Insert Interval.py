'''
57. Insert Interval
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

 

Constraints:

    0 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 105
    intervals is sorted by starti in ascending order.
    newInterval.length == 2
    0 <= start <= end <= 105

Algorithm

1. Create an empty result list.

2. Add all intervals that end before newInterval starts.
   Condition:
   interval.end < newInterval.start

3. Merge all intervals that overlap with newInterval.
   Condition:
   interval.start <= newInterval.end

   Update:
   newInterval.start = min(newInterval.start, interval.start)
   newInterval.end = max(newInterval.end, interval.end)

4. Add the merged newInterval to result.

5. Add all remaining intervals.

6. Return result.
'''
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)
        # Step 1: Add intervals that come before newInterval
        # No overlap because their end is smaller than newInterval start
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        # Step 2: Merge all overlapping intervals
        # Overlap exists when interval start <= newInterval end
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # Step 3: Add merged newInterval
        result.append(newInterval)
        # Step 4: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
'''
Time Complexity:
O(n)

Reason:
We traverse intervals once.

Space Complexity:
O(n)

Reason:
We create a result list.

'''