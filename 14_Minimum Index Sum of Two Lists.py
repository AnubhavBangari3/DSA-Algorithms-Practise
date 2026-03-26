'''
599. Minimum Index Sum of Two Lists
Solved
Easy
Topics
premium lock iconCompanies

Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

Example 3:

Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

 

Constraints:

    1 <= list1.length, list2.length <= 1000
    1 <= list1[i].length, list2[i].length <= 30
    list1[i] and list2[i] consist of spaces ' ' and English letters.
    All the strings of list1 are unique.
    All the strings of list2 are unique.
    There is at least a common string between list1 and list2.
Algorithm:

1. Create a hash map to store elements of list1 with their indices
   → {restaurant: index}

2. Initialize:
   min_sum = infinity
   result = []

3. Iterate through list2:
   If the current string exists in the map:
      Compute index_sum = i + j

      If index_sum < min_sum:
         Update min_sum
         Reset result list → [current_string]

      Else if index_sum == min_sum:
         Append current string to result

4. Return result


Complexity
Time Complexity: O(n + m)
Building hashmap → O(n)
Traversing second list → O(m)
Space Complexity: O(n)
For storing hashmap of list1

'''

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Step 1: store list1 indices
        index_map = {}
        for i, word in enumerate(list1):
            index_map[word] = i
        
        min_sum = float('inf')
        result = []
        
        # Step 2: traverse list2
        for j, word in enumerate(list2):
            if word in index_map:
                curr_sum = index_map[word] + j
                
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    result = [word]
                elif curr_sum == min_sum:
                    result.append(word)
        
        return result