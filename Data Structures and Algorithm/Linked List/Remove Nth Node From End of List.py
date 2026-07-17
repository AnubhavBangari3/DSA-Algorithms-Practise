class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Delete nth node from end
        slow.next = slow.next.next
        
        return dummy.next
    
'''
Algorithm

1. Create a dummy node and connect it to the head of the linked list.

2. Initialize two pointers:
   - fast at the dummy node.
   - slow at the dummy node.

3. Move the fast pointer n+1 steps ahead.

4. Move both pointers one step at a time until fast reaches the end.

5. At this point:
   - Slow points to the node just before the nth node from the end.

6. Remove the nth node by skipping it:
   - slow.next = slow.next.next

7. Return the node after the dummy node.

Pattern:
Two Pointers (Fast and Slow)

Time Complexity: O(n)

Space Complexity: O(1)
'''