# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        level = []
        level_val = []

        while queue:
            cur = queue.popleft()
            if cur:
                level_val.append(cur.val)
                level.extend([cur.left, cur.right])
            if not queue and level:
                queue.extend(level)
                res.append(level_val)
                level = []
                level_val = []

        return res