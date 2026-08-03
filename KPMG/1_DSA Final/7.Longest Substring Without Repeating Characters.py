class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Stores characters currently inside the sliding window
        seen = set()
        # Left pointer of the sliding window
        left = 0
        # Stores the maximum length found so far
        ans = 0
        # Expand the window using the right pointer
        for right in range(len(s)):
            # If current character is already present,
            # shrink the window until it becomes unique
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add current character to the window
            seen.add(s[right])

            # Update the maximum window size
            ans = max(ans, right - left + 1)
        # Return the length of the longest substring
        return ans

'''
1. Create an empty set to store the characters in the current window.

2. Initialize:
   - left = 0 (start of window)
   - ans = 0 (maximum length found)

3. Traverse the string using the right pointer.

4. If the current character already exists in the set:
   - Remove characters from the left side.
   - Move the left pointer forward.
   - Repeat until the duplicate is removed.

5. Add the current character to the set.

6. Update the maximum length:
   ans = max(ans, right - left + 1)

7. After traversing the entire string, return ans.

Time Complexity: O(n)
- Each character is added to and removed from the set at most once.

Space Complexity: O(min(n, m))
- m = number of unique characters.
- In the worst case, the set stores all unique characters in the current window.
'''