'''
2130. Maximum Twin Sum of a Linked List
Solved
Medium
Topics
premium lock iconCompanies
Hint

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

Example 2:

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Example 3:

Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

 

Constraints:

    The number of nodes in the list is an even integer in the range [2, 105].
    1 <= Node.val <= 105


Algorithm

1. Use slow and fast pointers to find the middle of the linked list.

2. Reverse the second half of the linked list.

3. Initialize max_sum = 0

4. Traverse:
   - one pointer from head
   - one pointer from reversed second half

5. For each pair:
   - compute twin sum
   - update max_sum

6. Return max_sum

Complexity
Time Complexity: O(n)
Reason:
Find middle → O(n)
Reverse second half → O(n)
Compare both halves → O(n)

Overall:

O(n)

because we drop constants.

Space Complexity: O(1)
Reason:
We only use pointers
No extra array / stack / hashmap

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Find middle of the linked List
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #Reverse the second half
        prev=None
        while slow:
            nextNode=slow.next
            slow.next=prev
            prev=slow
            slow=nextNode

        #compare 1st half and reversed second half
        first=head
        second=prev
        maxSum=0

        while second:
            maxSum=max(maxSum,first.val+second.val)
            first=first.next
            second=second.next

        return maxSum        