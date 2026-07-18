class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # If the list has 0 or 1 node, it is already reordered.
        if not head or not head.next:
            return

        # -------------------- STEP 1 : FIND THE MIDDLE --------------------

        # Initialize slow and fast pointers.
        slow, fast = head, head

        # Move slow by one step and fast by two steps.
        # When fast reaches the end, slow will be at the middle.
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # -------------------- STEP 2 : REVERSE THE SECOND HALF --------------------

        # Start of the second half.
        second = slow.next

        # Break the linked list into two separate halves.
        slow.next = None

        # Previous node used while reversing.
        prev = None

        # Reverse the second half of the linked list.
        while second:

            # Store the next node before changing the link.
            temp = second.next

            # Reverse the current node's pointer.
            second.next = prev

            # Move prev to the current node.
            prev = second

            # Move to the next node.
            second = temp

        # Prev is now the head of the reversed second half.

        # -------------------- STEP 3 : MERGE BOTH HALVES --------------------

        # First points to the first half.
        first = head

        # Second points to the reversed second half.
        second = prev

        # Merge one node from each half alternately.
        while second:

            # Save the next nodes before changing links.
            temp1 = first.next
            temp2 = second.next

            # Connect the current node from the first half.
            first.next = second

            # Connect the current node from the second half.
            second.next = temp1

            # Move both pointers forward.
            first = temp1
            second = temp2

'''
Algorithm

1. If the linked list has 0 or 1 node, return because it is already reordered.
2. Find the middle of the linked list using slow and fast pointers.
3. Split the linked list into two halves.
4. Reverse the second half of the linked list.
5. Initialize:
   - first pointer at the beginning of the first half.
   - second pointer at the beginning of the reversed second half.
6. Merge both halves alternately:
   - Connect one node from the first half.
   - Connect one node from the second half.
   - Repeat until the second half becomes empty.
7. The linked list is now reordered in-place.

Pattern:
Slow & Fast Pointers + Linked List Reversal + Alternate Merge

Time Complexity: O(n)

Space Complexity: O(1)

'''