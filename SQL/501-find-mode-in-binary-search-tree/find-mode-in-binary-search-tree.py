# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        f={}
        def freq(node):
            if node.val in f:
                f[node.val]+=1
            else:
                f[node.val]=1
            if node.left:
                freq(node.left)
            if node.right:
                freq(node.right)
            return f
        freq(root)
        max_value=max(f.values())
        res=[key for key,values in f.items() if values==max_value]
        return res