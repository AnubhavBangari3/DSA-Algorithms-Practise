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
Algorithm

1. If the tree is empty:
   - Return an empty list.

2. Create a queue
   and insert the root.

3. While the queue is not empty:

   a. Find the number of nodes
      in the current level.

   b. Process exactly those nodes.

   c. Store their values.

   d. Insert their children
      into the queue.

4. Append the current level
   to the answer.

5. Return the final result.

Pattern:
Tree BFS (Level Order Traversal)

Time Complexity:
O(n)

Space Complexity:
O(n)

Where:
n = number of nodes
'''