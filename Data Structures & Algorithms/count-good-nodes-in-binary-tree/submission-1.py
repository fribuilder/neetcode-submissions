# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, max_v):
            nonlocal ans

            if not node:
                return None
            else:
                if node.val >= max_v:
                    ans += 1
                    max_v = node.val
            dfs(node.left, max_v)
            dfs(node.right, max_v)
        
        dfs(root, -10e5)
        return ans