class Solution:
    def checkInclusion(self, s1, s2):
        # If s1 is longer, impossible
        if len(s1) > len(s2):
            return False
        # Frequency arrays
        count1 = [0] * 26
        count2 = [0] * 26
        # Build frequency for s1
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        window_size = len(s1)
        # Build first window frequency
        for i in range(window_size):
            count2[ord(s2[i]) - ord('a')] += 1
        # Check first window
        if count1 == count2:
            return True
        # Sliding Window
        for right in range(window_size, len(s2)):
            # Add new character
            count2[ord(s2[right]) - ord('a')] += 1
            # Remove old character
            left_char = s2[right - window_size]
            count2[ord(left_char) - ord('a')] -= 1
            # Compare frequencies
            if count1 == count2:
                return True
        return False
'''
Algorithm

1. If s1 is longer than s2, return False.

2. Create two frequency arrays of size 26:
   - one for s1
   - one for the current window in s2

3. Count the frequency of every character in s1.

4. Count the frequency of the first window in s2.
   The window size should be equal to len(s1).

5. If both frequency arrays are equal, return True.

6. Slide the window across s2:
   - Add the new character entering the window.
   - Remove the old character leaving the window.
   - Compare the window frequency with s1 frequency.

7. If any window has the same frequency as s1, return True.

8. If no matching window is found, return False.

Pattern:
Fixed Size Sliding Window + Frequency Count

Time Complexity: O(n)
Space Complexity: O(1)
'''