class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:    
        # Since the array is sorted, we can use the two-pointer technique.
        # One pointer starts at the beginning (smallest value),
        # and the other starts at the end (largest value).
        l, r = 0, len(numbers) - 1
        # Continue searching while the pointers do not cross
        while l < r:
            # Calculate the sum of the values at the two pointers
            curSum = numbers[l] + numbers[r]
            # If the sum is greater than the target,
            # we need a smaller number → move the right pointer left
            if curSum > target:
                r -= 1
            # If the sum is smaller than the target,
            # we need a larger number → move the left pointer right
            elif curSum < target:
                l += 1
            # If the sum matches the target, we found the pair
            else:
                # The problem requires 1-based indexing
                return [l + 1, r + 1]
        # The problem guarantees exactly one solution,
        # so this line should never be reached
        return []
    
'''
Algorithm

1. Initialize two pointers:
   - left at the beginning of the sorted array.
   - right at the end of the sorted array.

2. Traverse while left is less than right.

3. Calculate the sum of the elements at the two pointers.

4. If the sum is equal to the target:
   - Return the 1-based indices of the two elements.

5. If the sum is less than the target:
   - Move the left pointer one step to the right to increase the sum.

6. If the sum is greater than the target:
   - Move the right pointer one step to the left to decrease the sum.

7. Continue until the pair is found.

Pattern:
Two Pointers (Sorted Array)

Time Complexity: O(n)
Space Complexity: O(1)
'''