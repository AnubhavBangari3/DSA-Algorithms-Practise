'''
226. Invert Binary Tree
Solved
Easy
Topics
premium lock iconCompanies

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

1. Use **DFS with recursion**.
2. If the current node exists:
   - Swap its `left` and `right` children.
3. Recursively invert the new left subtree.
4. Recursively invert the new right subtree.
5. Continue until all nodes are processed.
6. Return the root.
'''

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
Complexity
Time Complexity: O(n)
Every node is visited exactly once.
Space Complexity: O(h)
Recursion stack depends on tree height.
Balanced tree: O(log n)
Skewed tree: O(n)
'''