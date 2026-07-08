# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        cur = root
        if not cur:
            return 0
        else:
            depth = max(self.maxDepth(cur.left) + 1, self.maxDepth(cur.right) + 1) 
        return depth