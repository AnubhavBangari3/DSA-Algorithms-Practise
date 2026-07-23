class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        # Result array initialized with 0
        answer = [0] * n
        # Monotonic decreasing stack
        # Stores indices of temperatures
        stack = []
        # Traverse all days
        for i in range(n):
            # If current temperature is warmer than
            # temperature at stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Previous colder day's index
                prev_day = stack.pop()
                # Number of days waited
                answer[prev_day] = i - prev_day
            # Push current day's index
            stack.append(i)

        return answer

'''
Algorithm

1. Create an answer array filled with 0.

2. Create an empty stack.
   - The stack stores indices of days that are still waiting
     for a warmer temperature.

3. Traverse the temperatures from left to right.

4. While:
   - the stack is not empty, and
   - the current temperature is greater than the temperature
     at the index on the top of the stack:
     
     a. Pop the previous day's index.
     b. Calculate the number of waiting days:
        current_index - previous_index.
     c. Store it in the answer array.

5. Push the current day's index onto the stack.

6. After the traversal, any indices left in the stack
   do not have a warmer future day, so their answers remain 0.

7. Return the answer array.

Pattern:
Monotonic Decreasing Stack

Time Complexity: O(n)

Space Complexity: O(n)

'''