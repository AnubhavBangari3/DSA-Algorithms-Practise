class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Set to store numbers we have already seen
        seen = set()

        # Traverse the array
        for num in nums:

            # If number already exists, duplicate found
            if num in seen:
                return True

            # Store the current number
            seen.add(num)

        # No duplicate found
        return False

'''
1. Create an empty set called `seen`.
2. Traverse each number in the array.
3. Check if the number already exists in `seen`.
4. If yes, return `True`.
5. Otherwise, add the number to `seen`.
6. If the loop finishes, return `False`.

- **Time:** O(n)
- **Space:** O(n)

'''