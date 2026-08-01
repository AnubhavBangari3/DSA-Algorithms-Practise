# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Start from the root.
        cur = root

        while cur:

            # If both nodes are greater than current,
            # LCA must be in the right subtree.
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right

            # If both nodes are smaller than current,
            # LCA must be in the left subtree.
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left

            # Otherwise, current node lies between p and q
            # (or equals one of them), so it is the LCA.
            else:
                return cur

'''
Algorithm

1. Start from the root.

2. If both p and q are greater than
   the current node,
   move to the right subtree.

3. If both p and q are smaller than
   the current node,
   move to the left subtree.

4. Otherwise,
   the current node is the Lowest
   Common Ancestor (LCA).

5. Return the current node.

Pattern:
BST Traversal

Time Complexity:
O(h)

Space Complexity:
O(1)

Where:
h = height of the BST

'''