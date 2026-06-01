"""
125. Valid Palindrome

Problem:
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward.

Return True if string is palindrome, otherwise False.

Examples:

Input: s = "A man, a plan, a canal: Panama"
Output: True

Input: s = "race a car"
Output: False

Input: s = " "
Output: True

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: Two Pointers
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Initialize two pointers:
      left = 0
      right = len(s) - 1

2. Traverse while left < right

3. Skip non-alphanumeric characters:
      - Move left pointer forward
      - Move right pointer backward

4. Convert characters to lowercase and compare:
      - If mismatch → return False

5. Move both pointers inward

6. If loop completes → return True
"""

class Solution:
    def isPalindrome(self, s):

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

            left += 1
            right -= 1

        return True


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Each character is visited at most once
- Two pointers traverse entire string

Space Complexity: O(1)

Explanation:
- No extra data structure used
- Only pointers are maintained
"""