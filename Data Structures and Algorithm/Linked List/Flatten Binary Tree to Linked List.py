# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Stores the nodes in preorder traversal.
        self.preorder_nodes = []
        # Perform preorder traversal.
        def preorder(node):
            # Base case.
            if not node:
                return
            # Visit the current node.
            self.preorder_nodes.append(node)
            # Traverse left subtree.
            preorder(node.left)
            # Traverse right subtree.
            preorder(node.right)

        # Build the preorder sequence.
        preorder(root)

        # Remove the first node because it is already the root.
        if self.preorder_nodes:
            self.preorder_nodes.pop(0)
        # Connect every node to the next preorder node.
        while self.preorder_nodes:
            # Right pointer becomes the next preorder node.
            root.right = self.preorder_nodes.pop(0)
            # Left pointer must always be None.
            root.left = None
            # Move to the next node.
            root = root.right

        # Ensure the last node also has no left child.
        if root:
            root.left = None

'''
Algorithm

1. Perform a preorder traversal of the tree.

2. Store every visited node in a list.

3. Remove the first node from the list because it is already the root.

4. Traverse the remaining nodes.

5. For each node:
   - Connect it as the right child.
   - Set the left child to NULL.
   - Move to the next node.

6. Return after the tree has been flattened.

Pattern:
Tree Traversal (Preorder)

Time Complexity:
O(n²)

Space Complexity:
O(n)

'''