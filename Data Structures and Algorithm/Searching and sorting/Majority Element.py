from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1

            if d[num] > len(nums) / 2:
                return num
        

