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


'''
'''
1. Use **Floyd's Cycle Detection Algorithm** with two pointers:
   - `slow` → moves one step at a time.
   - `fast` → moves two steps at a time.
2. Start both pointers at `head`.
3. While `fast` and `fast.next` exist:
   - Move `slow` one step.
   - Move `fast` two steps.
4. If `slow == fast`, both pointers have met inside the cycle.
   - Return `True`.
5. If `fast` reaches the end (`None`), there is no cycle.
6. Return `False`.
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
Complexity
Time Complexity: O(n)
Both pointers traverse at most a linear number of nodes.
Space Complexity: O(1)
Only two pointers are used.
'''