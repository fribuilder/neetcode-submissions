# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        l = []
        layer = []
        ans = []

        while q:
            cur = q.popleft()
            l.append(cur.val)

            if cur.left:
                layer.append(cur.left)
            if cur.right:
                layer.append(cur.right)
            if not q:
                q = deque(layer)
                layer = []
                ans.append(l)
                l = []

        return ans