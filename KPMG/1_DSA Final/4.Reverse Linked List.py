class Solution:
    def reverseList(self, head):
        # Previous node
        prev = None
        # Current node
        curr = head
        # Traverse the linked list
        while curr:
            # Store next node before breaking the link
            nxt = curr.next
            # Reverse the current node's pointer
            curr.next = prev
            # Move prev to current node
            prev = curr
            # Move to next node
            curr = nxt

        # Prev becomes new head
        return prev

'''
1. Initialize two pointers:
   - prev = None
   - curr = head

2. Traverse the linked list until curr becomes None.

3. For each node:
   - Store the next node.
   - Reverse the current node's next pointer to prev.
   - Move prev to the current node.
   - Move curr to the saved next node.

4. When traversal finishes, prev points to the new head.

5. Return prev.

Time Complexity: O(n)
- Visit each node exactly once.

Space Complexity: O(1)
- Only three pointers (prev, curr, nxt) are used.
'''