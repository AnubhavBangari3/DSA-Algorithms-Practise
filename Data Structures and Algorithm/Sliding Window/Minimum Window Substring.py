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
    Algorithm

1. If t is longer than s, return an empty string.

2. Count the frequency of characters required from t.

3. Track:
   - window character counts
   - required = number of unique characters needed
   - formed = number of unique characters currently satisfied
   - left pointer
   - best minimum window found so far

4. Expand the window using the right pointer.

5. Add the current character into the window count.

6. If this character is required and its count matches the required count,
   increase formed.

7. When formed == required, the current window contains all characters of t.

8. While the window is valid:
   - Update the best answer if the current window is smaller.
   - Remove the left character from the window.
   - If removing it makes the window invalid, decrease formed.
   - Move left forward.

9. After processing all characters:
   - If no valid window was found, return "".
   - Otherwise, return the smallest valid substring.

Pattern:
Variable Size Sliding Window + Frequency Count

Time Complexity: O(m + n)
Space Complexity: O(m + n)
    '''