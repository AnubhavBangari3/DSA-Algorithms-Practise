'''
Algorithm: Remove Duplicates from Sorted Array (Two Pointers)

1. Initialize two pointers: i = 0 and j = 1.
2. Iterate while j < len(nums).
3. If nums[i] == nums[j]:
   - Remove the duplicate element using nums.pop(j).
   - Keep j unchanged to check the next shifted element.
4. Otherwise:
   - Update i = j.
   - Increment j by 1.
5. Repeat until j reaches the end of the array.
6. Return len(nums), representing the number of unique elements.

Time Complexity: O(n²) - pop(j) shifts remaining elements.
Space Complexity: O(1) - Modifies the array in place.

'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i,j=0,1

        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i=j
                j+=1
        return len(nums)
