'''
739. Daily Temperatures
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100


'''
'''
1. Create an `answer` array initialized with `0`.
2. Use a **Monotonic Decreasing Stack**.
3. The stack stores **indices**, not temperatures.
4. Traverse each day `i`.
5. While:
   - The stack is not empty, and
   - Current temperature is greater than the temperature at the stack top,
   
   then we found a warmer day.
6. Pop the previous day's index.
7. Calculate:

   `days_waited = i - prev_day`

8. Store it in `answer[prev_day]`.
9. Push the current day's index onto the stack.
10. Any indices left in the stack have no warmer future day, so their answer remains `0`.

'''

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
Complexity
Time Complexity: O(n)
Every index is pushed once and popped at most once.
Space Complexity: O(n)
In the worst case, the stack may contain all indices.
'''