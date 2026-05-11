'''
2266. Count Number of Texts
Medium
Topics
premium lock iconCompanies
Hint

Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.

In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

    For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
    Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.

However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

    For example, when Alice sent the message "bob", Bob received the string "2266622".

Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.

Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.

 

Constraints:

    1 <= pressedKeys.length <= 105
    pressedKeys only consists of digits from '2' - '9'.

Algorithm

1. We need to count how many ways pressedKeys can be split into valid letter groups.

2. Same consecutive digits form one group.

3. For digits:
   2, 3, 4, 5, 6, 8
   max group size = 3

   For digits:
   7, 9
   max group size = 4

4. Use DP:
   dp[i] = number of ways to decode pressedKeys[0 : i]

5. Base case:
   dp[0] = 1

6. For every index i from 1 to n:
   Look backward from i:
   - Take same digit group of size 1, 2, 3, or 4
   - Stop if digit changes
   - Stop if group size exceeds allowed limit

   Add:
   dp[i] += dp[i - group_size]

7. Return dp[n] modulo 10^9 + 7

Complexity

Time Complexity:
O(n)

Reason:
For every index, we check at most 4 previous characters.

Space Complexity:
O(n)

Reason:
We use a DP array of size n + 1.
'''

class Solution:
    def countTexts(self, pressedKeys):
        MOD = 10**9 + 7
        n = len(pressedKeys)

        # dp[i] = number of ways to decode pressedKeys[0:i]
        dp = [0] * (n + 1)

        # Empty string has one way
        dp[0] = 1

        for i in range(1, n + 1):
            # Current digit
            digit = pressedKeys[i - 1]

            # Digits 7 and 9 have 4 letters
            # Other digits have 3 letters
            max_press = 4 if digit in "79" else 3

            # Try group size 1 to max_press
            for length in range(1, max_press + 1):

                # Avoid going out of bounds
                if i - length < 0:
                    break

                # All characters in current group must be same digit
                if pressedKeys[i - length] != digit:
                    break

                # Add ways before this group
                dp[i] = (dp[i] + dp[i - length]) % MOD

        return dp[n]