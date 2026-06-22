'''
39. Combination Sum
Solved
Medium
Topics
premium lock iconCompanies

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

 

Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40

Algorithm

1. Use Backtracking / DFS.

2. Maintain:
   - current combination
   - current remaining target
   - start index

3. At every step:
   If remaining target == 0:
      add current combination to result

4. If remaining target < 0:
      stop that path

5. For each candidate from start index:
   - Choose candidate
   - Recurse with reduced target

6. Since same number can be reused:
   call dfs(i, remaining - candidates[i])

7. Backtrack by removing last chosen number.

8. Return result.
'''
class Solution:
    def combinationSum(self, candidates, target):
        # Store all valid combinations
        result = []
        # Current combination
        path = []
        def dfs(start, remaining):
            # If target becomes 0, valid combination found
            if remaining == 0:
                result.append(path[:])
                return
            # If remaining becomes negative, invalid path
            if remaining < 0:
               return

            # Try every candidate from start index
            for i in range(start, len(candidates)):
                # Choose current candidate
                path.append(candidates[i])
                # Reuse allowed, so pass i again
                dfs(i, remaining - candidates[i])
                # Backtrack
                path.pop()
        dfs(0, target)
        return result
'''
Time Complexity:
O(2^target) approximately

Reason:
Each candidate can be reused multiple times,
so recursion tree depends on target.

Space Complexity:
O(target)

Reason:
Recursion depth can go up to target / smallest candidate.
Output list is not counted.
'''