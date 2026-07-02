'''
1696. Jump Game VI
Medium
Topics
premium lock iconCompanies
Hint

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.

Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0

 

Constraints:

    1 <= nums.length, k <= 105
    -104 <= nums[i] <= 104

Algorithm

1. Create dp array.
   dp[i] = maximum score to reach index i

2. Base case:
   dp[0] = nums[0]

3. For every index i:
   dp[i] = nums[i] + maximum dp value from previous k indices

   Meaning:
   dp[i] = nums[i] + max(dp[i-k], dp[i-k+1], ..., dp[i-1])

4. To get max previous dp efficiently, use a deque.

5. Deque stores indices whose dp values are in decreasing order.

6. For every index i from 1 to n-1:

   a. Remove indices from front if they are outside jump range.

   b. Front of deque has index with maximum dp value.

   c. Calculate:
      dp[i] = nums[i] + dp[deque[0]]

   d. Remove indices from back while dp[i] >= dp[deque[-1]]
      because smaller values are useless.

   e. Add current index i into deque.

7. Return dp[n-1]

Time Complexity:
O(n)

Reason:
Each index is added and removed from deque at most once.

Space Complexity:
O(n)

Reason:
We use dp array and deque.

'''

from collections import deque

class Solution:
    def maxResult(self, nums, k):
        n = len(nums)

        # dp[i] = maximum score to reach index i
        dp = [0] * n
        dp[0] = nums[0]

        # Deque stores indices.
        # It keeps dp values in decreasing order.
        dq = deque([0])

        for i in range(1, n):

            # Remove indices that are more than k steps behind
            while dq and dq[0] < i - k:
                dq.popleft()

            # Best previous index is at front of deque
            dp[i] = nums[i] + dp[dq[0]]

            # Remove smaller/equal dp values from back
            # because current index is better for future jumps
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()

            # Add current index
            dq.append(i)

        return dp[n - 1]