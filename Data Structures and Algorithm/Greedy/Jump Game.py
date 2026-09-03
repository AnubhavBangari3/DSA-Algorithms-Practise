
'''
1. Use a **Greedy** approach.
2. Keep `max_reach` = farthest index we can currently reach.
3. Traverse the array.
4. If `i > max_reach`, we cannot reach index `i`, so return `False`.
5. Otherwise update:

   `max_reach = max(max_reach, i + nums[i])`

6. If `max_reach` reaches the last index, return `True`.

Complexity
Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Farthest index we can reach
        max_reach = 0

        # Last index
        end = len(nums) - 1

        for i in range(len(nums)):

            # Cannot reach current index
            if i > max_reach:
                return False

            # Update farthest reachable index
            max_reach = max(
                max_reach,
                i + nums[i]
            )

            # Last index is reachable
            if max_reach >= end:
                return True

        return False