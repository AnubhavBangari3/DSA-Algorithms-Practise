'''
Algorithm

1. Initialize the empty Hashmap
2. Interate through the array
3. For each element
   a. Compute diff= target-current number
   b. If diff exists in Hashmap return indices
4. Else store current number with indices in Hashmap


'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkDiff={}
        for num in range(len(nums)):
            diff=target-nums[num]
            if diff in checkDiff:
                return [checkDiff[diff],num]
            checkDiff[nums[num]]=num
        
'''

Time Complexity:
O(n)
Explanation:
We traverse the array only once
Hashmap operations (lookup + insert) = O(1)

Space Complexity:
O(n)
Explanation:
In worst case, we store all elements in hashmap
'''