import heapq

class Solution:
    def findKthLargest(self, nums, k):

        # Min Heap stores only the k largest elements seen so far.
        heap = []

        # Process every number in the array.
        for num in nums:

            # Insert the current number into the heap.
            heapq.heappush(heap, num)

            # If more than k elements are present,
            # remove the smallest element.
            if len(heap) > k:
                heapq.heappop(heap)

        # The smallest element in the heap
        # is the kth largest element overall.
        return heap[0]

'''
Algorithm

1. Create an empty Min Heap.

2. Traverse every number in the array.

3. Insert the current number into the heap.

4. If the heap size becomes greater than k:
   - Remove the smallest element.

5. Continue until all numbers are processed.

6. The heap now contains only the k largest elements.

7. The smallest element in the heap
   is the kth largest element.

Pattern:
Heap (Min Heap)

Time Complexity:
O(n log k)

Space Complexity:
O(k)

'''