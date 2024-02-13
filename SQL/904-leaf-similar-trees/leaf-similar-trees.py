# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf1=[]
        self.leaf2=[]

        def inorder(node,values):
            if not node:
                return
            if node.left is None and node.right is None:
                values.append(node.val)
            inorder(node.left,values)
            inorder(node.right,values)
        inorder(root1,self.leaf1)
        inorder(root2,self.leaf2)

        if self.leaf1==self.leaf2:
            return True
        return False

        # Time Complexity O(n)
        # Space Complexity O(n)


        