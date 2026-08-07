class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = Maximum subarray sum ending at index i
        dp = [0] * len(nums)

        # Base case: first element
        dp[0] = nums[0]

        # Build the DP array
        for i in range(1, len(nums)):

            # Either:
            # 1. Extend the previous subarray
            # 2. Start a new subarray from the current element
            dp[i] = max(nums[i] + dp[i - 1], nums[i])

        # The answer is the maximum value in dp
        return max(dp)

'''
1. Create a DP array where `dp[i]` stores the maximum subarray sum ending at index `i`.
2. Initialize `dp[0]` with the first element.
3. Traverse the array from index `1`.
4. For each element:
   - Extend the previous subarray.
   - Or start a new subarray from the current element.
5. Store the larger value in `dp[i]`.
6. Return the maximum value from the DP array.

- **Time:** O(n)
- **Space:** O(n)
'''