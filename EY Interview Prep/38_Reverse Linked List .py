'''
206. Reverse Linked List
Solved
Easy
Topics
premium lock iconCompanies

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


'''
'''
1. Use three pointers:
   - `prev` → previous node.
   - `curr` → current node.
   - `nxt` → temporarily stores the next node.
2. Initialize:
   - `prev = None`
   - `curr = head`
3. For every node:
   - Save `curr.next` in `nxt`.
   - Reverse the link using `curr.next = prev`.
   - Move `prev` to `curr`.
   - Move `curr` to `nxt`.
4. Continue until `curr` becomes `None`.
5. `prev` will now point to the new head.
6. Return `prev`.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # Previous node
        prev = None
        # Current node
        curr = head
        # Traverse the linked list
        while curr:
            # Store next node before breaking the link
            nxt = curr.next
            # Reverse the current node's pointer
            curr.next = prev
            # Move prev to current node
            prev = curr
            # Move to next node
            curr = nxt

        # Prev becomes new head
        return prev

'''
Complexity
Time Complexity: O(n)
We visit every node exactly once.
Space Complexity: O(1)
Only three pointers are used.
'''