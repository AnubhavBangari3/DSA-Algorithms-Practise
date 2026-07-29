from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        # Max Heap for the smaller half.
        # Python has only a Min Heap, so values are stored as negative.
        self.lo = []

        # Min Heap for the larger half.
        self.hi = []

    def addNum(self, num: int) -> None:
        # First, add the number to the smaller half.
        heappush(self.lo, -num)

        # Move the largest value from lo to hi.
        # This keeps every value in lo <= every value in hi.
        heappush(self.hi, -self.lo[0])
        heappop(self.lo)

        # lo is allowed to have at most one extra element.
        # If hi becomes larger, move its smallest value back to lo.
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def findMedian(self) -> float:
        # Odd number of elements:
        # lo contains the extra middle element.
        if len(self.lo) > len(self.hi):
            return -self.lo[0]

        # Even number of elements:
        # Average the largest value of lo and smallest value of hi.
        return (-self.lo[0] + self.hi[0]) / 2

'''
Algorithm

1. Maintain two heaps:
   lo:
   - Max Heap
   - Stores the smaller half of the numbers.

   hi:
   - Min Heap
   - Stores the larger half of the numbers.

2. When adding a number:

   a. Insert it into lo.
   b. Move the largest value from lo to hi.
   c. If hi becomes larger than lo:
      - Move the smallest value from hi back to lo.

3. Maintain these rules:

   - Every value in lo <= every value in hi.
   - lo and hi have equal sizes,
     or lo has exactly one extra element.

4. To find the median:

   - If lo has one extra element:
     return the top of lo.

   - Otherwise:
     return the average of
     the top of lo and the top of hi.

Pattern:
Two Heaps

Time Complexity:

addNum():
O(log n)

findMedian():
O(1)

Space Complexity:
O(n)
'''