'''
1. Maintain an array `tails`.
2. `tails[i]` stores the smallest possible ending value of an increasing subsequence of length `i + 1`.
3. For every number:
   - Use Binary Search to find the first position where `tails[index] >= num`.
4. If no such position exists:
   - Append `num`.
   - This increases the LIS length.
5. Otherwise:
   - Replace `tails[index]` with `num`.
   - This keeps a smaller tail and gives better chances to extend later.
6. Return `len(tails)`.

Complexity
Time Complexity: O(n log n)
Space Complexity: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums):

        # tails[i] = smallest possible ending value
        # of an increasing subsequence of length i + 1
        tails = []

        # Traverse every number
        for num in nums:

            # Find first index where tails[index] >= num
            index = bisect.bisect_left(tails, num)

            # num is greater than all current tails
            # so extend the subsequence
            if index == len(tails):
                tails.append(num)

            else:
                # Replace with a smaller tail
                # to improve future possibilities
                tails[index] = num

        # Length of tails = LIS length
        return len(tails)