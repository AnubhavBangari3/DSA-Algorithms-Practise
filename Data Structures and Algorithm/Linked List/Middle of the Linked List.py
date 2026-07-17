# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
        
'''
Algorithm

1. Initialize two pointers:
   - slow at the head.
   - fast at the head.

2. Traverse the linked list while fast and fast.next exist.

3. In each iteration:
   - Move slow one node forward.
   - Move fast two nodes forward.

4. When fast reaches the end of the list:
   - Slow will be at the middle node.

5. Return slow.

Pattern:
Slow and Fast Pointers

Time Complexity: O(n)

Space Complexity: O(1)

'''