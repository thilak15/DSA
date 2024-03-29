# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+[node.val]+inorder(node.right)
        values=inorder(root)
        dummyhead=newroot=TreeNode()
        for val in values:
            newroot.right=TreeNode(val)
            newroot=newroot.right
        return dummyhead.right

        # Time Complexity O(n)
        # Space Complexity O(n)