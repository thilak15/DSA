#class TreeNode:
    #def __init__(self, val=0, left=None, right=None):
        #self.val = val
        #self.left = left
        #self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: if the tree doesn't exist, it can't have a path sum equal to targetSum
        if not root:
            return False
        
        # Check if it's a leaf node and its value equals the remaining targetSum
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        # Recursively check the left and right subtrees with the updated target sum
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
