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
1. Create an empty Min Heap.

2. Traverse every number in the array.

3. Push the current number into the heap.

4. If the heap size becomes greater than k,
   remove the smallest element.

5. After processing all numbers,
   the heap contains exactly the k largest elements.

6. The smallest element inside the heap
   is the kth largest element.

Key Idea:
Maintain only the k largest elements instead of sorting the entire array.

Time Complexity:

Each insertion into the heap:
O(log k)

Each deletion:
O(log k)

Performed for n elements.

Overall:

O(n log k)

--------------------------------

Space Complexity:

Heap stores at most k elements.

Overall:

O(k)

'''