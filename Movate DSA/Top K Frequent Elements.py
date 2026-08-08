from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Count frequency of each number
        freq = Counter(nums)

        # bucket[i] stores numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]

        # Put each number into its frequency bucket
        for num, count in freq.items():
            bucket[count].append(num)

        result = []

        # Traverse from highest frequency to lowest
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                result.append(num)

                # Once we get k elements, return answer
                if len(result) == k:
                    return result

'''
1. Count the frequency of every number using `Counter`.
2. Create buckets where the index represents the frequency.
3. Put each number into its corresponding frequency bucket.
4. Traverse the buckets from highest frequency to lowest.
5. Add numbers to the result.
6. Once `k` elements are collected, return the result.

- **Time:** O(n)
- **Space:** O(n)
'''