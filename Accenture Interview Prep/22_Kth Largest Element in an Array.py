'''
215. Kth Largest Element in an Array
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

Algorithm

1. Create an empty Min Heap.

2. Traverse every number in nums.

3. Push current number into heap.

4. If heap size becomes greater than k:
      remove the smallest element.

5. After processing all elements,
   heap contains k largest elements.

6. The root of Min Heap is the kth largest element.

7. Return heap[0].


'''
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Min Heap
        heap = []
        # Process every number
        for num in nums:
            # Insert into heap
            heapq.heappush(heap, num)
            # Keep only k largest elements
            if len(heap) > k:
                heapq.heappop(heap)

        # Root of heap is kth largest element
        return heap[0]
'''
Time Complexity:
O(n log k)

Reason:
Each insertion/removal takes O(log k).

Space Complexity:
O(k)

Reason:
Heap stores only k elements.

'''