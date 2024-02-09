# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Using Queue Data Strucutre Which increases the space cmplexity by O(n)
        if not root:
            return []
        max_values=[]
        queue=deque([root])
        while queue:
            level_size=len(queue)
            level_max=float('-inf')

            for _ in range(level_size):
                node=queue.popleft()
                level_max=max(level_max,node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_values.append(level_max)

        return max_values
        # Time complexity O(n)

        