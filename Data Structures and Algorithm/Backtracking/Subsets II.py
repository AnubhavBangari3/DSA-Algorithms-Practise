'''
1. Sort `nums` so duplicate values come together.
2. Use **Backtracking**.
3. Maintain:
   - `subset` → current subset.
   - `result` → all unique subsets.
4. At every DFS call, add a copy of `subset` to `result`.
5. Loop from `start` to the end.
6. Skip duplicates at the **same recursion level**:

   `if i > start and nums[i] == nums[i - 1]: continue`

7. Choose the current number, recurse, then backtrack.
8. Return `result`.

Complexity
Time Complexity: O(n × 2^n)
Space Complexity: O(n) recursion space, excluding output.
'''


class Solution:
    def subsetsWithDup(self, nums):

        # Sort so duplicates are adjacent
        nums.sort()

        # Store all unique subsets
        result = []

        # Current subset
        subset = []

        def dfs(start):

            # Add copy of current subset
            result.append(subset[:])

            # Try all choices
            for i in range(start, len(nums)):

                # Skip duplicate choices
                # at the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Choose
                subset.append(nums[i])

                # Explore
                dfs(i + 1)

                # Backtrack
                subset.pop()

        dfs(0)

        return result