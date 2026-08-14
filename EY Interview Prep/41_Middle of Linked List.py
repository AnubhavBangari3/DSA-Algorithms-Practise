'''
876. Middle of the Linked List
Solved
Easy
Topics
premium lock iconCompanies

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

 

Constraints:

    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100


'''

'''
1. Use two pointers:
   - `slow` → moves **one step** at a time.
   - `fast` → moves **two steps** at a time.
2. Start both pointers at `head`.
3. Continue while `fast` and `fast.next` exist.
4. Move:
   - `slow = slow.next`
   - `fast = fast.next.next`
5. When `fast` reaches the end, `slow` will be at the middle.
6. Return `slow`.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):

        # Slow and fast pointers
        slow = head
        fast = head

        # Continue while fast can move two steps
        while fast and fast.next:

            # Slow moves one step
            slow = slow.next

            # Fast moves two steps
            fast = fast.next.next

        # Slow is now at the middle
        return slow

'''
Complexity
Time Complexity: O(n)
We traverse the linked list once.
Space Complexity: O(1)
Only two pointers are used.
'''