'''
141. Linked List Cycle
Solved
Easy
Topics
premium lock iconCompanies

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

 

Follow up: Can you solve it using O(1) (i.e. constant) memory?


Algo

1. Use two pointers:

   slow -> moves one step at a time
   fast -> moves two steps at a time

2. Initialize:
   slow = head
   fast = head

3. Traverse the linked list while:
   fast != None
   and fast.next != None

4. Move:
   slow = slow.next
   fast = fast.next.next

5. If slow == fast:
      Cycle exists
      return True

6. If loop finishes:
      No cycle exists
      return False


'''
class Solution:
    def hasCycle(self, head):
        # Slow and fast pointers
        slow = head
        fast = head
        # Traverse while fast pointer can move
        while fast and fast.next:
            # Move slow by one step
            slow = slow.next
            # Move fast by two steps
            fast = fast.next.next
            # If both pointers meet,
            # cycle exists
            if slow == fast:
                return True
        # Fast reached end of list
        # No cycle
        return False
'''
Time Complexity:
O(n)

Reason:
Each pointer traverses the list at most once.

Space Complexity:
O(1)

Reason:
Only two pointers are used.

'''