'''
740. Delete and Earn
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

 

Constraints:

    1 <= nums.length <= 2 * 104
    1 <= nums[i] <= 104

Algorithm

1. Count total points for each number.
   Example:
   nums = [2,2,3,3,3,4]
   points[2] = 4
   points[3] = 9
   points[4] = 4

2. Now the problem becomes House Robber:
   If we take number x, we cannot take x - 1 or x + 1.

3. Use DP:
   take = points gained if we take current number
   skip = points gained if we skip current number

4. Traverse from 1 to max(nums):

   new_take = skip + points[i]
   new_skip = max(take, skip)

   take = new_take
   skip = new_skip

5. Return max(take, skip)


Complexity

Time Complexity:
O(n + max_num)

Reason:
We count nums once and then process values from 1 to max_num.

Space Complexity:
O(max_num)

Reason:
We store points for each number.



'''

class Solution:
    def deleteAndEarn(self, nums):
        # Find maximum number to create points array
        max_num = max(nums)

        # points[i] = total points we can earn by deleting all i's
        points = [0] * (max_num + 1)

        # Build points array
        for num in nums:
            points[num] += num

        # House Robber style DP
        take = 0
        skip = 0

        # Process every value from 1 to max_num
        for i in range(1, max_num + 1):
            # If we take i, we must have skipped i - 1
            new_take = skip + points[i]

            # If we skip i, take best from previous state
            new_skip = max(take, skip)

            # Update states
            take = new_take
            skip = new_skip

        return max(take, skip)