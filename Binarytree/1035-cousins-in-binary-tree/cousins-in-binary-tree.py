# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_info=(-1,None) # Depth,Parent
        self.y_info=(-1,None)

        def dfs(node,depth,parent):
            if not node:
                return
            if node.val==x:
                self.x_info=(depth,parent)
            elif node.val==y:
                self.y_info=(depth,parent)
            
            dfs(node.left,depth+1,node)
            dfs(node.right,depth+1,node)

        dfs(root,0,None)

        return self.x_info[0]==self.y_info[0] and self.y_info[1]!=self.x_info[1]
        # Time Complexity O(n)
        # Space Complexity O(h) h is the height of the tree