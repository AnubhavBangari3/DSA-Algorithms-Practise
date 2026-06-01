"""
3. Longest Substring Without Repeating Characters

Problem:

Given a string s, find the length of the longest substring
without duplicate characters.

Examples:

Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3

Constraints:
- 0 <= s.length <= 5 * 10^4
- Contains letters, digits, symbols and spaces
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: Sliding Window + Set
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Create:
      seen set
      left pointer = 0
      ans = 0

2. Expand window using right pointer

3. If duplicate exists:
      Remove characters from left side
      until duplicate disappears

4. Add current character to set

5. Calculate current window size:
      right - left + 1

6. Update maximum answer

7. Return answer
"""

class Solution:
    def lengthOfLongestSubstring(self, s):

        # Stores unique characters in current window
        seen = set()

        # Left pointer of sliding window
        left = 0

        # Stores maximum substring length
        ans = 0

        # Expand window
        for right in range(len(s)):

            # Duplicate found
            while s[right] in seen:

                # Remove left character
                seen.remove(s[left])

                # Shrink window
                left += 1

            # Add new character
            seen.add(s[right])

            # Update answer
            ans = max(ans, right - left + 1)

        return ans


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Each character enters set once
- Each character removed once
- Both pointers move only forward

Space Complexity: O(k)

Explanation:
- Set stores unique characters
- k = unique characters count
"""