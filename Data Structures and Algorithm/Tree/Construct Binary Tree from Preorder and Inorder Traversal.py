# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # If no nodes are left, return None.
        if not preorder or not inorder:
            return None

        # First element of preorder is always the root.
        rootVal = preorder[0]

        # Find the root position in inorder traversal.
        index = inorder.index(rootVal)

        # Nodes before root belong to left subtree.
        leftInorderArr = inorder[:index]

        # Nodes after root belong to right subtree.
        rightInorderArr = inorder[index + 1:]

        # Left subtree nodes appear immediately after root
        # in preorder traversal.
        leftPreorderArr = preorder[1 : 1 + len(leftInorderArr)]

        # Remaining nodes belong to right subtree.
        rightPreorderArr = preorder[1 + len(leftInorderArr):]

        # Recursively build left subtree.
        left = self.buildTree(leftPreorderArr, leftInorderArr)

        # Recursively build right subtree.
        right = self.buildTree(rightPreorderArr, rightInorderArr)

        # Create and return the current root.
        return TreeNode(rootVal, left, right)

'''
Algorithm

1. The first element of preorder
   is always the root.

2. Find the root in inorder.

3. Elements before the root in inorder
   belong to the left subtree.

4. Elements after the root in inorder
   belong to the right subtree.

5. Split preorder accordingly.

6. Recursively build the left subtree.

7. Recursively build the right subtree.

8. Return the root.

Pattern:
Tree Construction + Divide & Conquer

Time Complexity:
O(n²)

Space Complexity:
O(n)

Where:
n = number of nodes
'''