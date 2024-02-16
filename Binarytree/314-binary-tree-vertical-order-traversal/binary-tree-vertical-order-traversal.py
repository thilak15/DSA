# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col=defaultdict(list)
        queue=deque([(root,0)])
        while queue:
            node,k=queue.popleft()
            col[k].append(node.val)

            if node.left:
                queue.append((node.left,k-1))
            if node.right:
                queue.append((node.right,k+1))
        return [col[k] for k in sorted(col)]
        
        # The complexity is O(n+wlong(w))-> w is the width of the binary tree 
        # In a perfectly balanced tree W<<N
        #For balanced trees it will be O(n)
        # FOr unbalced trees w will be approaching n so it will be O(nlogn)
        #Space Complexiyt O(n)