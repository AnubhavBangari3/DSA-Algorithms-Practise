class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        # Result array
        answer = [1] * n
        # Store left products
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]
        # Store right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            # Multiply left and right products
            answer[i] *= right_product
            # Update right product
            right_product *= nums[i]

        return answer

'''
1. Create a result array initialized with `1`.
2. Traverse from left to right and store the product of all left elements.
3. Traverse from right to left and maintain the product of all right elements.
4. Multiply the left and right products for each index.
5. Return the result array.

- **Time:** O(n)
- **Space:** O(1) *(excluding the output array)*
'''