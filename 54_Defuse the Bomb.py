'''
1652. Defuse the Bomb
Easy
Topics
premium lock iconCompanies
Hint

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

    If k > 0, replace the ith number with the sum of the next k numbers.
    If k < 0, replace the ith number with the sum of the previous -k numbers.
    If k == 0, replace the ith number with 0.

As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

 

Constraints:

    n == code.length
    1 <= n <= 100
    1 <= code[i] <= 100
    -(n - 1) <= k <= n - 1

Algorithm
1. Let n = length of array

2. If k == 0:
   return array of size n filled with 0

3. Create result array of size n

4. For each index i from 0 to n-1:

   If k > 0:
       sum next k elements:
       for j in range(1 to k):
           index = (i + j) % n
           add code[index]

   If k < 0:
       sum previous -k elements:
       for j in range(1 to -k):
           index = (i - j + n) % n
           add code[index]

5. Store sum in result[i]

6. Return result

Complexity

Time Complexity:
O(n * |k|)

Reason:
For each element, we sum k elements

Space Complexity:
O(n)

Reason:
Result array is used

(i + j) % n → move forward circularly
(i - j + n) % n → move backward circularly
'''
class Solution:
    def decrypt(self, code, k):
        n = len(code)
        
        # If k == 0, return all zeros
        if k == 0:
            return [0] * n
        
        result = [0] * n
        
        # Traverse each index
        for i in range(n):
            total = 0
            
            # If k is positive → sum next k elements
            if k > 0:
                for j in range(1, k + 1):
                    index = (i + j) % n   # circular index
                    total += code[index]
            
            # If k is negative → sum previous -k elements
            else:
                for j in range(1, -k + 1):
                    index = (i - j + n) % n   # circular index
                    total += code[index]
            
            result[i] = total
        
        return result