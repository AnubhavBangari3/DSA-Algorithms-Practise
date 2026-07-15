class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # l -> next position to place 0
        l = 0
        # r -> next position to place 2
        r = len(nums) - 1
        # i -> current element being processed
        i = 0
        # Helper function to swap two elements
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        # Process elements until i crosses r
        while i <= r:
            # If current element is 0,
            # move it to the left partition.
            if nums[i] == 0:
                swap(l, i)
                l += 1
            # If current element is 2,
            # move it to the right partition.
            # Do not move i yet because the swapped
            # element must also be processed.
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            # Move to the next element.
            i += 1
'''
Algorithm

1. Initialize three pointers:
   - left points to the next position for 0.
   - right points to the next position for 2.
   - current scans the array.

2. Traverse the array while current <= right.

3. If the current element is 0:
   - Swap it with the element at left.
   - Increment left.
   - Increment current.

4. If the current element is 2:
   - Swap it with the element at right.
   - Decrement right.
   - Do not move current yet because the swapped element must be processed.

5. If the current element is 1:
   - Simply move current forward.

6. Continue until all elements have been processed.

Pattern:
Three Pointers (Dutch National Flag)

Time Complexity: O(n)
Space Complexity: O(1)

'''