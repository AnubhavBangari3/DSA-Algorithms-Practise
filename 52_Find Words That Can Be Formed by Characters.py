'''
1160. Find Words That Can Be Formed by Characters
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

 

Constraints:

    1 <= words.length <= 1000
    1 <= words[i].length, chars.length <= 100
    words[i] and chars consist of lowercase English letters.

Algorithm

1. Count frequency of each character in chars.

2. Initialize total_length = 0.

3. For each word in words:
   a. Count frequency of each character in word.
   b. Check if every character in word is available enough times in chars.
   c. If yes, add len(word) to total_length.

4. Return total_length.

Complexity
Time Complexity:
O(C + W * K)

Where:
C = length of chars
W = number of words
K = average length of each word

Space Complexity:
O(1)

Reason:
Only 26 lowercase letter counts are used.



'''
class Solution:
    def countCharacters(self, words, chars):
        # Count available characters
        char_count = {}
        for ch in chars:
            char_count[ch] = char_count.get(ch, 0) + 1
        total_length = 0
        # Check every word
        for word in words:
            word_count = {}
            # Count characters in current word
            for ch in word:
                word_count[ch] = word_count.get(ch, 0) + 1
            can_form = True
            # Check if word can be formed from chars
            for ch in word_count:
                if word_count[ch] > char_count.get(ch, 0):
                    can_form = False
                    break
            # If good word, add its length
            if can_form:
                total_length += len(word)

        return total_length