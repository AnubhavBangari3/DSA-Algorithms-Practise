from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Dictionary to store frequency of each element
        freq = defaultdict(int)

        # Count the occurrences
        for num in nums:
            freq[num] += 1

            # Return immediately if count exceeds n/2
            if freq[num] > len(nums) // 2:
                return num

'''
1. Create an empty dictionary to store frequencies.
2. Traverse the array.
3. Increase the count of each element.
4. If the count becomes greater than `n/2`, return that element.
5. Since a majority element always exists, it will definitely be found.

- **Time:** O(n)
- **Space:** O(n)
'''