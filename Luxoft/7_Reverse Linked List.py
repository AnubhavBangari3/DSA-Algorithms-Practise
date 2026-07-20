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
    
