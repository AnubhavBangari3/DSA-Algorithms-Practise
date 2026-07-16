class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # If every number is 0, return only one "0".
        if not any(map(bool, nums)):
            return "0"
        # Convert all numbers to strings for concatenation.
        nums = list(map(str, nums))
        # A single number is already the answer.
        if len(nums) < 2:
            return "".join(nums)
        # Return True when x should appear before y.
        # Example: for "3" and "30", compare "330" with "303".
        def compare(x, y):
            return int(nums[x] + nums[y]) > int(nums[y] + nums[x])
        # Arrange every position using the custom comparison rule.
        for i in range(len(nums) - 1):
            j = i + 1
            # Compare nums[i] with every remaining number.
            while j < len(nums):
                # If nums[j] should appear before nums[i], swap them.
                if not compare(i, j):
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
        # Join the arranged strings to form the largest number.
        return "".join(nums)
    
'''
Algorithm
1. Check whether every number in the array is 0.
2. If all numbers are 0, return "0".
3. Convert every integer into a string.
4. Compare two strings x and y using:
   - x + y
   - y + x
5. If x + y is greater than y + x, place x before y.
6. Otherwise, place y before x.
7. Use this comparison to arrange all strings in the required order.
8. Join the arranged strings and return the result.
Pattern:
Custom Sorting + Greedy
Time Complexity: O(n² × d)
Space Complexity: O(n × d)

'''