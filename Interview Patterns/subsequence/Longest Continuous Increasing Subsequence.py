class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                ans[i]+=ans[i-1]
        return max(ans)
        
'''
1) Initialize an array where each element represents the length of the longest increasing continuous subarray ending at that index.
2) Since every element by itself is an increasing subarray, initialize every value to 1.
3) Traverse the array from the second element.
4) For each element:
   If the current element is greater than the previous element, extend the previous increasing sequence by one.
   Otherwise, start a new increasing sequence of length 1.
5) Keep track of the maximum length.
6) Return the maximum length.

'''