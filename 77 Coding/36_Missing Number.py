'''
268. Missing Number
Solved
Easy
Topics
premium lock iconCompanies

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:

Input: nums = [0,1]

Output: 2

Explanation:

n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]

Output: 8

Explanation:

n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
 

 

 

 

Constraints:

    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.

 

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Algo
1. Sort the array (if not already sorted)

2. Initialize two pointers:
   left = 0
   right = n - 1

3. Apply Binary Search:
   while left <= right:
       mid = (left + right) // 2

       if nums[mid] == mid:
           → missing number is on right side
           → move left = mid + 1
       else:
           → missing number is on left side
           → move right = mid - 1

4. After loop ends, return left
   → left will point to the missing number

Complexity

Time Complexity:
O(n log n) → due to sorting
O(log n) → binary search

Overall: O(n log n)

(If array already sorted → O(log n))

Space Complexity:
O(1) → no extra space used


'''
class Solution:
    def missingNumber(self, nums):
        # Step 1: Sort the array (skip if already sorted)
        nums.sort()
        
        # Step 2: Initialize pointers
        left = 0
        right = len(nums) - 1
        
        # Step 3: Binary Search
        while left <= right:
            mid = (left + right) // 2
            
            # If value matches index → missing is on right side
            if nums[mid] == mid:
                left = mid + 1
            else:
                # If mismatch → missing is on left side
                right = mid - 1
        
        # Step 4: 'left' is the missing number
        return left