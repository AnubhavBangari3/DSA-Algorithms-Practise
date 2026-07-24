class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people's weights in ascending order.
        people.sort()

        # Two pointers:
        # left  -> lightest person
        # right -> heaviest person
        left = 0
        right = len(people) - 1

        # Counts the minimum number of boats needed.
        boats = 0

        # Continue until all people have been assigned a boat.
        while left <= right:

            # Always place the heaviest person in a boat.
            remaining_capacity = limit - people[right]
            right -= 1

            # One boat is used.
            boats += 1

            # If the lightest person can fit with the
            # heaviest person, place them together.
            if left <= right and people[left] <= remaining_capacity:
                left += 1

        return boats

'''
Algorithm

1. Sort the array of people's weights.

2. Initialize two pointers:
   - left = lightest person.
   - right = heaviest person.

3. Initialize the boat count as 0.

4. While left <= right:

   a. Always place the heaviest person in a boat.

   b. Check if the lightest person can fit
      in the same boat.

   c. If yes:
      - Move the left pointer.

   d. Move the right pointer because the
      heaviest person has already been placed.

   e. Increase the boat count.

5. Return the total number of boats.

Pattern:
Greedy + Two Pointers

Time Complexity: O(n log n)

Space Complexity: O(1)

'''