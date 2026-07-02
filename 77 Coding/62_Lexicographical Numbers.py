'''
386. Lexicographical Numbers
Solved
Medium
Topics
premium lock iconCompanies

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]

 

Constraints:

    1 <= n <= 5 * 104

Algorithm

1. Start DFS from numbers 1 to 9

2. In DFS:
   - If current number > n:
       return

   - Add current number to result

   - Try appending digits 0 to 9:
       next_num = current * 10 + digit

   - Recursively call DFS(next_num)

3. This naturally generates numbers
   in lexicographical order.

Lexicographical order behaves like a DFS tree.

Example for n = 13:

1
├── 10
├── 11
├── 12
├── 13
2
3
4
...

So we perform preorder DFS.

Complexity

Time Complexity:
O(n)

Reason:
Every number from 1 to n is visited exactly once

Space Complexity:
O(1) extra space
(excluding recursion stack and output)

Recursion depth is at most O(log n)

'''
class Solution:
    def lexicalOrder(self, n):
        result = []

        # DFS function
        def dfs(curr):
            # Stop if number exceeds n
            if curr > n:
                return

            # Add current number
            result.append(curr)

            # Generate next lexicographical numbers
            for digit in range(10):
                next_num = curr * 10 + digit

                # Skip numbers greater than n
                if next_num > n:
                    return

                dfs(next_num)

        # Start DFS from 1 to 9
        for i in range(1, 10):
            dfs(i)

        return result