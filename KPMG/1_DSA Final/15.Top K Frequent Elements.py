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
1. Count the frequency of every element using a hash map.

2. Create a bucket array where:
   bucket[i] stores all numbers appearing exactly i times.

3. Place every number into its corresponding bucket.

4. Traverse the buckets from highest frequency to lowest.

5. Collect elements until k elements have been added.

6. Return the result.

Key Idea:
Instead of sorting frequencies (O(n log n)),
group numbers by frequency (Bucket Sort), then scan from highest frequency downward.

Time Complexity: O(n)

Counter creation          → O(n)

Bucket insertion          → O(n)

Bucket traversal          → O(n)

Overall:

O(n)

--------------------------------

Space Complexity: O(n)

Frequency map             → O(n)

Bucket array              → O(n)

Result                    → O(k)

Overall:

O(n)

'''