class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Dummy node simplifies result-list creation.
        dummy = ListNode(0)
        current = dummy

        # Stores carry from the previous addition.
        carry = 0

        # Continue while either list has digits or carry remains.
        while l1 or l2 or carry:

            # Use 0 when one linked list has ended.
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            # Add both digits and the previous carry.
            total = value1 + value2 + carry

            # Carry is the tens digit.
            carry = total // 10

            # Current result digit is the ones digit.
            digit = total % 10

            # Add the result digit to the linked list.
            current.next = ListNode(digit)
            current = current.next

            # Move the input pointers forward.
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
    
'''
Algorithm

1. Create a dummy node for the result linked list.

2. Initialize:
   - current at the dummy node.
   - carry as 0.

3. Traverse while either linked list has nodes or a carry remains.

4. Get the current digit from both linked lists.
   - If a list has ended, use 0.

5. Calculate:
   total = digit1 + digit2 + carry

6. Find:
   - Result digit = total % 10
   - New carry = total // 10

7. Create a new node using the result digit.

8. Move the result pointer and both input pointers forward.

9. After processing all digits, return dummy.next.

Pattern:
Linked List Simulation + Carry

Time Complexity: O(max(m, n))

Space Complexity: O(max(m, n)) for the output list
Auxiliary Space Complexity: O(1)

'''