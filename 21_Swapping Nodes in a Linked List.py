'''
1721. Swapping Nodes in a Linked List
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

 

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 105
    0 <= Node.val <= 100


Algorithm

1. Traverse the list to find the kth node from the beginning.
   Let this node be first.

2. Use another pointer (fast) starting from first.

3. Move fast to the end of the list.
   At the same time, move another pointer (second) from head.

4. When fast reaches the last node,
   second will be at the kth node from the end.

5. Swap values of first and second.

6. Return head.

Complexity

Time Complexity: O(n)
Space Complexity: O(1)



'''

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Step 1: Find kth node from beginning
        first = head
        for _ in range(k - 1):
            first = first.next
        
        # Step 2: Use two pointers to find kth from end
        fast = first
        second = head
        
        while fast.next:
            fast = fast.next
            second = second.next
        
        # Step 3: Swap values
        first.val, second.val = second.val, first.val
        
        return head