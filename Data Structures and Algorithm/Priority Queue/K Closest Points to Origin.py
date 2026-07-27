import heapq

class Solution:
    def kClosest(self, points, k):
        # Max Heap (using negative distance)
        # Stores only the k closest points.
        heap = []

        # Process every point.
        for x, y in points:
            # Calculate the squared distance
            # from the origin.
            dist = x * x + y * y
            # Push the point into the max heap.
            # Negative distance simulates a max heap.
            heapq.heappush(heap, (-dist, x, y))
            # If more than k points are stored,
            # remove the farthest point.
            if len(heap) > k:
                heapq.heappop(heap)

        # Return the remaining k closest points.
        return [[x, y] for dist, x, y in heap]

'''
Algorithm

1. Create an empty Max Heap.
2. Traverse every point.
3. Calculate its squared distance
   from the origin:

      x² + y²
4. Insert the point into the heap
   using negative distance.
5. If the heap size becomes greater than k:
   - Remove the farthest point.
6. Continue until all points
   are processed.
7. The heap now contains exactly
   the k closest points.
8. Return those points.

Pattern:
Heap (Max Heap)

Time Complexity:
O(n log k)

Space Complexity:
O(k)

'''