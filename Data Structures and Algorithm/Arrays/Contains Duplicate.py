class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

'''
1) Create an empty set to store the elements seen so far.
2) Traverse the array one element at a time.
3) For each element:
  Check if it already exists in the set.
  If it exists, a duplicate has been found, so return True.
  Otherwise, add the element to the set.
4) If the entire array is traversed without finding a duplicate, return False.
'''