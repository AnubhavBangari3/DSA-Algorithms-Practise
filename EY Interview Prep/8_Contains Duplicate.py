"""
217. Contains Duplicate

Problem:

Given an integer array nums,

Return:

True  -> if any value appears more than once

False -> if all values are unique

Examples:

Input: nums = [1,2,3,1]
Output: True

Input: nums = [1,2,3,4]
Output: False

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: HashSet Lookup
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Create empty set called seen

2. Traverse array

3. For each number:

      If number already exists in set:
            return True

      Else:
            add number to set

4. If traversal completes:
      return False
"""

class Solution:
    def containsDuplicate(self, nums):

        # Stores unique numbers
        seen = set()

        for num in nums:

            # Duplicate found
            if num in seen:
                return True

            # Store number
            seen.add(num)

        return False


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Traverse array once
- Set lookup = O(1)
- Set insertion = O(1)

Overall:
O(n)

Space Complexity: O(n)

Explanation:
- Worst case:
all elements unique

Set stores entire array
"""