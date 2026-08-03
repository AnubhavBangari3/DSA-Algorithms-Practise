class Solution:
    def rotate(self, nums: List[int], k: int) -> None:    
        # Helper function to reverse elements between indices i and j
        # This swaps elements moving inward until the pointers meet
        def swap(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            return nums   
        # If k is larger than the array size,
        # rotating k times is equivalent to rotating k % n times
        if k > len(nums):
            k %= len(nums)
        # Only rotate if k > 0
        if k > 0:
            # Step 1: Reverse the entire array
            # Example: [1,2,3,4,5,6,7] → [7,6,5,4,3,2,1]
            swap(nums, 0, len(nums) - 1)
            # Step 2: Reverse the first k elements
            # Example: [7,6,5,4,3,2,1] → [5,6,7,4,3,2,1]
            swap(nums, 0, k - 1)
            # Step 3: Reverse the remaining elements
            # Example: [5,6,7,4,3,2,1] → [5,6,7,1,2,3,4]
            swap(nums, k, len(nums) - 1)

'''
1. Compute:
   k = k % n
   (Rotating n times gives the same array.)

2. Reverse the entire array.

3. Reverse the first k elements.

4. Reverse the remaining n-k elements.

5. The array is now rotated to the right by k positions.

Key Idea:
Instead of shifting elements one by one, use three reversals to achieve the rotation in O(n) time and O(1) extra space.

Time Complexity: O(n)

- Reverse entire array → O(n)
- Reverse first k elements → O(k)
- Reverse remaining elements → O(n-k)

Overall:
O(n)

Space Complexity: O(1)

- Rotation is done in-place.
'''