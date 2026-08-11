'''
125. Valid Palindrome
Solved
Easy
Topics
premium lock iconCompanies

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.




'''
'''
1. Use **Two Pointers**:
   - `left` starts from the beginning.
   - `right` starts from the end.
2. Skip non-alphanumeric characters from both sides.
3. Convert both characters to lowercase and compare them.
4. If they are different, return `False`.
5. If they are the same, move both pointers toward the center.
6. If all characters match, return `True`.
'''

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
Complexity
Time Complexity: O(n)
Each character is visited at most once by the pointers.
Space Complexity: O(1)
No extra string or data structure is created.

'''