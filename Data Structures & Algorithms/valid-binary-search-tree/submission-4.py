# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if node:
                left_min, left_max = dfs(node.left)
                right_min, right_max = dfs(node.right)
                if not(node.val > left_max and node.val < right_min):
                    res = False
                return min(node.val, left_min, right_min), max(node.val, left_max, right_max)
        
            else:
                return float('inf'), -float('inf')

        dfs(root)
        return res 