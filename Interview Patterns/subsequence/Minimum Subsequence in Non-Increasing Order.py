class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ans=[]
        currentSum=0
        nums.sort(reverse=True)
        totalSum=sum(nums)
        for num in nums:
            totalSum-=num
            currentSum+=num
            ans.append(num)
            if currentSum > totalSum:
                return ans
        return ans
'''
1) Sort the array in descending order.
2) Compute the total sum of all elements.
3) Initialize:
   chosenSum = 0
   empty answer list.
4) Traverse the sorted array from largest to smallest.
5) For each number:
   Add it to the answer.
   Add it to chosenSum.
6) Remove it from the remaining sum (remainingSum = totalSum - chosenSum).
As soon as:
chosenSum > remainingSum

'''