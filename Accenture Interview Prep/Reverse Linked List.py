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

Algorithm
1. Initialize:
   prev = None
   curr = head

2. Traverse the linked list until curr becomes None.

3. For every node:
   - Store next node.
   - Reverse current node's pointer.
   - Move prev forward.
   - Move curr forward.

4. When traversal finishes:
   prev points to the new head.

5. Return prev.

'''
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
Time Complexity:
O(n)

Reason:
Each node is visited exactly once.

Space Complexity:
O(1)

Reason:
Only three pointers are used.

'''