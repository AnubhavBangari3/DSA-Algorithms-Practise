class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy node helps simplify edge cases
        dummy = ListNode()
        # Current pointer for merged list
        current = dummy
        # Compare nodes from both lists
        while list1 and list2:
            # Choose smaller node
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move current pointer
            current = current.next
        # Attach remaining nodes
        if list1:
            current.next = list1
        else:
            current.next = list2
        # Return merged list
        return dummy.next
    
'''
Algorithm

1. Create a dummy node to act as the start of the merged list.
2. Initialize a current pointer to the dummy node.
3. Traverse both linked lists while neither is empty.
4. Compare the current nodes of both lists:
   - Attach the smaller node to the merged list.
   - Move the corresponding list pointer forward.
5. Move the current pointer to the newly added node.
6. After one list becomes empty, attach the remaining nodes of the other list.
7. Return the node after the dummy node as the head of the merged list.

Pattern:
Linked List Pointer Manipulation

Time Complexity: O(m + n)

Space Complexity: O(1)
'''