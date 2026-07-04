class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d={} 
        for i,num in enumerate(nums):
            diff=target - num
            if diff in d:
                return [d[diff],i]
            d[num]=i

'''
1) Create ab empty hash map to store number and indices
2) Traverse the array from left to right
3) For each element
   calculate the value needed for target
   check if the value exists in hash map
4) If it exists
   Return the index stored in the hash map and the current index.
5) Otherwise
   Store the current element and its index in the hash map.
6) Since the problem guarantees exactly one solution, the algorithm will eventually return the required pair.

'''