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
Algorithm

1. Count the frequency of each number using a hash map.
2. Create buckets where the index represents frequency.
   - bucket[1] stores numbers appearing 1 time.
   - bucket[2] stores numbers appearing 2 times.
   - and so on.
3. Put each number into the bucket matching its frequency.
4. Traverse the buckets from highest frequency to lowest frequency.
5. Add numbers from the buckets into the result list.
6. Once the result contains k elements, return it.

Pattern:
Hash Map + Bucket Sort

'''