class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur=maxSum=sum(nums[:k])

        for i in range(k,len(nums)):
            cur+=nums[i]-nums[i-k]
            maxSum=max(maxSum,cur)
        return maxSum/k

'''
1)Take the sum of the first k elements.
2)Store it as both:
 current window sum
 maximum sum found so far
3)Move the window one step at a time.
4)For every new element:
 Add the new element entering the window.
 Remove the old element leaving the window.
5)After updating the window sum, compare it with the maximum sum.
6)At the end, divide the maximum sum by k to get the maximum average.

'''