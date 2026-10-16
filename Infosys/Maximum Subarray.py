'''
Algorithm: Maximum Subarray (Kadane's Algorithm - Dynamic Programming)

1. Initialize a DP array of size n with zeros.
2. Set dp[0] = nums[0] as the first subarray sum.
3. Iterate through the array starting from index 1.
4. For each index i, calculate:
   - nums[i] + dp[i - 1] (extend the previous subarray).
   - nums[i] (start a new subarray).
5. Update dp[i] = max(nums[i] + dp[i - 1], nums[i]).
6. Repeat until all elements are processed.
7. Return max(dp) as the maximum subarray sum.

Time Complexity: O(n)
Space Complexity: O(n)

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):

            dp[i] = max(
                nums[i] + dp[i - 1],
                nums[i]
            )

        return max(dp)