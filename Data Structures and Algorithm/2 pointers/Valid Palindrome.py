class Solution:
    def isPalindrome(self, s):
        # Two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False
            # Move both pointers
            left += 1
            right -= 1
        return True
    
'''
Algorithm

1. Initialize two pointers:
   - left at the beginning of the string.
   - right at the end of the string.

2. Traverse while left is less than right.

3. Move the left pointer forward until it points to an alphanumeric character.

4. Move the right pointer backward until it points to an alphanumeric character.

5. Compare the lowercase versions of the characters at both pointers.
   - If they are different, return False.

6. If they match, move both pointers towards the center.

7. Continue until the pointers meet or cross.

8. If all valid character pairs match, return True.

Pattern:
Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

'''