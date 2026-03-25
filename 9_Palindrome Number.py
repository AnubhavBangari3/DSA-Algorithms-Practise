'''
9. Palindrome Number
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given an integer x, return true if x is a , and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?

Algorithm

1. If x < 0 → return False
2. If x % 10 == 0 and x != 0 → return False

3. Initialize:
   reversedHalf = 0

4. While x > reversedHalf:
   last digit = x % 10
   reversedHalf = reversedHalf * 10 + last digit
   x = x // 10

5. Check:
   If x == reversedHalf → even length palindrome
   OR
   If x == reversedHalf // 10 → odd length palindrome

6. Return result

Why x == reversedHalf // 10?

For odd length:

121

Step:
x = 1
reversedHalf = 12

Ignore middle digit → reversedHalf // 10 = 1



Complexity

Time Complexity: O(log n)
Reason:
Each iteration removes one digit
Number of digits ≈ log₁₀(n)
Space Complexity: O(1)
Reason:
Only a few variables used

'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Handle Edge Cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        #Reverse Second Half
        reverseHalf=0
        while x > reverseHalf:
            d=x%10
            reverseHalf=reverseHalf*10 + d
            x//=10

        #Check Palindrome
        return x == reverseHalf or x == reverseHalf//10