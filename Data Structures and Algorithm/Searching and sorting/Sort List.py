# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Merge two sorted linked lists.
    def merge_ll(self, a, b):
        # If one list is empty, return the other list.
        if a is None:
            return b
        if b is None:
            return a

        # Choose the smaller node as the current node.
        if a.val < b.val:
            result = a
            # Merge the remaining part of list a with list b.
            result.next = self.merge_ll(a.next, b)
        else:
            result = b
            # Merge list a with the remaining part of list b.
            result.next = self.merge_ll(a, b.next)

        return result

    # Find the middle node of the linked list.
    def get_middle(self, head):
        if head is None:
            return head

        # Slow moves one step and fast moves two steps.
        slow = head
        fast = head

        # When fast reaches the end, slow reaches the middle.
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A list with zero or one node is already sorted.
        if head is None or head.next is None:
            return head

        # Find the middle node.
        middle = self.get_middle(head)

        # Store the starting node of the right half.
        next_to_middle = middle.next

        # Break the linked list into two separate halves.
        middle.next = None

        # Recursively sort the left half.
        left = self.sortList(head)

        # Recursively sort the right half.
        right = self.sortList(next_to_middle)

        # Merge both sorted halves.
        sorted_list = self.merge_ll(left, right)

        return sorted_list
    
'''
Algorithm

1. If the linked list is empty or contains only one node, return it because it is already sorted.

2. Find the middle node using slow and fast pointers.
   - Slow moves one node at a time.
   - Fast moves two nodes at a time.
   - When fast reaches the end, slow points to the middle.

3. Divide the linked list into two halves by disconnecting the middle node from the right half.

4. Recursively sort the left half.

5. Recursively sort the right half.

6. Merge the two sorted linked lists:
   - Compare the first nodes of both lists.
   - Select the smaller node.
   - Recursively merge the remaining nodes.

7. Return the head of the merged sorted linked list.

Pattern:
Merge Sort + Slow and Fast Pointers

Time Complexity: O(n log n)
Space Complexity: O(log n) for sort recursion, with additional recursive merge call-stack usage

'''
        
        
        
        
        
        
        