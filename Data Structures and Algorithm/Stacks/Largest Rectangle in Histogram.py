class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores (start_index, height) in increasing height order
        max_area = 0

        for index, height in enumerate(heights):
            start = index

            # Current bar is smaller, so taller bars cannot extend further
            while stack and stack[-1][1] > height:
                prev_index, prev_height = stack.pop()
                width = index - prev_index
                max_area = max(max_area, prev_height * width)
                start = prev_index

            stack.append((start, height))

        # Remaining bars can extend until the end of the histogram
        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area

'''
1. Create an empty monotonic increasing stack.
2. Store pairs:
   (starting index, bar height)
3. Traverse every bar.
4. For each bar:
   - Assume its starting index is the current index.
   - While the stack top is taller than the current bar:
     a. Pop the taller bar.
     b. Calculate its width:
        current index - its starting index.
     c. Calculate its rectangle area.
     d. Update the maximum area.
     e. Move the current bar's starting index backward
        to the popped bar's starting index.

5. Push the current bar with its earliest possible starting index.
6. After traversal, bars left in the stack can extend
   until the end of the histogram.
7. Calculate their areas and return the maximum.

Pattern:
Monotonic Increasing Stack

Time Complexity:
O(n)

Space Complexity:
O(n)

'''