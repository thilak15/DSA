# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node,path):
            if node is None:
                return []
            path +=str(node.val)+"->"
            if node.left is None and node.right is None:
                paths.append(path[:-2])
                return
            dfs(node.left,path)
            dfs(node.right,path)
        paths=[]
        dfs(root,"")
        return paths
        # Time Complexity O(n)
        # Space Complexity O(n)


