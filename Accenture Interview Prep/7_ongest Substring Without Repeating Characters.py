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

1. Use Sliding Window.

2. Maintain:
   - left pointer = start of window
   - right pointer = end of window
   - seen set = characters currently inside window

3. Move right pointer one by one.

4. If s[right] is already in seen:
   - shrink window from left
   - remove s[left] from seen
   - move left forward
   - continue until s[right] is no longer duplicate

5. Add s[right] into seen.

6. Update answer:
   ans = max(ans, right - left + 1)

7. Return ans.

'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        # Set to store unique characters in current window
        seen = set()
        # Left pointer of sliding window
        left = 0
        # Maximum length found so far
        ans = 0
        # Right pointer expands the window
        for right in range(len(s)):
            # If duplicate character is found,
            # shrink window from left until duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add current character to window
            seen.add(s[right])
            # Update maximum window length
            ans = max(ans, right - left + 1)
        return ans

'''

Time Complexity:
O(n)

Reason:
Each character is added and removed from set at most once.

Space Complexity:
O(min(n, character_set))

Reason:
Set stores only unique characters in current window.
'''