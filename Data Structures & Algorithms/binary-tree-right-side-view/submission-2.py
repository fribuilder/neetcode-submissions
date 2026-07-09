# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        ans = []
        l = []

        while q:
            cur = q.popleft()
            if cur.left:
                l.append(cur.left)
            if cur.right:
                l.append(cur.right)

            if not q:
                ans.append(cur.val)
                q = deque(l)
                l = []
        
        return ans