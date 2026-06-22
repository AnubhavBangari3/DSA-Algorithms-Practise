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

Algorithm

1. Create:
   answer array initialized with 0
   empty stack
2. Stack stores indices of temperatures.
3. Traverse temperatures from left to right.
4. For every current day i:
   While stack is not empty AND

   temperatures[i] > temperatures[stack.top()]:

       previous_day = stack.pop()

       answer[previous_day] = i - previous_day
5. Push current index into stack.
6. Any indices left in stack have no warmer day,
   so their answer remains 0.
7. Return answer.

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
Time Complexity:
O(n)

Reason:
Each index is pushed once and popped once.

Space Complexity:
O(n)

Reason:
Stack may store all indices.

'''