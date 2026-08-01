# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Empty tree has diameter 0.
        if root is None:
            return 0

        # Returns the height of a subtree.
        def height(root):
            if root is None:
                return 0

            # Height = 1 + taller subtree.
            return 1 + max(height(root.left), height(root.right))

        # Height of left subtree.
        l = height(root.left)

        # Height of right subtree.
        r = height(root.right)

        # Diameter completely inside left subtree.
        dl = self.diameterOfBinaryTree(root.left)

        # Diameter completely inside right subtree.
        dr = self.diameterOfBinaryTree(root.right)

        # Maximum of:
        # 1. Path passing through current node.
        # 2. Left subtree diameter.
        # 3. Right subtree diameter.
        return max(l + r, max(dl, dr))

'''
Algorithm

1. Start DFS from the root.

2. For every node:

   a. Find the height of the left subtree.

   b. Find the height of the right subtree.

3. The longest path passing through
   this node is:

   left height + right height

4. Update the global diameter if this
   path is larger.

5. Return the height of the current node:

   1 + max(left height, right height)

6. After DFS finishes,
   return the maximum diameter found.

Pattern:
DFS + Tree Height

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree

'''