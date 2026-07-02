'''
143. Reorder List
Solved
Medium
Topics
premium lock iconCompanies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

 

Constraints:

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000


    Algorithm:

1. Find the middle of the linked list
   - Use slow and fast pointers
   - slow moves one step
   - fast moves two steps
   - When fast reaches the end, slow will be at the middle

2. Reverse the second half of the list
   - Start from the node after the middle
   - Reverse the links one by one

3. Merge the two halves alternately
   - First half starts from head
   - Second half starts from the reversed list
   - Pick one node from first half, then one from second half

4. Return the reordered list

Complexity:

Time Complexity: O(n)
- Finding middle takes O(n)
- Reversing second half takes O(n)
- Merging both halves takes O(n)
- Overall → O(n)

Space Complexity: O(1)
- Reordering is done in-place

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2