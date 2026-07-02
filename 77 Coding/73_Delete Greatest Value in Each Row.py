'''
769. Max Chunks To Make Sorted
Solved
Medium
Topics
premium lock iconCompanies
Hint

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

 

Constraints:

    n == arr.length
    1 <= n <= 10
    0 <= arr[i] < n
    All the elements of arr are unique.

Algorithm

1. Initialize:
   max_seen = 0
   chunks = 0

2. Traverse array from left to right.

3. At every index i:
   - Update max_seen = max(max_seen, arr[i])

4. If max_seen == i:
   - It means all numbers from 0 to i are present in this part.
   - So this part can become one valid chunk.
   - Increment chunks.

5. Return chunks.


Complexity

Time Complexity:
O(n)

Reason:
We traverse the array once.

Space Complexity:
O(1)

Reason:
Only variables are used.



'''

class Solution:
    def maxChunksToSorted(self, arr):
        # Stores maximum value seen so far
        max_seen = 0

        # Count of valid chunks
        chunks = 0

        # Traverse array
        for i in range(len(arr)):
            # Update maximum value in current prefix
            max_seen = max(max_seen, arr[i])

            # If max value equals current index,
            # all values from 0 to i are inside this prefix.
            # So this prefix can be sorted as one chunk.
            if max_seen == i:
                chunks += 1

        return chunks