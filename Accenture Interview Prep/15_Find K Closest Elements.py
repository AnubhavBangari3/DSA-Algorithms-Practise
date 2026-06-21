'''
658. Find K Closest Elements
Solved
Medium
Topics
premium lock iconCompanies

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104

Algorithm

1. Since arr is sorted, use Binary Search on the starting index.

2. We need to find the best window of size k.

3. Possible starting index of window:
   left = 0
   right = len(arr) - k

4. While left < right:

   mid = (left + right) // 2

5. Compare two boundary elements:
   arr[mid] and arr[mid + k]

6. If x - arr[mid] > arr[mid + k] - x:
      left side is farther
      move window right
      left = mid + 1

   Else:
      right side is farther or equal
      keep/move window left
      right = mid

7. Final window starts at left.

8. Return arr[left : left + k]

'''
class Solution:
    def findClosestElements(self, arr, k, x):
        # Search space for starting index of k-size window
        left = 0
        right = len(arr) - k
        # Binary search for best window start
        while left < right:
            mid = (left + right) // 2
            # Compare distance of left boundary and right boundary
            # Window options:
            # start at mid or start after mid
            if x - arr[mid] > arr[mid + k] - x:
                # arr[mid] is farther from x,
                # so move window to the right
                left = mid + 1
            else:
                # arr[mid + k] is farther or equal,
                # so keep window on left side
                right = mid
        # Return k elements from best starting position
        return arr[left : left + k]
'''
Time Complexity:
O(log(n - k) + k)

Reason:
Binary search finds best window start.
Then slicing takes k elements.

Space Complexity:
O(k)

Reason:
Output list contains k elements.
'''