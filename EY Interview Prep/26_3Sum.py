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


'''
'''

1. Sort the array.
2. Fix one number `nums[i]`.
3. Use two pointers:
   - `left = i + 1`
   - `right = len(nums) - 1`
4. Calculate:

   `total = nums[i] + nums[left] + nums[right]`

5. If `total < 0`:
   - Move `left` right to increase the sum.
6. If `total > 0`:
   - Move `right` left to decrease the sum.
7. If `total == 0`:
   - Add the triplet to the result.
   - Move both pointers.
   - Skip duplicates.
8. Also skip duplicate values for the first number.

'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:   
        # This will store all unique triplets that sum to 0
        res = []
        # Step 1: Sort the array
        # Sorting allows us to use the two pointer technique
        # and also helps in easily skipping duplicates
        nums.sort()
        # Step 2: Fix one element and find the other two using two pointers
        for i, a in enumerate(nums):
            # Skip duplicate values for the first element
            # to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue
            # Initialize two pointers
            l, r = i + 1, len(nums) - 1
            # Step 3: Use two pointers to find pairs that sum with 'a' to 0
            while l < r:
                # Calculate the current sum of the triplet
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    # If sum is too large, move right pointer left
                    # to decrease the sum
                    r -= 1
                elif threeSum < 0:
                    # If sum is too small, move left pointer right
                    # to increase the sum
                    l += 1
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    # Move both pointers inward
                    l += 1
                    r -= 1
                    # Skip duplicate values for the second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # Skip duplicate values for the third number
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        # Return all unique triplets
        return res

'''
Complexity
Time Complexity: O(n²)
Sorting takes O(n log n).
For each element, two pointers scan the remaining array.
Overall: O(n²).
Space Complexity: O(1) extra space
Ignoring the output array and sorting implementation.

'''