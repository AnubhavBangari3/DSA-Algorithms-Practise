'''
1. Use **Backtracking**.
2. Maintain:
   - `subset` → current subset being built.
   - `result` → stores all subsets.
3. At every DFS call:
   - Add a copy of the current subset to `result`.
4. Loop through the remaining elements.
5. For each element:
   - Add it to `subset`.
   - Call DFS for the next index.
   - Remove it after returning to backtrack.
6. Return all subsets.

Complexity
Time Complexity: O(n × 2^n)
Space Complexity: O(n) recursion space, excluding output.
'''

class Solution:
    def subsets(self, nums):

        # Store all subsets
        result = []

        # Current subset
        subset = []

        def dfs(index):

            # Add copy of current subset
            result.append(subset[:])

            # Try every remaining element
            for i in range(index, len(nums)):

                # Choose
                subset.append(nums[i])

                # Explore
                dfs(i + 1)

                # Backtrack
                subset.pop()

        # Start from first index
        dfs(0)

        return result

