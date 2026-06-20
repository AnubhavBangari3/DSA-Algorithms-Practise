'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
premium lock iconCompanies

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

 

Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length

Algorithm

1. Use Sliding Window.

2. Maintain:
   - left pointer
   - frequency count of characters in current window
   - max_freq = highest frequency of any character in current window

3. Expand window using right pointer.

4. For every s[right]:
   - Increase its frequency
   - Update max_freq

5. Window size = right - left + 1

6. Characters to replace:
   window_size - max_freq

7. If characters to replace > k:
   - window is invalid
   - shrink from left

8. Keep updating answer with maximum valid window size.

9. Return answer.

'''
class Solution:
    def characterReplacement(self, s, k):
        # Frequency of characters in current window
        count = {}
        # Left pointer of sliding window
        left = 0
        # Highest frequency of one character in current window
        max_freq = 0
        # Maximum valid window length
        ans = 0
        # Expand window with right pointer
        for right in range(len(s)):
            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            # Update highest frequency in current window
            max_freq = max(max_freq, count[s[right]])
            # Current window size
            window_size = right - left + 1
            # If replacements needed are more than k,
            # shrink window from left
            if window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
            # Update answer
            ans = max(ans, right - left + 1)
        return ans

'''
Time Complexity:
O(n)

Reason:
Each character is processed at most twice.

Space Complexity:
O(1)

Reason:
Only 26 uppercase English letters are stored.

'''