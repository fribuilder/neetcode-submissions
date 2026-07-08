# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        if not cur:
            return None
        else:
            right = cur.right
            cur.right = cur.left
            cur.left = right
        self.invertTree(cur.left)
        self.invertTree(cur.right)
        return root