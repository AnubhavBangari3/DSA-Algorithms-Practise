'''
1346. Check If N and Its Double Exist
Solved
Easy
Topics
premium lock iconCompanies
Hint

Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

 

Constraints:

    2 <= arr.length <= 500
    -103 <= arr[i] <= 103

Algorithm

1. Create an empty set.

2. Traverse each number num in array:

   - Check if:
       2 * num exists in set
       OR
       num is even and num / 2 exists in set

   - If yes:
       return True

   - Otherwise:
       add num to set

3. If traversal finishes:
   return False

Complexity
Time Complexity:
O(n)

Reason:
Set lookup takes O(1) average time.

Space Complexity:
O(n)

Reason:
Set stores elements.


'''

class Solution:
    def checkIfExist(self, arr):
        # Store previously seen numbers
        seen = set()

        # Traverse array
        for num in arr:

            # Check if double exists
            if 2 * num in seen:
                return True

            # Check if half exists
            # num must be even to have integer half
            if num % 2 == 0 and num // 2 in seen:
                return True

            # Add current number to set
            seen.add(num)

        return False