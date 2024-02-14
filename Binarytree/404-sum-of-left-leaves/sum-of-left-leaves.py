# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return 0

            if node.left and not node.left.left and not node.left.right:  # Check if it's a left leaf
                return node.left.val + inorder(node.right)  # Add left leaf's value and recurse for right subtree
            else:
                return inorder(node.left) + inorder(node.right)  # Recurse for both subtrees

        return inorder(root)

        # Time Complexity O(n)
        # Space Complexity O(H)

