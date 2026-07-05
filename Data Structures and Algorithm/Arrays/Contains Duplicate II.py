class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False
        
'''
1) Create an empty set to store the elements in the current window.
2) Traverse the array from left to right.
3) For each element:
  Check if it already exists in the set.
  If yes, a duplicate exists within distance k, so return True.
  Otherwise, add the current element to the set.
4) If the window size exceeds k, remove the element that falls out of the window.
5) If the traversal completes without finding a valid duplicate, return False.

'''