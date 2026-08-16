'''
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [0, 104].
    -100 <= Node.val <= 100


'''
'''
1. Use **DFS with recursion**.
2. If `root` is `None`, return `0`.
3. Recursively calculate the depth of the left subtree.
4. Recursively calculate the depth of the right subtree.
5. Take the maximum of the two depths.
6. Add `1` for the current node.
7. Return the result.
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

'''
Complexity
Time Complexity: O(n)
Every node is visited exactly once.
Space Complexity: O(h)
Recursion stack depends on the height h of the tree.
Balanced tree: O(log n)
Skewed tree: O(n)
'''