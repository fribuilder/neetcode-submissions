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
        layer = []

        while q:
            node = q.popleft()
            if node.left:
                layer.append(node.left)
            if node.right:
                layer.append(node.right)
            if not q:
                ans.append(node.val)
                q.extend(layer)
                layer = []

        
        return ans