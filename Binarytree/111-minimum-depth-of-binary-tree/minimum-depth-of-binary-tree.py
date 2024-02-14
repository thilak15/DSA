# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """if not root:
            return 0
        depth =1
        self.min_depth=float('inf')
        def dfs(node,depth):
            if depth>=self.min_depth or node is None:
                return
            if node.left is None and node.right is None:
                if depth<self.min_depth:
                    self.min_depth=depth
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,depth)
        return self.min_depth"""
        if not root:
            return 0
        def dfs(node):
            if node is None:
                return float('inf')
            if node.left is None and node.right is None:
                return 1
            return min(dfs(node.left),dfs(node.right))+1
        return dfs(root)


