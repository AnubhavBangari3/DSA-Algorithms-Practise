'''
1046. Last Stone Weight
Solved
Easy
Topics
premium lock iconCompanies
Hint

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:

Input: stones = [1]
Output: 1

 

Constraints:

    1 <= stones.length <= 30
    1 <= stones[i] <= 100

Algorithm

1. Use a Max Heap to always get the two largest stones

2. Convert array into max heap
   (In Python, use negative values with min heap)

3. While heap has more than 1 element:
   - Pop two largest stones: y and x

   - If y != x:
         push (y - x) back into heap

   - If y == x:
         both destroyed → do nothing

4. If heap is empty:
       return 0
   Else:
       return remaining element

Complexity

Time Complexity:
O(n log n)

Reason:
- Heapify → O(n)
- Each operation → O(log n)
- We perform at most n operations

Space Complexity:
O(n)

Reason:
Heap stores elements
'''

import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max heap by pushing negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Process until at most one stone remains
        while len(max_heap) > 1:
            # Get two largest stones
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            
            # If they are not equal, push the difference
            if y != x:
                heapq.heappush(max_heap, -(y - x))
        
        # Return result
        return -max_heap[0] if max_heap else 0