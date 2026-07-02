'''
2405. Optimal Partition of String
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

 

Constraints:

    1 <= s.length <= 105
    s consists of only English lowercase letters.



Algorithm

1. Start answer = 1
2. Create an empty set seen
3. Traverse each character ch in s
4. If ch already in seen:
      increment answer
      clear seen
5. Add ch to seen
6. Return answer

Time Complexity
O(n)

We scan the string once.

Space Complexity
O(26) = O(1)
'''
class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1

        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)

        return count