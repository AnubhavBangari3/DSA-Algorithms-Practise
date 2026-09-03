'''
1. Use **Dynamic Programming**.
2. Create `jumps` where:

   `jumps[i]` = minimum jumps required to reach index `i`.

3. Set:
   - `jumps[0] = 0`
   - Other positions initially = infinity.
4. For every index `i`, check previous indices `j`.
5. If index `j` can reach `i`:

   `j + nums[j] >= i`

6. Then:

   `jumps[i] = jumps[j] + 1`

7. Return `jumps[n - 1]`.

Complexity
Time Complexity: O(n²)
Space Complexity: O(n)
'''

class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)

        # Already at the last index
        if n <= 1:
            return 0

        # jumps[i] = minimum jumps needed
        # to reach index i
        jumps = [float("inf")] * n

        jumps[0] = 0

        # Find minimum jumps for every index
        for i in range(1, n):

            # Check previous positions
            for j in range(i):

                # Can index j reach index i?
                if j + nums[j] >= i:

                    jumps[i] = jumps[j] + 1
                    break

        return jumps[n - 1]