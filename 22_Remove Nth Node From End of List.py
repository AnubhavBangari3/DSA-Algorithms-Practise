'''
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

 

Follow up: Could you do this in one pass?

Algorithm
1. Use a dummy node pointing to head (to handle edge cases like deleting head).

2. Initialize two pointers:
   - fast = dummy
   - slow = dummy

3. Move fast pointer n+1 steps ahead.

4. Now move both fast and slow together until fast reaches the end.

5. At this point:
   slow is just before the node to be deleted.

6. Remove the node:
   slow.next = slow.next.next

7. Return dummy.next

Complexity
Time Complexity: O(n)
Space Complexity: O(1)


'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Delete nth node from end
        slow.next = slow.next.next
        
        return dummy.next