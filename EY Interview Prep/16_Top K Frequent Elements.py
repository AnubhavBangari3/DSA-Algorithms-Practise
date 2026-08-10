'''
347. Top K Frequent Elements
Solved
Medium
Topics
premium lock iconCompanies

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



'''

'''
1. Count the frequency of each number using a dictionary.
2. Create buckets where:
   - Index = frequency
   - Value = numbers having that frequency.
3. Traverse the buckets from highest frequency to lowest.
4. Add numbers to the result until we get `k` elements.
5. Return the result.

'''

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
Complexity
Time Complexity: O(n)
Counting frequencies takes O(n).
Building and traversing buckets also takes O(n).
Space Complexity: O(n)
Frequency dictionary and buckets may store up to n elements.

'''