'''
1. Two Sum
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''

'''
Algorithm

1. Initialize the empty Hashmap
2. Interate through the array
3. For each element
   a. Compute diff= target-current number
   b. If diff exists in Hashmap return indices
4. Else store current number with indices in Hashmap

'''

class Solution:
    def twoSum(self, nums, target):
        # Stores number -> index
        checkDiff = {}

        for i, num in enumerate(nums):
            # Required number to make target
            diff = target - num

            # If required number already exists
            if diff in checkDiff:
                return [checkDiff[diff], i]

            # Store current number with index
            checkDiff[num] = i

'''
Time Complexity:
O(n)
Explanation:
We traverse the array only once
Hashmap operations (lookup + insert) = O(1)

Space Complexity:
O(n)
Explanation:
In worst case, we store all elements in hashmap
'''