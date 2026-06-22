'''
78. Subsets
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums of unique elements, return all possible (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.

Algorithm

1. Use Backtracking (DFS).

2. At every index, we have two choices:
   - Include current element
   - Exclude current element

3. Store current subset in a temporary list.

4. Whenever DFS is called,
   add a copy of current subset to answer.

5. Explore remaining elements one by one.

6. After recursion,
   remove last element (Backtrack).

7. Return all generated subsets.
'''
class Solution:
    def subsets(self, nums):
        # Store all subsets
        result = []
        # Current subset being built
        subset = []
        # Backtracking function
        def dfs(index):
            # Store a copy of current subset
            result.append(subset[:])
            # Try including every remaining element
            for i in range(index, len(nums)):
                # Choose current element
                subset.append(nums[i])
                # Explore further
                dfs(i + 1)
                # Backtrack (remove last element)
                subset.pop()
        # Start from index 0
        dfs(0)
        return result
'''
Time Complexity:
O(n × 2^n)

Reason:
There are 2^n subsets and
copying each subset takes O(n).

Space Complexity:
O(n)

Reason:
Recursion stack and temporary subset.
(Output array is not counted.)

'''