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
    
'''
Algorithm

1. If the current node is None:
   - Return 0.

2. Recursively calculate the maximum depth of the left subtree.

3. Recursively calculate the maximum depth of the right subtree.

4. Take the larger depth between the left and right subtree.

5. Add 1 for the current node.

6. Return the result.

Pattern:
Depth-First Search (DFS) + Recursion

Time Complexity: O(n)

Space Complexity: O(h)

where:
n = number of nodes
h = height of the tree
'''