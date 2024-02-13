class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return -1  # or some other default value indicating the root is None
        
        self.nearest = root.val  # Initialize with root's value for a valid starting point
        self.diff = abs(target - root.val)  # Initialize with the difference between target and root's value
        
        def dfs(node):
            if not node:
                return
            current_diff = abs(target - node.val)
            if current_diff < self.diff:
                self.diff = current_diff
                self.nearest = node.val
            elif current_diff==self.diff:
                if node.val<self.nearest:
                    self.nearest=node.val
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.nearest
    # Time Complexity O(n)
    # Space Complexity O(1)