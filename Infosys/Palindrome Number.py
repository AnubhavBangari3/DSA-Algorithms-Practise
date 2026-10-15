
'''
Algorithm: Palindrome Number (Reverse Half)

1. Check edge cases:
   - If x < 0, return False.
   - If x ends with 0 and x != 0, return False.
2. Initialize reverseHalf = 0.
3. While x > reverseHalf:
   - Extract the last digit: d = x % 10.
   - Update reverseHalf = reverseHalf * 10 + d.
   - Remove the last digit from x using x //= 10.
4. Compare the two halves:
   - For even digits, check x == reverseHalf.
   - For odd digits, check x == reverseHalf // 10.
5. Return True if either condition matches, otherwise False.

Time Complexity: O(log10(n))
Space Complexity: O(1)

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