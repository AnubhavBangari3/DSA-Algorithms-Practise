'''
1. Use **Backtracking**.
2. Maintain:
   - `path` → current permutation.
   - `visited` → tracks which numbers are already used.
   - `result` → stores all complete permutations.
3. Try every number at every position.
4. If a number is already used, skip it.
5. Otherwise:
   - Mark it visited.
   - Add it to `path`.
   - Run DFS.
6. After recursion:
   - Remove it from `path`.
   - Mark it unvisited.
7. When `len(path) == len(nums)`, store a copy in `result`.

Complexity
Time Complexity: O(n × n!)
Space Complexity: O(n) recursion space, excluding output.
'''

class Solution:
    def permute(self, nums):

        # Store all permutations
        result = []

        # Current permutation
        path = []

        # Track used elements
        visited = [False] * len(nums)

        def dfs():

            # Complete permutation formed
            if len(path) == len(nums):
                result.append(path[:])
                return

            # Try every number
            for i in range(len(nums)):

                # Skip already used number
                if visited[i]:
                    continue

                # Choose
                visited[i] = True
                path.append(nums[i])

                # Explore
                dfs()

                # Backtrack
                path.pop()
                visited[i] = False

        dfs()

        return result