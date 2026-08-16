'''
102. Binary Tree Level Order Traversal
Solved
Medium
Topics
premium lock iconCompanies
Hint

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000


    
1. Use **BFS (Breadth-First Search)** with a queue.
2. If the tree is empty, return `[]`.
3. Add the root node to the queue.
4. While the queue is not empty:
   - Get the number of nodes currently in the queue using `level_size`.
   - These nodes belong to the current level.
5. Process exactly `level_size` nodes:
   - Remove a node from the front of the queue.
   - Add its value to `current_level`.
   - Add its left and right children to the queue.
6. After processing the complete level, add `current_level` to `result`.
7. Return `result`.
'''

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty,
        # return an empty list.
        if root is None:
            return []
        # Queue for BFS traversal.
        queue = deque([root])
        # Stores the final level order traversal.
        result = []
        # Process nodes level by level.
        while queue:
            # Stores values of the current level.
            current_level = []
            # Number of nodes at the current level.
            level_size = len(queue)
            # Process exactly one level.
            for _ in range(level_size):
                # Remove the front node.
                node = queue.popleft()
                current_level.append(node.val)
                # Add the left child.
                if node.left:
                    queue.append(node.left)
                # Add the right child.
                if node.right:
                    queue.append(node.right)

            # Store the completed level.
            result.append(current_level)

        return result

'''

Complexity
Time Complexity: O(n)
Every node is visited exactly once.
Space Complexity: O(n)
The queue may contain up to an entire level of the tree.
'''