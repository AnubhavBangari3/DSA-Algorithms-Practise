class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def checkSymmetric(left_node, right_node):

            # If both mirror positions are empty,
            # this part is symmetric.
            if left_node is None and right_node is None:
                return True

            # If both nodes exist, their values must match,
            # and their opposite children must also mirror each other.
            if left_node is not None and right_node is not None:
                return (
                    left_node.val == right_node.val
                    and checkSymmetric(left_node.left, right_node.right)
                    and checkSymmetric(left_node.right, right_node.left)
                )

            # One node exists while the other does not.
            return False

        # Compare the left and right subtrees as mirrors.
        return checkSymmetric(root.left, root.right)

'''
Algorithm — Recursive

1. Compare the left subtree and right subtree.
2. For two mirror nodes:

   a. If both are None:
      - Return True.

   b. If only one is None:
      - Return False.

   c. If their values are different:
      - Return False.
3. Recursively compare:

   - left.left with right.right
   - left.right with right.left
4. Return True only if both comparisons succeed.

Pattern:
Tree DFS + Mirror Recursion

Time Complexity:
O(n)

Space Complexity:
O(h)

'''