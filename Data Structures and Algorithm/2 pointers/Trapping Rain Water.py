class Solution:
    def trap(self, height: List[int]) -> int:
        # Total water trapped
        res = 0
        # Number of bars
        n = len(height)
        # left[i] = maximum height to the left of index i (including itself)
        left = [0] * n
        # right[i] = maximum height to the right of index i (including itself)
        right = [0] * n
        # Initialize first value
        left[0] = height[0]
        # Fill left max array
        # Each position stores the highest bar seen so far from the left
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        # Initialize last value
        right[n-1] = height[n-1]
        # Fill right max array
        # Each position stores the highest bar seen so far from the right
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        # Calculate trapped water at each index
        for i in range(n):
            # Water level is limited by the smaller boundary
            # Water stored = min(left boundary, right boundary) - current height
            res += min(left[i], right[i]) - height[i]
        return res
'''
Algorithm

1. Create two arrays:
   - left[i] stores the maximum height from index 0 to i.
   - right[i] stores the maximum height from index i to the last index.

2. Fill the left array:
   - Set left[0] = height[0].
   - For every index i, store the maximum of:
     - left[i - 1]
     - height[i]

3. Fill the right array:
   - Set right[n - 1] = height[n - 1].
   - Traverse from right to left.
   - For every index i, store the maximum of:
     - right[i + 1]
     - height[i]

4. Traverse every index of the height array.

5. At each index:
   - The water level is limited by the smaller of the highest left boundary and highest right boundary.
   - Calculate trapped water as:
     min(left[i], right[i]) - height[i]

6. Add the trapped water at every index to the result.

7. Return the total trapped water.

Pattern:
Prefix Maximum + Suffix Maximum

Time Complexity: O(n)
Space Complexity: O(n)
'''