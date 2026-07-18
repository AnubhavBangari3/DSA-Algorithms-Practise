class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # ---------------- STEP 1 : FIND THE MEETING POINT ----------------

        # Initialize both pointers at the starting node.
        slow = nums[0]
        fast = nums[0]

        # Move slow by one step and fast by two steps.
        # Since a duplicate creates a cycle, both pointers will eventually meet.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            # Stop when both pointers meet inside the cycle.
            if slow == fast:
                break

        # ---------------- STEP 2 : FIND THE START OF THE CYCLE ----------------

        # Start another pointer from the beginning.
        slow2 = nums[0]

        # Move both pointers one step at a time.
        # They will meet at the beginning of the cycle,
        # which is the duplicate number.
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        # Return the duplicate number.
        return slow
    
'''
Algorithm

1. Treat the array as a linked list:
   - Index represents the current node.
   - Value represents the next node.

2. Initialize two pointers:
   - slow at the starting node.
   - fast at the starting node.

3. Move:
   - slow one step at a time.
   - fast two steps at a time.

4. Continue until both pointers meet.
   - This confirms the presence of a cycle.

5. Initialize another pointer from the starting node.

6. Move both pointers one step at a time.

7. The node where they meet is the beginning of the cycle.

8. Return this node as the duplicate number.

Pattern:
Floyd's Cycle Detection (Tortoise and Hare)

Time Complexity: O(n)

Space Complexity: O(1)

'''