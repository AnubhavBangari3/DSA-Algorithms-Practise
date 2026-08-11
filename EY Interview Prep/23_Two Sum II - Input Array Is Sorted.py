'''
167. Two Sum II - Input Array Is Sorted
Solved
Medium
Topics
premium lock iconCompanies

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.


    

'''

'''

1. Since the array is **sorted**, use the **Two Pointers** technique.
2. Place:
   - `l` at the beginning.
   - `r` at the end.
3. Calculate:

   `current_sum = numbers[l] + numbers[r]`

4. If `current_sum > target`:
   - We need a smaller sum.
   - Move `r` left.
5. If `current_sum < target`:
   - We need a larger sum.
   - Move `l` right.
6. If the sum equals `target`, return `[l + 1, r + 1]`.
7. Add `1` because the problem requires **1-based indexing**.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Since the array is sorted, we can use the two-pointer technique.
        # One pointer starts at the beginning (smallest value),
        # and the other starts at the end (largest value).
        l, r = 0, len(numbers) - 1

        # Continue searching while the pointers do not cross
        while l < r:

            # Calculate the sum of the values at the two pointers
            curSum = numbers[l] + numbers[r]

            # If the sum is greater than the target,
            # we need a smaller number → move the right pointer left
            if curSum > target:
                r -= 1

            # If the sum is smaller than the target,
            # we need a larger number → move the left pointer right
            elif curSum < target:
                l += 1

            # If the sum matches the target, we found the pair
            else:
                # The problem requires 1-based indexing
                return [l + 1, r + 1]

        # The problem guarantees exactly one solution,
        # so this line should never be reached
        return []

'''
Complexity
Time Complexity: O(n)
Each pointer moves at most n times.
Space Complexity: O(1)
Only two pointers are used.
'''