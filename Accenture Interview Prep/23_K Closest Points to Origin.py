'''
973. K Closest Points to Origin
Solved
Medium
Topics
premium lock iconCompanies

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

 

Constraints:

    1 <= k <= points.length <= 104
    -104 <= xi, yi <= 104

Algorithm

1. Use Max Heap of size k.

2. For every point [x, y]:
   - Calculate squared distance:
     distance = x*x + y*y

3. Push (-distance, x, y) into heap.
   Negative distance is used to simulate max heap.

4. If heap size becomes greater than k:
   - Pop one element.
   - This removes the farthest point among current points.

5. After processing all points:
   - Heap contains k closest points.

6. Return all points from heap.


Algorithm

1. Use Max Heap of size k.

2. For every point [x, y]:
   - Calculate squared distance:
     distance = x*x + y*y

3. Push (-distance, x, y) into heap.
   Negative distance is used to simulate max heap.

4. If heap size becomes greater than k:
   - Pop one element.
   - This removes the farthest point among current points.

5. After processing all points:
   - Heap contains k closest points.

6. Return all points from heap.

'''
import heapq

class Solution:
    def kClosest(self, points, k):
        # Max heap using negative distance
        heap = []
        for x, y in points:

            # Squared distance from origin
            dist = x * x + y * y

            # Push negative distance to simulate max heap
            heapq.heappush(heap, (-dist, x, y))

            # Keep only k closest points
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract points from heap
        return [[x, y] for dist, x, y in heap]
'''
Time Complexity:
O(n log k)

Reason:
For every point, heap operation takes O(log k).

Space Complexity:
O(k)

Reason:
Heap stores only k points.
'''