'''
567. Permutation in String
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given two strings s1 and s2, return true if s2 contains a of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

 

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.

Algorithm

1. If len(s1) > len(s2):
   return False

2. Create frequency arrays of size 26:
   - count1 for s1
   - count2 for current window in s2

3. Fill count1 using s1.

4. Fill count2 using first window of size len(s1).

5. Compare count1 and count2:
   If equal → permutation found.

6. Slide window through s2:
   - Add new character on right
   - Remove old character on left

7. After every slide:
   Compare frequency arrays.

8. If equal:
   return True

9. Return False

'''
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
Time Complexity:
O(n)

Reason:
We slide window once through s2.

Space Complexity:
O(1)

Reason:
Two arrays of size 26.
'''