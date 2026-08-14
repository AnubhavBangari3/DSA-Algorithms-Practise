'''
21. Merge Two Sorted Lists
Solved
Easy
Topics
premium lock iconCompanies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.



'''



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