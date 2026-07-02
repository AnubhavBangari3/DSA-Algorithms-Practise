'''
395. Longest Substring with At Least K Repeating Characters
Solved
Medium
Topics
premium lock iconCompanies

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

if no such substring exists, return 0.

 

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

 

Constraints:

    1 <= s.length <= 104
    s consists of only lowercase English letters.
    1 <= k <= 105

Algorithm (Divide & Conquer)

1. Count frequency of chars in current substring
2. Find any char whose frequency < k
3. If no such char:
      whole substring is valid → return length
4. Else:
      split the substring on that bad char
      recursively solve each part
5. Return maximum of all parts

Time Complexity
Worst case:
O(n^2)
Because each recursive call may count frequencies again.
But in practice, often faster due to splitting.

Space Complexity
O(n)
Due to recursion and substring splits.
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in freq:
            if freq[ch] < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))
        
        return len(s)
    
