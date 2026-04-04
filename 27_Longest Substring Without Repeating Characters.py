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

1. left = 0
2. seen = empty set
3. for right in range(len(s)):
      while s[right] in seen:
          remove s[left] from seen
          left += 1
      add s[right] to seen
      update answer = max(answer, right-left+1)
4. return answer

Time Complexity
O(n)

Why?

right moves forward once
left also moves forward once

So total = linear.

Space Complexity
O(min(n, charset))

In worst case, set stores unique chars in current window.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=ans=0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            ans=max(ans,right-left+1)
        return ans
        