# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_count=dfs(node.left)
            right_count=dfs(node.right)

            return left_count+right_count+1
        return dfs(root)
        # Time Complexity O(n)
        # Space Complexity O(n)