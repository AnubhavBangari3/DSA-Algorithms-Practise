'''
46. Permutations
Solved
Medium
Topics
premium lock iconCompanies

Given an array nums of distinct integers, return all the possible . You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

Algorithm

1. Use Backtracking / DFS.

2. Maintain:
   - current permutation (path)
   - visited array

3. If current permutation size == nums length:
      add copy of permutation to result
      return

4. Traverse every number.

5. If number is already used:
      skip it

6. Otherwise:
      - mark as visited
      - add to current permutation
      - recurse
      - remove last element (backtrack)
      - mark as not visited

7. Return result.

'''
class Solution:
    def permute(self, nums):
        # Store all permutations
        result = []
        # Current permutation being built
        path = []
        # Track used elements
        visited = [False] * len(nums)
        # Backtracking function
        def dfs():
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path[:])
                return
            # Try every number
            for i in range(len(nums)):
                # Skip if already used
                if visited[i]:
                    continue
                # Choose current number
                visited[i] = True
                path.append(nums[i])
                # Explore further
                dfs()
                # Backtrack
                path.pop()
                visited[i] = False
        dfs()
        return result

'''
Time Complexity:
O(n × n!)

Reason:
There are n! permutations.
Copying each permutation takes O(n).

Space Complexity:
O(n)

Reason:
Visited array + recursion stack.
(Output list is not counted.)

'''