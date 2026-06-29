'''
15. 3Sum
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

Algorithm

1. Sort nums.
2. Create result list.
3. Fix one number nums[i] using a loop.
4. Skip duplicate nums[i] to avoid duplicate triplets.
5. For each fixed nums[i], use two pointers:
   left = i + 1
   right = len(nums) - 1
6. Calculate:
   total = nums[i] + nums[left] + nums[right]
7. If total == 0:
   - Add triplet to result
   - Move left and right
   - Skip duplicate left values
   - Skip duplicate right values
8. If total < 0:
   - Need bigger sum
   - Move left forward
9. If total > 0:
   - Need smaller sum
   - Move right backward
10. Return result.
'''
class Solution:
    def threeSum(self, nums):
        # Sort array to use two pointers and handle duplicates
        nums.sort()
        result = []
        n = len(nums)
        # Fix one number at a time
        for i in range(n - 2):
            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Two pointers for remaining two numbers
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # Found valid triplet
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # Sum too small, move left to increase sum
                elif total < 0:
                    left += 1
                # Sum too large, move right to decrease sum
                else:
                    right -= 1
        return result
'''
Time Complexity:
O(n²)

Reason:
Sorting takes O(n log n).
For each i, two pointer scan takes O(n).

Space Complexity:
O(1)

Reason:
No extra space except output.
'''