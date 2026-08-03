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
1. Create an answer array initialized with 1.

2. Traverse from left to right:
   - Store the product of all elements to the left of the current index.
   - Update the running left product.

3. Traverse from right to left:
   - Multiply the current answer with the product of all elements to the right.
   - Update the running right product.

4. Return the answer array.

Key Idea:
For every index,

Product Except Self =
(Product of all elements on the left)
×
(Product of all elements on the right)

No division is required.

Time Complexity: O(n)

- Left traversal → O(n)
- Right traversal → O(n)

Overall:
O(n)

Space Complexity: O(1)

- Excluding the output array.
- Only two extra variables are used:
  left_product
  right_product

(Note:
The answer array is not counted as extra space according to the problem statement.)
'''