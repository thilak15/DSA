# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Iterative Approach Using a stack
        """if root is None:
            return True
        stack=[(root.left,root.right)]

        while stack:
            left,right=stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val!=right.val:
                return False
            stack.append((left.right,right.left))
            stack.append((left.left,right.right))

        return True"""
        # Time Complexity O(n)
        # Space Complexity O(n)
        # Recursive Approach
        def ismirrior(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val==right.val) and ismirrior(left.right,right.left) and ismirrior(left.left,right.right)
        if root is None:
            return True
        return ismirrior(root.left,root.right)   
        
        