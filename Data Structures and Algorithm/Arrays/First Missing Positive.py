class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
    
'''
Algorithm

1. Let n be the length of the array.
2. Traverse the array using index i.
3. For each nums[i], check if it is a useful positive number.
   A number is useful only if it lies between 1 and n.
4. If nums[i] is between 1 and n, find its correct index:
   correct_index = nums[i] - 1
5. If nums[i] is not already at its correct position,
   swap nums[i] with nums[correct_index].
6. Do not move i immediately after swapping,
   because the new value at index i also needs to be checked.
7. If nums[i] is out of range, duplicate, or already correctly placed,
   move to the next index.
8. After rearranging, scan the array again.
9. The first index i where nums[i] != i + 1 means i + 1 is missing.
10. If every index contains the correct value,
    return n + 1.

Pattern:
Cyclic Sort / Index Placement

Time Complexity: O(n)
Space Complexity: O(1)

'''