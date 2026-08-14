'''
496. Next Greater Element I
Solved
Easy
Topics
premium lock iconCompanies

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

 

Constraints:

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.

 
Follow up: Could you find an O(nums1.length + nums2.length) solution?

'''

'''
1. Use a **Monotonic Stack** while traversing `nums2`.
2. The stack stores numbers whose next greater element has not been found yet.
3. For every number `n` in `nums2`:
   - While the stack is not empty and `n > stack[-1]`:
     - `n` is the next greater element for the top value.
     - Pop it and store the mapping.
4. Push the current number into the stack.
5. After traversal, any numbers still inside the stack have no greater element on the right.
   - Map them to `-1`.
6. Finally, build the result for `nums1` using the mapping.

'''

from typing import List

class Solution:
    def nextGreaterElement(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:

        # Stores final result
        result = []

        # Monotonic decreasing stack
        stack = []

        # number -> next greater element
        mapping = {}

        # Traverse nums2
        for num in nums2:

            # Current number is greater than stack top
            while stack and num > stack[-1]:

                # Current number is the next greater
                # element for the popped value
                smaller = stack.pop()
                mapping[smaller] = num

            # Push current number
            stack.append(num)

        # Remaining numbers have no greater element
        while stack:
            mapping[stack.pop()] = -1

        # Build answer for nums1
        for num in nums1:
            result.append(mapping[num])

        return result

'''

Complexity
Time Complexity: O(n + m)
Every element of nums2 is pushed and popped at most once.
Then we traverse nums1 once.
Space Complexity: O(n)
Stack and mapping can store elements from nums2.
'''