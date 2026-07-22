# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check whether there are at least k nodes
        # available for reversal.
        current = head

        for _ in range(k):
            if not current:
                return head
            current = current.next

        # Reverse the current group of k nodes.
        previous = None
        current = head

        for _ in range(k):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # 'head' is now the last node of the reversed group.
        # Connect it with the recursively reversed remaining list.
        head.next = self.reverseKGroup(current, k)

        # 'previous' becomes the new head
        # of the reversed group.
        return previous


'''
Algorithm

1. Check whether at least k nodes are available.
   - If not, return the current head without reversing.

2. Reverse the next k nodes using the standard
   linked list reversal technique.

3. After reversing:
   - The original head becomes the last node
     of the reversed group.

4. Recursively reverse the remaining list.

5. Connect the last node of the current group
   to the head of the next reversed group.

6. Return the new head of the current reversed group.

Pattern:
Linked List + Recursion + Reverse

Time Complexity: O(n)

Space Complexity: O(n / k) (recursive call stack)

'''