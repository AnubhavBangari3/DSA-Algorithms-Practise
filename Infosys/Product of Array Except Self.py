'''
Algorithm: Product of Array Except Self (Prefix and Suffix Products)

1. Initialize n = len(nums).
2. Create an answer array of size n filled with 1.
3. Initialize left_product = 1.
4. Traverse the array from left to right:
   - Store left_product in answer[i].
   - Update left_product *= nums[i].
5. Initialize right_product = 1.
6. Traverse the array from right to left:
   - Update answer[i] *= right_product.
   - Update right_product *= nums[i].
7. Return answer containing the product of all elements except the current element.

Time Complexity: O(n)
Space Complexity: O(1) auxiliary space, excluding the output array.

'''


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)

        answer = [1] * n
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_productt
            right_product *= nums[i]

        return answer