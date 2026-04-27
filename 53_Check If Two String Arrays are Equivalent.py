'''

1662. Check If Two String Arrays are Equivalent
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

 

Constraints:

    1 <= word1.length, word2.length <= 103
    1 <= word1[i].length, word2[i].length <= 103
    1 <= sum(word1[i].length), sum(word2[i].length) <= 103
    word1[i] and word2[i] consist of lowercase letters.

Algorithm
Approach 1 (Simple):

1. Join all strings in word1 → form string s1
2. Join all strings in word2 → form string s2
3. Compare s1 and s2
4. Return True if equal, else False

Complexity

Time Complexity:
O(n)

Reason:
We traverse all characters once while joining

Space Complexity:
O(n)

Reason:
New strings are created


'''
class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        # Join all parts of word1
        s1 = "".join(word1)
        
        # Join all parts of word2
        s2 = "".join(word2)
        
        # Compare both strings
        return s1 == s2