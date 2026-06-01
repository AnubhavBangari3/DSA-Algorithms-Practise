"""
242. Valid Anagram

Problem:
Given two strings s and t, return True if t is an anagram of s,
otherwise return False.

An Anagram means:
Both strings contain exactly same characters
with same frequencies.

Examples:

Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- Strings contain lowercase English letters
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: HashMap / Frequency Counting
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. If lengths are different:
      return False

2. Create empty hashmap frequencyCount

3. Traverse first string:
      Increase frequency of each character

4. Traverse second string:
      Decrease frequency of each character

5. If any frequency becomes non-zero:
      return False

6. Otherwise return True
"""

class Solution:
    def isAnagram(self, s, t):

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        frequencyCount = {}

        # Count characters from first string
        for char in s:
            frequencyCount[char] = frequencyCount.get(char, 0) + 1

        # Remove counts using second string
        for char in t:
            frequencyCount[char] = frequencyCount.get(char, 0) - 1

        # Check remaining frequencies
        for value in frequencyCount.values():
            if value != 0:
                return False

        return True


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n)

Explanation:
- Traverse first string once
- Traverse second string once
- Traverse hashmap once

Space Complexity: O(1)

Explanation:
- Only lowercase English letters
- Max 26 characters stored

(Note:
For generic strings / Unicode,
space complexity becomes O(k)
where k = unique characters)
"""