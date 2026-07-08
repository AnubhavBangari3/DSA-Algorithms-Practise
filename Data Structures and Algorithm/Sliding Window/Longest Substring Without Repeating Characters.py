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
    
'''
Algorithm

1. Create an empty set to store the unique characters in the current window.
2. Initialize:
   - left pointer = 0
   - answer = 0
3. Expand the window using the right pointer.
4. For each character:
   - If the character is already present in the set, repeatedly:
     - Remove the character at the left pointer from the set.
     - Move the left pointer forward.
   - Continue until the current character is no longer present in the set.
5. Add the current character to the set.
6. Calculate the current window length and update the maximum length.
7. After traversing the entire string, return the maximum length found.

Pattern:
Sliding Window + Hash Set

Time Complexity: O(n)
Space Complexity: O(min(n, character set size))
'''