# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth =1
        self.min_depth=float('inf')
        def dfs(node,depth):
            if not node:
                return
            if node.left is None and node.right is None:
                if depth<self.min_depth:
                    self.min_depth=depth
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,depth)
        return self.min_depth

