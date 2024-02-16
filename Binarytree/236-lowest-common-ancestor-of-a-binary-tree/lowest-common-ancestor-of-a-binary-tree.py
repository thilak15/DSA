# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def common(node,p,q):
            if not node or node is p or node is q:
                return node
            left=common(node.left,p,q)
            right=common(node.right,p,q)

            if left and right:
                return node
            return left if left else right
        return common(root,p,q)
    # Time Complexity O(n)
    # Space Complexity O(n)