# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            length = len(queue)
            level = []
            for i in range(length):
                cur = queue.popleft()
                if cur:
                    if not queue:
                        res.append(cur.val)
                    if cur.left:
                        level.append(cur.left)
                    if cur.right:
                        level.append(cur.right)
            queue.extend(level)
            print(queue)
        
        return res