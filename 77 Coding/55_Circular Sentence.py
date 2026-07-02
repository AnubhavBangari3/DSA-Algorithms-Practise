'''
2490. Circular Sentence
Solved
Easy
Topics
premium lock iconCompanies
Hint

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

    For example, "Hello World", "HELLO", "hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

    The last character of each word in the sentence is equal to the first character of its next word.
    The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

 

Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.

 

Constraints:

    1 <= sentence.length <= 500
    sentence consist of only lowercase and uppercase English letters and spaces.
    The words in sentence are separated by a single space.
    There are no leading or trailing spaces.


Algorithm

1. Split the sentence into words using space

2. Let words = list of words

3. Traverse from i = 0 to len(words) - 2:
   - Check if last character of words[i] == first character of words[i+1]
   - If not equal → return False

4. Finally, check circular condition:
   - last character of last word == first character of first word

5. If all conditions satisfied → return True

Complexity

Time Complexity:
O(n)

Reason:
We traverse the sentence once

Space Complexity:
O(n)

Reason:
Split creates list of words


'''
class Solution:
    def isCircularSentence(self, sentence):
        # Split sentence into words
        words = sentence.split()
        
        # Check adjacent words
        for i in range(len(words) - 1):
            # Last char of current word should match first char of next word
            if words[i][-1] != words[i + 1][0]:
                return False
        
        # Check circular condition (last word → first word)
        if words[-1][-1] != words[0][0]:
            return False
        
        return True