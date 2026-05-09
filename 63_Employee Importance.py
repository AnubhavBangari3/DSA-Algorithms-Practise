'''

690. Employee Importance
Solved
Medium
Topics
premium lock iconCompanies

You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

    employees[i].id is the ID of the ith employee.
    employees[i].importance is the importance value of the ith employee.
    employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.

Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

 

Example 1:

Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

Example 2:

Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3
Explanation: Employee 5 has an importance value of -3 and has no direct subordinates.
Thus, the total importance value of employee 5 is -3.

 

Constraints:

    1 <= employees.length <= 2000
    1 <= employees[i].id <= 2000
    All employees[i].id are unique.
    -100 <= employees[i].importance <= 100
    One employee has at most one direct leader and may have several subordinates.
    The IDs in employees[i].subordinates are valid IDs.

    
Algorithm

1. Create a hashmap:
   employee_id → employee object

2. Define DFS function:
   dfs(employee_id)

3. In DFS:
   - Get employee using employee_id
   - Start total with employee.importance
   - For every subordinate_id:
       total += dfs(subordinate_id)

4. Return total

5. Call dfs(id)


Complexity

Time Complexity:
O(n)

Reason:
Each employee is visited once

Space Complexity:
O(n)

Reason:
Hashmap stores all employees
Recursion stack can go up to O(n)

'''

"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):
        # Map employee id to employee object for O(1) access
        emp_map = {}

        for employee in employees:
            emp_map[employee.id] = employee

        # DFS to calculate total importance
        def dfs(emp_id):
            # Get current employee
            employee = emp_map[emp_id]

            # Start with current employee's importance
            total = employee.importance

            # Add importance of all direct and indirect subordinates
            for sub_id in employee.subordinates:
                total += dfs(sub_id)

            return total

        return dfs(id)