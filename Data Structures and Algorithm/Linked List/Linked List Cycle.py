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
    
'''
Algorithm

1. Initialize two pointers:
   - slow at the head.
   - fast at the head.
2. Traverse the linked list while fast and fast.next exist.
3. In each iteration:
   - Move slow one step forward.
   - Move fast two steps forward.
4. If slow and fast point to the same node:
   - A cycle exists.
   - Return True.
5. If fast reaches the end of the list:
   - No cycle exists.
   - Return False.

Pattern:
Slow and Fast Pointers (Floyd's Cycle Detection)

Time Complexity: O(n)

Space Complexity: O(1)
'''