class Solution:
    def totalFruit(self, fruits: List[int]):

        # Left pointer of the sliding window
        start = 0

        # Right pointer of the sliding window
        end = 0

        # Stores:
        # fruit_type -> latest index where it appeared
        last_index = {}

        # Maximum fruits collected
        max_fruits = 0

        # Expand the window
        while end < len(fruits):

            # Update latest index of current fruit
            last_index[fruits[end]] = end

            # More than 2 fruit types?
            if len(last_index) >= 3:

                # Find the fruit that appeared earliest
                earliest_index = min(last_index.values())

                # Remove that fruit from the basket
                del last_index[fruits[earliest_index]]

                # Shrink window
                start = earliest_index + 1

            # Update maximum window size
            max_fruits = max(max_fruits, end - start + 1)

            # Expand window
            end += 1

        return max_fruits

'''
1. Initialize two pointers:
   start = 0
   end = 0

2. Create a dictionary to store:
   fruit_type -> latest index.

3. Expand the window by moving end.

4. Update the latest index of the current fruit.

5. If the window contains more than 2 fruit types:
   • Find the smallest stored index.
   • Remove that fruit from the dictionary.
   • Move start to earliest_index + 1.

6. Update the maximum window size.

7. Continue until end reaches the end of the array.

8. Return the maximum window size.

Key Idea:

Maintain a sliding window that always contains
at most two fruit types.
Whenever a third type appears,
remove the fruit whose last occurrence is the earliest.


Time Complexity:

Each fruit is processed once.

Dictionary operations:
Insert/Delete/Search = O(1)

Finding minimum last index:

min(dictionary.values())

Dictionary size is at most 3,
so this is O(1).

Overall:

O(n)

--------------------------------

Space Complexity:

Dictionary stores at most
3 fruit types.

Overall:

O(1)

'''