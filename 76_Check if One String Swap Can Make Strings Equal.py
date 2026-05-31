'''
1790. Check if One String Swap Can Make Strings Equal
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

 

Constraints:

    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters.

Algorithm

1. If lengths are different:
   return False

2. Traverse both strings together.

3. Store indices where characters differ.

4. Cases:

   Case 1:
   No differences found
   Strings already equal
   return True

   Case 2:
   Exactly 2 differences found

   Suppose mismatch positions are:
   i and j

   Check:
   s1[i] == s2[j]
   AND
   s1[j] == s2[i]

   If yes:
      one swap can fix it
      return True

5. Otherwise:
   return False

Complexity

Time Complexity:
O(n)

Reason:
Single traversal of strings

Space Complexity:
O(1)

Reason:
At most 2 mismatch positions stored

'''

class Solution:
    def areAlmostEqual(self, s1, s2):

        # Store mismatch positions
        diff = []

        # Find mismatching indices
        for i in range(len(s1)):

            if s1[i] != s2[i]:

                diff.append(i)

                # More than 2 mismatches means impossible
                if len(diff) > 2:
                    return False

        # Strings already equal
        if len(diff) == 0:
            return True

        # Exactly one mismatch cannot be fixed with one swap
        if len(diff) != 2:
            return False

        # Extract mismatch indices
        i, j = diff

        # Check if swapping fixes strings
        return (
            s1[i] == s2[j]
            and
            s1[j] == s2[i]
        )