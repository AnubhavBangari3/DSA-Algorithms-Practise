'''
Algorithm: Linked List Cycle (Floyd's Cycle Detection / Slow and Fast Pointers)

1. Initialize two pointers: slow = head and fast = head.
2. Traverse the linked list while fast and fast.next exist.
3. Move slow one step forward: slow = slow.next.
4. Move fast two steps forward: fast = fast.next.next.
5. Check if slow == fast:
   - If both pointers meet, return True (cycle exists).
6. Repeat until the pointers meet or fast reaches the end.
7. If fast reaches the end, return False (no cycle exists).

Time Complexity: O(n)
Space Complexity: O(1)

'''

class Solution:
    def hasCycle(self, head):
        # Slow and fast pointers
        slow = head
        fast = head
        # Traverse while fast pointer can move
        while fast and fast.next:
            # Move slow by one step
            slow = slow.next
            # Move fast by two steps
            fast = fast.next.next
            # If both pointers meet,
            # cycle exists
            if slow == fast:
                return True
        # Fast reached end of list
        # No cycle
        return False