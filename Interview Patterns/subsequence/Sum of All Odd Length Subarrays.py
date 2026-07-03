class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(0,len(arr) + 1,2):
            for j in range(len(arr) - i):
                ans += sum(arr[j:j+ i + 1])
                
        return ans
'''
1) Consider every possible odd subarray length (1, 3, 5, ...).
2) For each odd length, slide a window across the array.
3) Compute the sum of each odd-length subarray.
4) Add its sum to the final answer.
5) Return the accumulated sum.

'''