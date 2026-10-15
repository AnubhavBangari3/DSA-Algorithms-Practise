'''
Algorithm: Two Sum (Hash Map)

1. Initialize an empty dictionary 'seen' to store numbers and their indices.
2. Iterate through the array using enumerate().
3. Calculate the complement: diff = target - num.
4. If diff exists in seen, return [seen[diff], i].
5. Otherwise, store the current number and its index in seen.
6. Repeat until the required pair is found.

Time Complexity: O(n)
Space Complexity: O(n)

'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}

        for i,num in enumerate(nums):
            diff=target-num

            if diff in seen:
                return [seen[diff],i]

            seen[num]=i


        