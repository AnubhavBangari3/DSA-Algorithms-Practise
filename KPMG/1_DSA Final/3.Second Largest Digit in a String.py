class Solution:
    def secondHighest(self, s: str) -> int:
        # String containing all valid digits
        nums = "1234567890"

        # Store all digits found in the string
        digits = []

        # Traverse each character in the string
        for i in range(len(s)):

            # If the character is a digit
            if s[i] in nums:

                # Convert it to integer and store it
                digits.append(int(s[i]))

        # Remove duplicate digits
        digits = set(digits)

        # If at least one digit exists
        if len(digits) > 0:

            # Remove the largest digit
            digits.remove(max(digits))

            # If another digit still exists,
            # it is the second largest
            if len(digits) > 0:
                return max(digits)
            else:
                return -1

        # No digits found
        else:
            return -1

'''
1. Create an empty list to store all digits.

2. Traverse every character in the string.
   - If the character is a digit, convert it to an integer and add it to the list.

3. Convert the list into a set to remove duplicate digits.

4. If no digits exist, return -1.

5. Remove the largest digit from the set.

6. If the set is still non-empty, return its maximum value (the second largest digit).

7. Otherwise, return -1.

Time Complexity: O(n)
- Traverse the string once. Set operations are O(1) on average.

Space Complexity: O(k)
- k is the number of distinct digits (at most 10), so effectively O(1).
'''