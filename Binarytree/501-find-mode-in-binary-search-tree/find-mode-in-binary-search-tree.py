# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """f={}
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
        return res"""
        # Time complexity O(n)
        # Space Complexity O(n)
        if not root:
            return []
        self.current_count=0
        self.max_count=0
        self.current_val=None
        self.modes=[]

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            update(node.val)
            inorder(node.right)
        def update(val):
            if self.current_val!=val:
                self.current_val=val
                self.current_count=0
            self.current_count+=1

            if self.current_count>self.max_count:
                self.max_count=self.current_count
                self.modes=[val]
            elif self.current_count==self.max_count:
                self.modes.append(val)
        inorder(root)
        return self.modes
        # In this approach we are taking the non decreasing traversal of in order traversal 
        # Time complexity O(n)
        # Space Complexity O(1)
            
