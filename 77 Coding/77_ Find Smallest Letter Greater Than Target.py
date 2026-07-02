'''
744. Find Smallest Letter Greater Than Target
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

 

Constraints:

    2 <= letters.length <= 104
    letters[i] is a lowercase English letter.
    letters is sorted in non-decreasing order.
    letters contains at least two different characters.
    target is a lowercase English letter.

Algorithm

1. Use Binary Search.

2. We need:
   smallest character strictly greater than target.

3. Initialize:
   left = 0
   right = len(letters)

4. While left < right:

   mid = (left + right) // 2

   If letters[mid] <= target:
       answer must be on right side
       left = mid + 1

   Else:
       possible answer found
       search left side
       right = mid

5. After loop:

   If left reaches array size:
      wrap around to first character

6. Return:
   letters[left % len(letters)]

Complexity

Time Complexity:
O(log n)

Reason:
Binary search halves search space.

Space Complexity:
O(1)


'''
class Solution:
    def nextGreatestLetter(self, letters, target):

        left = 0
        right = len(letters)

        # Binary Search
        while left < right:

            mid = (left + right) // 2

            # Current letter is not greater
            # so move right
            if letters[mid] <= target:
                left = mid + 1

            else:
                # Potential answer found
                right = mid

        # Use modulo for wrap around case
        return letters[left % len(letters)]