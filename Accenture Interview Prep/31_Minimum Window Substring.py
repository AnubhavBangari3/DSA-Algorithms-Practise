'''
76. Minimum Window Substring
Solved
Hard
Topics
premium lock iconCompanies
Hint

Given two strings s and t of lengths m and n respectively, return the minimum window of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

 

Follow up: Could you find an algorithm that runs in O(m + n) time?


Algorithm

1. Count frequency of every character in t.
   This tells what characters are required.
2. Use Sliding Window on s.
3. Maintain:
   left pointer
   right pointer
   window_count hashmap
   formed = number of required characters satisfied
   required = number of unique characters in t
4. Expand window using right pointer.
5. For every character s[right]:
   - Add it to window_count
   - If its count matches required count,
     increase formed
6. When formed == required:
   Current window contains all characters of t.
7. Now shrink from left to minimize window:
   - Update answer if current window is smaller
   - Remove s[left] from window_count
   - If removing breaks required frequency,
     decrease formed
   - Move left forward

8. Continue until right reaches end.
9. Return minimum window substring.

'''

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s, t):
        # If t is longer than s, impossible
        if len(t) > len(s):
            return ""
        # Count required characters from t
        need = Counter(t)
        # Number of unique characters we need to satisfy
        required = len(need)
        # Current window character count
        window = defaultdict(int)
        # formed tells how many required characters
        # currently satisfy their required frequency
        formed = 0
        # Sliding window left pointer
        left = 0
        # Store best answer:
        # length, start_index, end_index
        best_len = float("inf")
        best_start = 0
        best_end = 0

        # Expand window using right pointer
        for right in range(len(s)):

            # Add current character to window
            ch = s[right]
            window[ch] += 1

            # If current character is required
            # and its frequency matches exactly
            if ch in need and window[ch] == need[ch]:
                formed += 1
            # When all required characters are satisfied,
            # try shrinking the window
            while left <= right and formed == required:
                # Current window length
                window_len = right - left + 1
                # Update best answer if smaller
                if window_len < best_len:
                    best_len = window_len
                    best_start = left
                    best_end = right
                # Remove left character from window
                left_ch = s[left]
                window[left_ch] -= 1
                # If removed character was required
                # and now its count is less than needed,
                # window becomes invalid
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                # Move left pointer forward
                left += 1
        # If no valid window found
        if best_len == float("inf"):
            return ""
        return s[best_start : best_end + 1]

'''
Time Complexity:
O(m + n)

Where:
m = len(s)
n = len(t)

Reason:
We count t once.
Each character in s is added and removed from window at most once.

Space Complexity:
O(m + n)

Reason:
Hashmaps store character frequencies.
For ASCII letters, it can be considered O(1).

'''