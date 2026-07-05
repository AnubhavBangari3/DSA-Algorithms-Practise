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
1. Create a result array initialized with 1s.
2. Traverse the array from left to right while maintaining the product of all elements to the left of the current index.
3. Store the left product at each index in the result array, then update the left product by multiplying it with the current element.
4. Traverse the array from right to left while maintaining the product of all elements to the right of the current index.
5. Multiply the value already stored in the result array (left product) with the current right product.
6. Update the right product by multiplying it with the current element.
7. After both traversals, the result array contains the product of all elements except the current element.
8. Return the result array.
'''