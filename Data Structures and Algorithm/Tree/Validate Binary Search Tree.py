# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Checks whether every node lies
        # within the allowed range.
        def validate(root, low, high):

            # Empty subtree is always a valid BST.
            if not root:
                return True

            # Current node must lie strictly
            # between low and high.
            if root.val <= low or root.val >= high:
                return False

            # Left subtree:
            # All values must be < current node.
            #
            # Right subtree:
            # All values must be > current node.
            return (
                validate(root.left, low, root.val)
                and
                validate(root.right, root.val, high)
            )

        # Initially every value is allowed.
        return validate(root, -sys.maxsize, sys.maxsize)

'''
Algorithm

1. Start DFS from the root.

2. Every node has an allowed range:
   (low, high)

3. If the current node is outside
   this range,
   return False.

4. Recur for left subtree:
   Range = (low, current value)

5. Recur for right subtree:
   Range = (current value, high)

6. If every node satisfies its range,
   return True.

Pattern:
DFS + Range Validation

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of tree
'''