class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Maximum product found overall
        global_max = nums[0]

        # Maximum and minimum product
        # ending at previous position
        prev_max = nums[0]
        prev_min = nums[0]

        # Process remaining elements
        for num in nums[1:]:

            # Current minimum product
            curr_min = min(
                num,
                prev_max * num,
                prev_min * num
            )

            # Current maximum product
            curr_max = max(
                num,
                prev_max * num,
                prev_min * num
            )

            # Update global maximum
            global_max = max(
                global_max,
                curr_max
            )

            # Move values forward
            prev_max = curr_max
            prev_min = curr_min

        return global_max

'''
1. Keep track of:
   - `prev_max` → maximum product ending at current position.
   - `prev_min` → minimum product ending at current position.
2. We need both because a negative number can turn:
   - a large negative product into a large positive product.
3. For every number, calculate:

   `curr_max = max(num, prev_max * num, prev_min * num)`

   `curr_min = min(num, prev_max * num, prev_min * num)`

4. Update the global maximum.
5. Move `prev_max` and `prev_min` forward.
6. Return the global maximum.

Complexity
Time Complexity: O(n)
Space Complexity: O(1)
'''