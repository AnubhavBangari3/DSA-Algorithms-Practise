'''
90. Subsets II
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums that may contain duplicates, return all possible (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10

Algorithm
1. Sort nums first.
   This brings duplicate numbers together.

2. Use Backtracking / DFS.

3. At every recursive call:
   - Add current subset to result.

4. Traverse from start index to end.

5. Before choosing nums[i], check duplicate condition:

   If i > start and nums[i] == nums[i - 1]:
       skip nums[i]

   Reason:
   This avoids generating the same subset again
   at the same recursion level.

6. Choose nums[i]:
   - Add nums[i] to subset
   - Call DFS(i + 1)
   - Remove nums[i] while backtracking

7. Return result.

'''
class Solution:
    def subsetsWithDup(self, nums):
        # Sort to group duplicate numbers together
        nums.sort()
        # Store all unique subsets
        result = []
        # Current subset
        subset = []
        def dfs(start):
            # Add copy of current subset
            result.append(subset[:])
            # Try all choices from start index
            for i in range(start, len(nums)):
                # Skip duplicates at same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Choose nums[i]
                subset.append(nums[i])
                # Explore next index
                dfs(i + 1)
                # Backtrack
                subset.pop()
        dfs(0)
        return result
'''
Time Complexity:
O(n * 2^n)

Reason:
There can be up to 2^n subsets,
and copying each subset can take O(n).

Space Complexity:
O(n)

Reason:
Recursion stack and temporary subset.
Output array is not counted.
'''