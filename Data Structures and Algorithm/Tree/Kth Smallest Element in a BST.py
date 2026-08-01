# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Stores BST values in sorted order.
        arr = []

        # Perform inorder traversal.
        self.inorder(root, arr)

        # kth smallest is at index k-1.
        return arr[k - 1]

    def inorder(self, root, arr):

        # Empty subtree.
        if not root:
            return

        # Visit left subtree.
        self.inorder(root.left, arr)

        # Visit current node.
        arr.append(root.val)

        # Visit right subtree.
        self.inorder(root.right, arr)

'''
Algorithm

1. Perform an inorder traversal.

2. Visit nodes in this order:
   Left → Root → Right

3. Since it is a BST,
   inorder traversal visits nodes
   in sorted order.

4. Store every value in an array.

5. Return the element at index (k-1).

Pattern:
BST + Inorder Traversal

Time Complexity:
O(n)

Space Complexity:
O(n)

Where:
n = number of nodes
'''