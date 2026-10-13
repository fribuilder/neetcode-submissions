# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def good(root, max_val):
            nonlocal res
            if root:
                if root.val >= max_val:
                    res += 1
                    max_val = root.val

                good(root.left, max_val)
                good(root.right, max_val)
        
        good(root, -float('inf'))
        return res
            