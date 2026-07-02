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

1. Initialize prev = None
2. Traverse the list while head exists
3. Store next node
4. Reverse current node's pointer
5. Move prev forward
6. Move head forward
7. Return prev as new head

Complexity
Time Complexity: O(n)
Reason:
We visit each node exactly once.
Space Complexity: O(1)
Reason:
We only use a few pointers (prev, nextNode), no extra data structure.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None

        while head:
            nextNode = head.next   # store next node
            head.next = prev       # reverse link
            prev = head            # move prev forward
            head = nextNode        # move head forward
        return prev