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

'''
Algorithm

1. Create an empty list to store the answer.
2. Start with an empty string.
3. At each step:

   a. If we can still use '(':
      - Add '('.
      - Continue recursively.

   b. If the number of ')' used is less than
      the number of '(' used:
      - Add ')'.
      - Continue recursively.

4. When the string length becomes 2 × n:
   - Store the current string.
5. Return all stored combinations.

Pattern:
Backtracking

Time Complexity: O(4ⁿ / √n)   (Catalan Number)

Space Complexity: O(n)

'''