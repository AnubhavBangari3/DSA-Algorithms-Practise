'''
41. First Missing Positive
Solved
Hard
Topics
premium lock iconCompanies
Hint

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1

Algorithm
Cyclic placement approach
1. Let n = len(nums)

2. Traverse the array with index i = 0

3. While nums[i] is in range [1, n]
   and nums[i] is not already in its correct position
   and nums[i] != nums[nums[i] - 1]:
       swap nums[i] with nums[nums[i] - 1]

4. After placement, scan the array again:
   - if nums[i] != i + 1, then i + 1 is the first missing positive

5. If all positions are correct, return n + 1

Complexity
Time Complexity: O(n)
Reason:

Each number is moved at most into its correct place a limited number of times. Although there is a while loop with swaps, each swap puts at least one element closer to its final position, so total work across the whole array is linear.

Space Complexity: O(1)
Reason:

We rearrange the array in-place and only use a few extra variables like i and correct_idx.

'''
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