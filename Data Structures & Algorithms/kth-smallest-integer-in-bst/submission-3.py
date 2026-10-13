# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        res = 0
        def dfs(node):
            nonlocal count, res
            if node.left:
                dfs(node.left)
            if node:
                if count == k:
                    res = node.val
                count += 1
            if node.right:
                dfs(node.right)
        dfs(root)
        return res

                        