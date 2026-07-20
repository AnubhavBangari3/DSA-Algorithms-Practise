class Solution:
    def maximumSwap(self, num: int) -> int:

        # Convert the number into a list of digits.
        digits = list(str(num))

        # Stores the maximum digit seen so far while
        # traversing from right to left.
        max_digit = -1

        # Stores the index of the rightmost maximum digit.
        max_digit_index = -1

        # Indices of the two digits to be swapped.
        left_swap = -1
        right_swap = -1

        # Traverse from right to left.
        for i in range(len(digits) - 1, -1, -1):

            # Update the maximum digit found so far.
            if int(digits[i]) > int(max_digit):
                max_digit = digits[i]
                max_digit_index = i

            # If a larger digit exists on the right,
            # remember the current index as a swap candidate.
            elif int(digits[i]) < int(max_digit):
                left_swap = i
                right_swap = max_digit_index

        # The number is already the largest possible.
        if left_swap == -1:
            return num

        # Perform the swap.
        digits[left_swap], digits[right_swap] = (
            digits[right_swap],
            digits[left_swap],
        )

        # Convert the list back to an integer.
        return int("".join(digits))
    
'''
Algorithm

1. Convert the number into a list of digits.
2. Traverse the digits from right to left.
3. Maintain:
   - The largest digit seen so far.
   - The index of its rightmost occurrence.
4. If the current digit is smaller than the maximum digit
   seen on its right:
   - Store the current index as the left swap index.
   - Store the maximum digit's index as the right swap index.
5. Continue the traversal because a more significant digit
   on the left gives a larger number after swapping.
6. If no swap indices were found:
   - Return the original number.
7. Otherwise, swap the two digits.
8. Convert the digits back to an integer and return it.

Pattern:
Greedy

Time Complexity: O(n)

Space Complexity: O(n)

'''