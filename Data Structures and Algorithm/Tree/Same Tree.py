class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # If both nodes are empty,
        # this part of the trees matches.
        if p is None and q is None:
            return True

        # If both nodes exist,
        # compare their values and recursively
        # compare their left and right subtrees.
        if p is not None and q is not None:
            return (
                p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )

        # One node exists while the other doesn't,
        # so the trees are different.
        return False

'''
Algorithm

1. If both nodes are None:
   - Return True.

2. If both nodes exist:

   a. Compare their values.

   b. Recursively compare
      their left subtrees.

   c. Recursively compare
      their right subtrees.

   d. Return True only if
      all three conditions are True.

3. If one node is None
   and the other is not:
   - Return False.

Pattern:
Tree DFS (Recursion)

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree

'''