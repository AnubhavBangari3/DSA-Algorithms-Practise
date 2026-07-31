class Solution:

    def isSameTree(self, root1, root2):

        # Both trees ended together.
        if root1 is None and root2 is None:
            return True

        # Only one tree ended.
        if root1 is None or root2 is None:
            return False

        # Different values mean different trees.
        if root1.val != root2.val:
            return False

        # Both left and right subtrees must match.
        return (
            self.isSameTree(root1.left, root2.left)
            and self.isSameTree(root1.right, root2.right)
        )

    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        # No more nodes available to match.
        if root is None:
            return False

        # Check whether both trees match
        # starting from the current node.
        if self.isSameTree(root, subRoot):
            return True

        # Otherwise, search in the left
        # and right subtrees.
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

'''
Algorithm

1. Create a helper function
   to check whether two trees are identical.

2. In the helper function:

   a. If both nodes are None:
      - Return True.

   b. If only one node is None:
      - Return False.

   c. If their values are different:
      - Return False.

   d. Recursively compare:
      - Left subtree with left subtree.
      - Right subtree with right subtree.

3. For every node in the main tree:

   a. Check whether the tree starting
      from that node matches subRoot.

   b. If it matches:
      - Return True.

   c. Otherwise, search in the left
      and right subtrees.

4. If no matching subtree is found:
   - Return False.

Pattern:
Tree DFS + Same Tree

Time Complexity:
O(n × m)

Space Complexity:
O(h1 + h2)

Where:
n = number of nodes in root
m = number of nodes in subRoot
h1 and h2 = tree heights

'''