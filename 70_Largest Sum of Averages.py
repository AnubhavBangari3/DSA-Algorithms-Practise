'''
813. Largest Sum of Averages
Solved
Medium
Topics
premium lock iconCompanies

You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.

Note that the partition must use every integer in nums, and that the score is not necessarily an integer.

Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.

 

Example 1:

Input: nums = [9,1,2,3,9], k = 3
Output: 20.00000
Explanation: 
The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Example 2:

Input: nums = [1,2,3,4,5,6,7], k = 4
Output: 20.50000

 

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 104
    1 <= k <= nums.length

Algorithm

1. Use prefix sum to calculate average of any subarray quickly.

2. Define:
   dp[group][i] = maximum score we can get by partitioning
                  first i elements into group groups

3. Base case:
   dp[1][i] = average of nums[0 : i]

4. Transition:
   To calculate dp[group][i], try every possible last partition start.

   If last partition is nums[j : i],
   then:

   dp[group][i] =
       max(dp[group][i], dp[group - 1][j] + average(nums[j : i]))

5. Answer = dp[k][n]

Complexity

Time Complexity:
O(k * n^2)

Reason:
For every group and every ending index,
we try every possible partition point.

Space Complexity:
O(k * n)

Reason:
We use a DP table.

'''

class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)

        # prefix[i] = sum of first i elements
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Helper function to get average of nums[start:end]
        def average(start, end):
            return (prefix[end] - prefix[start]) / (end - start)

        # dp[group][i] = max score using first i elements in group groups
        dp = [[0.0] * (n + 1) for _ in range(k + 1)]

        # Base case:
        # With 1 group, score is average of first i elements
        for i in range(1, n + 1):
            dp[1][i] = average(0, i)

        # Fill DP table
        for group in range(2, k + 1):

            # Need at least group elements to make group non-empty partitions
            for i in range(group, n + 1):

                # Try all possible start positions of last partition
                for j in range(group - 1, i):

                    # Previous groups use first j elements
                    # Last group is nums[j:i]
                    dp[group][i] = max(
                        dp[group][i],
                        dp[group - 1][j] + average(j, i)
                    )

        return dp[k][n]