# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Stores the maximum path sum found so far.
        max_sum = [float("-inf")]

        def dfs(root, max_sum):

            # Empty subtree contributes 0.
            if not root:
                return 0

            # Ignore negative paths because they reduce the total sum.
            left = max(dfs(root.left, max_sum), 0)

            # Ignore negative paths because they reduce the total sum.
            right = max(dfs(root.right, max_sum), 0)

            # Current node acts as the highest point of the path.
            current_path = left + right + root.val

            # Update the overall maximum path sum.
            max_sum[0] = max(max_sum[0], current_path)

            # Return the best single path to the parent.
            return root.val + max(left, right)

        # Start DFS from the root.
        dfs(root, max_sum)

        return max_sum[0]

'''
Algorithm

1. Traverse the tree using DFS.

2. Calculate the maximum path sum
   from the left subtree.

3. Calculate the maximum path sum
   from the right subtree.

4. Ignore negative path sums
   by treating them as 0.

5. Calculate the path passing
   through the current node.

   left + root + right

6. Update the global maximum.

7. Return only one side
   (left or right) to the parent.

Pattern:
Tree DFS + Postorder Traversal

Time Complexity:
O(n)

Space Complexity:
O(h)

Where:
n = number of nodes
h = height of the tree
'''