# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        # If node is None, mark it with 'x'.
        if not root:
            return 'x'

        # Store:
        # Root, Left Subtree, Right Subtree
        return (
            root.val,
            self.serialize(root.left),
            self.serialize(root.right)
        )

    def deserialize(self, data):

        # 'x' represents a missing node.
        if data[0] == 'x':
            return None

        # Create the current node.
        node = TreeNode(data[0])

        # Recursively rebuild the left subtree.
        node.left = self.deserialize(data[1])

        # Recursively rebuild the right subtree.
        node.right = self.deserialize(data[2])

        # Return the reconstructed tree.
        return node

'''
Algorithm

Serialization

1. If the node is None,
   store 'x'.

2. Otherwise,
   store the current node value.

3. Serialize the left subtree.

4. Serialize the right subtree.

5. Return the complete structure.

-----------------------------------

Deserialization

1. If the current value is 'x',
   return None.

2. Create a new node.

3. Recursively build the left subtree.

4. Recursively build the right subtree.

5. Return the constructed node.

Pattern:
Tree Traversal (Preorder) + Recursion

Time Complexity:
O(n)

Space Complexity:
O(n)

Where:
n = number of nodes
'''