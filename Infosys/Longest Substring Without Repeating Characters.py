'''
Algorithm: Longest Substring Without Repeating Characters (Sliding Window)

1. Initialize an empty set 'seen' to store unique characters.
2. Initialize left = 0 and ans = 0.
3. Iterate through the string using the right pointer.
4. While s[right] exists in seen:
   - Remove s[left] from seen.
   - Increment left to shrink the window.
5. Add s[right] to seen.
6. Update ans = max(ans, right - left + 1).
7. Return ans as the length of the longest substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(min(n, k)), where k is the character set size.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        ans=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            ans=max(ans,right-left+1)
        return ans


