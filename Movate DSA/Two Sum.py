class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionary to store number -> index
        seen = {}

        # Traverse the array
        for i, num in enumerate(nums):

            # Find the number needed to reach target
            diff = target - num

            # If required number is already seen, return indices
            if diff in seen:
                return [seen[diff], i]

            # Store current number with its index
            seen[num] = i

'''
Algorithm
1. Create an empty dictionary.
2. Traverse the array.
3. For each number, calculate the required value (`target - current number`).
4. If the required value is already in the dictionary, return both indices.
5. Otherwise, store the current number and its index.
6. Continue until the pair is found.


Time Complexity
- **Time:** O(n)
- **Space:** O(n)
'''