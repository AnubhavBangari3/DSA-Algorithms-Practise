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