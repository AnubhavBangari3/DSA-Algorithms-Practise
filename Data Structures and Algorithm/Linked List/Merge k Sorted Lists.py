import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Heap will store the current smallest available node
        # from every linked list.
        heap = []

        # Put the first node of every non-empty linked list into the heap.
        for i, node in enumerate(lists):
            if node:
                # Store:
                # node.val -> used by heap to find the smallest value
                # i        -> used as a tie-breaker when values are equal
                # node     -> actual linked-list node
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node helps us build the final merged linked list.
        dummy = ListNode(0)

        # Curr always points to the last node of the merged list.
        curr = dummy

        # Continue until there are no nodes left in the heap.
        while heap:

            # Remove the smallest available node.
            value, list_index, node = heapq.heappop(heap)

            # Attach this smallest node to the merged linked list.
            curr.next = node

            # Move curr to the newly attached node.
            curr = curr.next

            # If this node has a next node,
            # add that next node into the heap.
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, list_index, node.next)
                )

        # Dummy was temporary, so return the actual head.
        return dummy.next
    
'''
Algorithm

1. Create a minimum heap.

2. Insert the first node of every non-empty linked list into the heap.

3. Each heap entry stores:
   - Node value.
   - List index.
   - Actual node.

4. Create a dummy node for the merged linked list.

5. While the heap is not empty:

   - Remove the smallest node from the heap.

   - Attach this node to the merged linked list.

   - If the removed node has a next node,
     insert that next node into the heap.

6. Continue until the heap becomes empty.

7. Return dummy.next.

Pattern:
Min Heap + Linked List Merge

Time Complexity: O(N log k)

Space Complexity: O(k)
'''