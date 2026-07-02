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

1. Initialize an empty set

2. Traverse each element in array:

   If element is already in set:
       return True   (duplicate found)

   Else:
       add element to set

3. If traversal completes:
   return False   (all elements are unique)

Complexity

Time Complexity:
O(n) → single pass

Space Complexity:
O(n) → set stores elements



'''

class Solution:
    def containsDuplicate(self, nums):
        # Set to store seen elements
        seen = set()
        
        # Traverse array
        for num in nums:
            
            # If already seen → duplicate exists
            if num in seen:
                return True
            
            # Otherwise add to set
            seen.add(num)
        
        # No duplicates found
        return False