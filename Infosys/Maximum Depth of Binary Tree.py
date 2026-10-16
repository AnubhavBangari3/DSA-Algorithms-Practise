'''
Algorithm: Maximum Depth of Binary Tree (Recursive DFS)

1. Check if root is None:
   - If yes, return 0 (empty tree).
2. Recursively calculate the depth of the left subtree:
   - left_depth = self.maxDepth(root.left).
3. Recursively calculate the depth of the right subtree:
   - right_depth = self.maxDepth(root.right).
4. Find the maximum depth between the left and right subtrees.
5. Add 1 to include the current node:
   - return max(left_depth, right_depth) + 1.
6. Recursion continues until all nodes are processed.
7. Return the maximum depth of the binary tree.

Time Complexity: O(n) - Each node is visited once.
Space Complexity: O(h) - Recursive call stack, where h is the tree height.
Worst Case Space: O(n) - Skewed tree.
Balanced Tree Space: O(log n).

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # If the tree is empty, its depth is 0.
        if root is None:
            return 0

        # Recursively find the maximum depth of the left subtree.
        left_depth = self.maxDepth(root.left)

        # Recursively find the maximum depth of the right subtree.
        right_depth = self.maxDepth(root.right)

        # Current depth is 1 (current node)
        # plus the deeper of the two subtrees.
        return max(left_depth, right_depth) + 1