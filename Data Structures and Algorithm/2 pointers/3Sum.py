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
Algorithm

1. Create an empty result list to store unique triplets.

2. Sort the array.

3. Traverse the array and fix one number at index i.

4. If the current fixed number is the same as the previous fixed number,
   skip it to avoid duplicate triplets.

5. For the remaining part of the array, use two pointers:
   - left = i + 1
   - right = last index

6. Calculate:
   current_sum = nums[i] + nums[left] + nums[right]

7. If current_sum is less than 0:
   - Move left pointer right to increase the sum.

8. If current_sum is greater than 0:
   - Move right pointer left to decrease the sum.

9. If current_sum equals 0:
   - Add the triplet to the result.
   - Move both pointers inward.
   - Skip duplicate values for left and right.

10. After checking all possible fixed numbers, return the result.

Pattern:
Sorting + Two Pointers

Time Complexity: O(n²)
Space Complexity: O(1) extra space excluding output
'''