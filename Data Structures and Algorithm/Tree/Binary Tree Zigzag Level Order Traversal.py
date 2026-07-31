from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # If the tree is empty,
        # return an empty list.
        if root is None:
            return []

        # Queue for BFS traversal.
        queue = deque([root])

        # Stores the final answer.
        result = []

        # Direction of traversal.
        left_to_right = True

        while queue:

            # Number of nodes in the current level.
            level_size = len(queue)

            # Stores values of the current level.
            current_level = []

            # Process one level.
            for _ in range(level_size):

                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Reverse only when traversing
            # from right to left.
            if not left_to_right:
                current_level.reverse()

            result.append(current_level)

            # Alternate direction.
            left_to_right = not left_to_right

        return result
'''
Algorithm

1. If the tree is empty:
   - Return an empty list.

2. Create a queue
   and insert the root.

3. Maintain a boolean:

   left_to_right = True

4. While the queue is not empty:

   a. Process all nodes
      in the current level.

   b. Store their values.

   c. Add their children
      to the queue.

   d. If left_to_right is False:
      - Reverse the level.

   e. Add the level
      to the answer.

   f. Toggle the direction.

5. Return the final answer.

Pattern:
Tree BFS (Level Order Traversal)

Time Complexity:
O(n)

Space Complexity:
O(n)
'''