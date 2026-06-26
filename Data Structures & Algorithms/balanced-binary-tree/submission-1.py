# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return True, 0   # balanced, height (0 for empty)

            left_bal, left_h = dfs(node.left)
            right_bal, right_h = dfs(node.right)

            height = 1 + max(left_h, right_h)
            balanced = left_bal and right_bal and abs(left_h - right_h) <= 1

            return balanced, height

        return dfs(root)[0]