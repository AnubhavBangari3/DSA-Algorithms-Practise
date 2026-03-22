'''
Algorithm
Floyd’s Cycle Detection
1. Initialize two pointers:
   slow = head
   fast = head

2. Traverse the list:
   while fast and fast.next:
       slow moves 1 step
       fast moves 2 steps

3. If slow == fast:
       cycle exists → return True

4. If loop ends:
       no cycle → return False


'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

            if fast == slow:
                return True

        return False
        
'''
Time Complexity:
O(n)

Reason:
- In the worst case, both slow and fast pointers traverse the linked list.
- Slow pointer moves one step at a time → up to n steps.
- Fast pointer moves two steps at a time → also bounded by n steps.
- Even in a cycle, they meet within at most n iterations.
- Therefore, total operations are linear → O(n).

------------------------------------------------

Space Complexity:
O(1)

Reason:
- We are only using two pointers (slow and fast).
- No extra data structures (like hash sets or arrays) are used.
- Memory usage does not grow with input size.
- Hence, constant space → O(1).
'''