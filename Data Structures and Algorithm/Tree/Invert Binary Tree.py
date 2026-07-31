class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # If the current node exists,
        # swap its left and right children.
        if root:
            root.left, root.right = root.right, root.left

            # Recursively invert the left subtree.
            self.invertTree(root.left)

            # Recursively invert the right subtree.
            self.invertTree(root.right)

        # Return the root of the inverted tree.
        return root
'''
Algorithm

1. If the current node is None:
   - Return None.

2. Swap the left and right children.

3. Recursively invert
   the left subtree.

4. Recursively invert
   the right subtree.

5. Return the current root.

Pattern:
Tree DFS (Recursion)

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree

'''