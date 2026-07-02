'''
234. Palindrome Linked List
Solved
Easy
Topics
premium lock iconCompanies

Given the head of a singly linked list, return true if it is a or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?

Algorithm
1. Find middle using slow & fast pointer

2. Reverse second half of list

3. Compare first half and second half:
   - If mismatch → return False

4. If all match → return True
Example:
1 → 2 → 2 → 1
Step 1: Find middle
slow = 2 (middle)
Step 2: Reverse second half
1 → 2 → 2 → 1
        ↓
        1 → 2
becomes:
        2 → 1
Step 3: Compare
1 == 1
2 == 2

✔️ Palindrome
Complexity
Time Complexity: O(n)
Reason:
Find middle → O(n)
Reverse → O(n)
Compare → O(n)

Total = O(n)

Space Complexity: O(1)
Reason:
No extra data structures
Only pointers used
'''

# Definition for singly-linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Find Middle
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        #Reverse Second half
        while slow:
            nextNode = slow.next      # Store next node (to not lose reference)
            slow.next = prev          # Reverse the current node's pointer
            prev = slow               # Move prev forward (new head of reversed list)
            slow = nextNode           # Move to next node in original list

        #Compare
        left=head
        right=prev

        while right:
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True