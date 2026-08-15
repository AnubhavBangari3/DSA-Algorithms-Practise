'''
75. Sort Colors
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 

Constraints:

    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

'''

'''

1. Use the **Dutch National Flag Algorithm** with three pointers:
   - `l` → next position where `0` should go.
   - `i` → current element being processed.
   - `r` → next position where `2` should go.
2. Traverse while `i <= r`.
3. If `nums[i] == 0`:
   - Swap it with `nums[l]`.
   - Move `l` forward.
4. If `nums[i] == 2`:
   - Swap it with `nums[r]`.
   - Move `r` backward.
   - Process the swapped element again.
5. If `nums[i] == 1`:
   - Leave it in the middle.
6. Continue until `i > r`.
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # l -> next position to place 0
        l = 0
        # r -> next position to place 2
        r = len(nums) - 1
        # i -> current element being processed
        i = 0
        # Helper function to swap two elements
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        # Process elements until i crosses r
        while i <= r:
            # If current element is 0,
            # move it to the left partition.
            if nums[i] == 0:
                swap(l, i)
                l += 1
            # If current element is 2,
            # move it to the right partition.
            # Do not move i yet because the swapped
            # element must also be processed.
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            # Move to the next element.
            i += 1

'''
Complexity
Time Complexity: O(n)
Every element is processed at most a constant number of times.
Space Complexity: O(1)
Sorting is done in-place using three pointers.
'''