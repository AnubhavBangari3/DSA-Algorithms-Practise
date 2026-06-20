'''
217. Contains Duplicate
Solved
Easy
Topics
premium lock iconCompanies

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109


Algorithm

1. Create an empty set.

2. Traverse the array.

3. For each number:
   - If number already exists in set:
       return True
   - Otherwise add it to set

4. If traversal completes:
   return False

'''

class Solution:
    def containsDuplicate(self, nums):

        # Store seen numbers
        seen = set()

        # Traverse array
        for num in nums:

            # Duplicate found
            if num in seen:
                return True

            # Add current number
            seen.add(num)

        # No duplicates found
        return False
    
'''
Time Complexity:
O(n)

Reason:
Each lookup and insertion in set takes O(1) average time.

Space Complexity:
O(n)

Reason:
In worst case all elements are unique and stored in set.

'''