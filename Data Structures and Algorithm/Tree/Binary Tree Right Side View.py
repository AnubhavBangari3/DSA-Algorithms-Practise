class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Stores the rightmost node
        # at every level.
        result = []

        self.dfs(root, 0, result)

        return result

    def dfs(self, node, level, result):

        # Reached beyond a leaf.
        if node is None:
            return

        # The first node visited at each level
        # is the rightmost node because
        # we always visit the right subtree first.
        if level == len(result):
            result.append(node.val)

        # Visit the right subtree first.
        self.dfs(node.right, level + 1, result)

        # Then visit the left subtree.
        self.dfs(node.left, level + 1, result)

'''
Algorithm

1. Create an empty result list.

2. Perform DFS starting from the root.

3. At each node:

   a. If this is the first node
      visited at this level:
      - Store its value.

   b. Visit the right subtree.

   c. Visit the left subtree.

4. Return the result.

Pattern:
Tree DFS (Preorder)

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree
'''