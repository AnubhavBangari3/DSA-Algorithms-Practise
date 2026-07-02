'''
2399. Check Distances Between Same Letters
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i]. If the ith letter does not appear in s, then distance[i] can be ignored.

Return true if s is a well-spaced string, otherwise return false.

 

Example 1:

Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true
Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.

Example 2:

Input: s = "aa", distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: false
Explanation:
- 'a' appears at indices 0 and 1 so there are zero letters between them.
Because distance[0] = 1, s is not a well-spaced string.

 

Constraints:

    2 <= s.length <= 52
    s consists only of lowercase English letters.
    Each letter appears in s exactly twice.
    distance.length == 26
    0 <= distance[i] <= 50


    
Algorithm

1. Create a hashmap to store first occurrence index of each character.

2. Traverse the string using index i.

3. For each character:
   - If character is not in hashmap:
       store its index
   - Else:
       calculate letters_between = i - first_index - 1
       find expected distance using distance[ord(ch) - ord('a')]
       if they are not equal:
           return False

4. If traversal completes, return True

Complexity
Time Complexity: O(n)
Reason:
We traverse the string once
Hashmap lookup and insertion are O(1)

So total = O(n)

Space Complexity: O(1)
Reason:
At most 26 lowercase letters can be stored in hashmap
So extra space does not grow with input size in practice

Strictly it is O(26), which is treated as O(1)

'''
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_seen = {}

        for i, ch in enumerate(s):
            if ch not in first_seen:
                first_seen[ch] = i
            else:
                letters_between = i - first_seen[ch] - 1
                if letters_between != distance[ord(ch) - ord('a')]:
                    return False

        return True