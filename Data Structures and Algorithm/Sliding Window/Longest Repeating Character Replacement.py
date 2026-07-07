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
Algorithm

1. Create a frequency map to store character counts in the current window.

2. Initialize:
   - left pointer = 0
   - max_freq = 0
   - answer = 0

3. Expand the window using the right pointer.

4. For every character at right:
   - Add it to the frequency map.
   - Update max_freq, which stores the highest frequency of any one character in the current window.

5. Check if the current window is valid:
   - window_size = right - left + 1
   - replacements_needed = window_size - max_freq

6. If replacements_needed > k:
   - Shrink the window from the left.
   - Decrease the frequency of s[left].
   - Move left forward.

7. Update the answer with the current valid window size.

8. Return the maximum window length found.

Pattern:
Sliding Window + Frequency Map

Time Complexity: O(n)
Space Complexity: O(1)

'''