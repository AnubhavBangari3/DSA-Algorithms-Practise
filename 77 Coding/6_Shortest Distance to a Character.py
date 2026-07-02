'''
821. Shortest Distance to a Character
Solved
Easy
Topics
premium lock iconCompanies

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]

 

Constraints:

    1 <= s.length <= 104
    s[i] and c are lowercase English letters.
    It is guaranteed that c occurs at least once in s.



Algorithm (2-Pass Thinking)
1. Initialize result array with large values

2. Left → Right pass:
   - Track last seen position of 'c'
   - For each index i:
       if s[i] == c:
           lastSeen = i
       answer[i] = i - lastSeen

3. Right → Left pass:
   - Reset lastSeen
   - For each index i:
       if s[i] == c:
           lastSeen = i
       answer[i] = min(answer[i], lastSeen - i)

4. Return answer

Complexity
Time Complexity: O(n)
Reason:
One pass left → right
One pass right → left
Total = 2n → O(n)
Space Complexity: O(n)
Reason:
Output array of size n


'''

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        ans=[0]*n

        #left to right
        pos=float("-inf")
        for i in range(n):
            if s[i] == c:
                pos=i
            ans[i]=i-pos
        
        #right to left
        pos=float("inf")
        for i in range(n-1,-1,-1):
            if s[i] == c:
                pos=i
            ans[i]=min(ans[i],pos-i)
        return ans