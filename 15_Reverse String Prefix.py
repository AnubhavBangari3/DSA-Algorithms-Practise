'''

3794. Reverse String Prefix
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.

 

Example 1:

Input: s = "abcd", k = 2

Output: "bacd"

Explanation:​​​​​​​

The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

Example 2:

Input: s = "xyz", k = 3

Output: "zyx"

Explanation:

The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

Example 3:

Input: s = "hey", k = 1

Output: "hey"

Explanation:

The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".

 

Constraints:

    1 <= s.length <= 100
    s consists of lowercase English letters.
    1 <= k <= s.length


    
Algorithm:

1. Convert the string into a list → s_list (since strings are immutable)

2. Initialize two pointers:
   left = 0
   right = k - 1

3. While left < right:
   - Swap characters at left and right
   - Move left forward → left += 1
   - Move right backward → right -= 1

4. Convert the list back to string using join

5. Return the final string

Complexity:

Time Complexity: O(n)
- Converting string to list → O(n)
- Reversing k elements → O(k)
- Joining back to string → O(n)
- Overall → O(n)

Space Complexity: O(n)
- Extra list is used to store characters

'''

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        li=list(s)
        l,r=0,k-1
        while l < r:
            li[l],li[r]=li[r],li[l]
            l+=1
            r-=1
        return "".join(li)

        