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


Algorithm
1. Initialize slow and fast pointers at head

2. Traverse:
   while fast and fast.next:
       slow moves 1 step
       fast moves 2 steps

3. When loop ends:
   slow will be at middle

4. Return slow

Complexity
Time Complexity: O(n)
Reason:
We traverse the list once
Fast moves 2 steps, but total operations still linear
Space Complexity: O(1)
Reason:
Only two pointers used

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
        