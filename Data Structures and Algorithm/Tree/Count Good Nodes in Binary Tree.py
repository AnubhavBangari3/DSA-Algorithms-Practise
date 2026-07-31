# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # DFS returns the number of good nodes
        # in the current subtree.
        def dfs(node, max_so_far):

            # No node to process.
            if not node:
                return 0

            # Current node is good if its value
            # is greater than or equal to every
            # value seen from the root.
            if node.val >= max_so_far:
                good = 1
            else:
                good = 0

            # Update the maximum value seen
            # on the current root-to-node path.
            max_so_far = max(max_so_far, node.val)

            # Count current good node +
            # good nodes from left subtree +
            # good nodes from right subtree.
            return (
                good
                + dfs(node.left, max_so_far)
                + dfs(node.right, max_so_far)
            )

        # Start DFS with a value smaller than
        # every possible node value.
        return dfs(root, -int(1e5))

'''
Algorithm

1. Start DFS from the root.

2. Keep track of the maximum value
   seen from the root to the current node.

3. For every node:

   a. If node value is greater than or equal
      to the maximum value seen so far,
      count it as a good node.

   b. Update the maximum value for the path.

4. Recursively process:
   - Left subtree.
   - Right subtree.

5. Return:
   Current good node count +
   Left subtree count +
   Right subtree count.

Pattern:
DFS + Path Information

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree

'''