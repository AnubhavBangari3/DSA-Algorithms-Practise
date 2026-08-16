'''
100. Same Tree
Solved
Easy
Topics
premium lock iconCompanies

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false

 

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

1. Use **DFS with recursion** to compare both trees simultaneously.
2. If both nodes are `None`:
   - They match, so return `True`.
3. If both nodes exist:
   - Compare their values.
   - Recursively compare their left subtrees.
   - Recursively compare their right subtrees.
4. If one node exists and the other is `None`:
   - The structure is different, so return `False`.
5. The trees are the same only if both their **structure and values** match.

'''

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
Complexity
Time Complexity: O(n)
Every node is compared once.
Space Complexity: O(h)
Recursion stack depends on tree height.
Balanced tree: O(log n)
Skewed tree: O(n)

'''