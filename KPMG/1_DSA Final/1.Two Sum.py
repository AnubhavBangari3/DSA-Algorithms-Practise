class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap to store:
        # number -> index
        differences = {}

        # Traverse the array once
        for i, num in enumerate(nums):

            # Find the number needed to make the target
            diff = target - num

            # If the required number has already been seen,
            # return its index and the current index
            if diff in differences:
                return [differences[diff], i]

            # Otherwise, store the current number and its index
            differences[num] = i
'''
1. Create an empty HashMap to store:
   Number -> Index.

2. Traverse the array once.

3. For each number:
   - Compute the required complement:
     complement = target - current_number.

4. Check if the complement already exists in the HashMap.
   - If yes, return the stored index and the current index.

5. Otherwise, store the current number and its index in the HashMap.

6. Since the problem guarantees exactly one solution, the answer will be found during traversal.

Time Complexity: O(n)
- Traverse the array once.
- HashMap lookup and insertion take O(1) on average.

Space Complexity: O(n)
- In the worst case, the HashMap stores all elements.
'''