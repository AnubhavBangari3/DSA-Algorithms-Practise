'''
22. Generate Parentheses
Solved
Medium
Topics
premium lock iconCompanies

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8


Algorithm

1. Create a result list to store all valid combinations

2. Use a backtracking function with:
   - current string
   - count of opening brackets used
   - count of closing brackets used

3. Base case:
   If length of current string == 2 * n:
       add it to result
       return

4. If opening count < n:
       add '(' and recurse

5. If closing count < opening count:
       add ')' and recurse

6. Return the result list

Complexity

Time Complexity:
O(4^n / sqrt(n))

Reason:
Number of valid combinations is the nth Catalan number

Space Complexity:
O(n) for recursion stack
O(4^n / sqrt(n)) for storing result


'''

class Solution:
    def generateParenthesis(self, n):
        result = []
        
        # Backtracking function
        def backtrack(curr, open_count, close_count):
            # If valid combination is complete
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # Add opening bracket if we still can
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            
            # Add closing bracket only if it remains valid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result