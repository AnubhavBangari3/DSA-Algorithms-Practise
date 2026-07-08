from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        ans=[]

        for i in range(len(nums)):
            while dq and dq[0] < i-k+1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans  
        
'''
Algorithm

1. Create an empty deque to store indices of useful elements for the current window.
2. Create an empty result array.
3. Traverse the array from left to right.
4. Before processing the current element:
   - Remove indices from the front of the deque that are outside the current window.
5. Remove indices from the back of the deque while their corresponding values are smaller than the current element.
   - These elements can never become the maximum for the current or any future window.
6. Add the current index to the back of the deque.
7. Once the first window of size k is formed:
   - The element at the front of the deque is the maximum element of the current window.
   - Add it to the result.
8. Continue until all windows have been processed.
9. Return the result.

Pattern:
Sliding Window + Monotonic Decreasing Deque

Time Complexity: O(n)
Space Complexity: O(k)

'''