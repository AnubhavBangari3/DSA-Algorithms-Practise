import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Min Heap stores only the k largest elements.
        self.heap = []
        # Number of largest elements to maintain.
        self.k = k
        # Insert the initial numbers.
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Insert the new value into the heap.
        heapq.heappush(self.heap, val)
        # If more than k elements are present,
        # remove the smallest element.
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # The root of the Min Heap is
        # the kth largest element.
        return self.heap[0]
'''
Algorithm

1. Create an empty Min Heap.
2. Store the value of k.
3. Insert all initial numbers
   into the heap.
4. Whenever a new number arrives:
   a. Insert it into the heap.
   b. If the heap size becomes
      greater than k:
      - Remove the smallest element.
5. The heap always contains
   the k largest elements.
6. Return the top of the heap,
   which is the kth largest element.

Pattern:
Heap (Min Heap)

Time Complexity:

Constructor:
O(n log k)

add():
O(log k)

Space Complexity:
O(k)

'''