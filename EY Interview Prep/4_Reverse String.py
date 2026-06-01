"""
344. Reverse String

Problem:
Write a function that reverses a string.

The input string is given as an array of characters.

Modify the input array in-place using O(1) extra memory.

Examples:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is printable ASCII character
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

3. Swap characters:
      s[left], s[right] = s[right], s[left]

4. Move pointers inward:
      left += 1
      right -= 1

5. Continue until pointers cross
"""

class Solution:
    def reverseString(self, s):

        left = 0
        right = len(s) - 1

        while left < right:

            # Swap characters
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Traverse half of array
- Each element swapped once

Space Complexity: O(1)

Explanation:
- In-place modification
- No extra data structure used
"""