'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, find the length of the longest without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Algorithm

1. Use Sliding Window approach.

2. Maintain:
   - left pointer → start of window
   - right pointer → expand window
   - set → stores unique characters in current window

3. Move right pointer:

   If current character already exists:
      shrink window from left
      remove characters until duplicate disappears

4. Add current character into set

5. Update maximum length

6. Return answer

Complexity

Time Complexity:
O(n)

Reason:
Each character enters and leaves window at most once.

Space Complexity:
O(min(n, charset))

Reason:
Set stores unique characters.


'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        # Stores unique characters in current window
        seen = set()
        # Left pointer of sliding window
        left = 0
        # Stores maximum substring length
        ans = 0
        # Expand window using right pointer
        for right in range(len(s)):
            # If duplicate found,
            # shrink window until duplicate removed
            while s[right] in seen:
                # Remove left character from set
                seen.remove(s[left])
                # Move left pointer forward
                left += 1
            # Add current character
            seen.add(s[right])
            # Update maximum window size
            ans = max(ans, right - left + 1)

        return ans