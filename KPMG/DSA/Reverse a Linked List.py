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
Algorithm

1. Initialize two pointers:
   - prev as None.
   - curr as the head of the linked list.

2. Traverse the linked list until curr becomes None.

3. For each node:
   - Store the next node.
   - Reverse the current node's next pointer to point to prev.
   - Move prev to the current node.
   - Move curr to the stored next node.

4. After the traversal is complete, prev points to the new head.

5. Return prev.

Pattern:
Linked List Pointer Manipulation

Time Complexity: O(n)

Space Complexity: O(1)

'''