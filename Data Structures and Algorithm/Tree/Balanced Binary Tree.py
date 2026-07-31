class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):

            # An empty tree has height 0.
            if node is None:
                return 0

            # Find the height of the left subtree.
            left_height = height(node.left)

            # If the left subtree is already unbalanced,
            # propagate the failure upward.
            if left_height == -1:
                return -1

            # Find the height of the right subtree.
            right_height = height(node.right)

            # If the right subtree is already unbalanced,
            # propagate the failure upward.
            if right_height == -1:
                return -1

            # If the current node is unbalanced,
            # return -1 as a special marker.
            if abs(left_height - right_height) > 1:
                return -1

            # Otherwise, return the height
            # of the current subtree.
            return 1 + max(left_height, right_height)

        # A balanced tree never returns -1.
        return height(root) != -1

'''

Algorithm

1. Perform a postorder DFS.
2. For every node:
   a. Compute the height
      of the left subtree.

   b. Compute the height
      of the right subtree.
3. If either subtree is unbalanced:
   - Return -1.
4. If the height difference
   is greater than 1:
   - Return -1.
5. Otherwise:
   - Return

     1 + max(left_height, right_height)

6. The tree is balanced
   if the final result is not -1.

Pattern:
Tree DFS (Bottom-Up)

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree
'''