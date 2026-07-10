# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(cur):
            if not cur:
                return 0
            else:
                nonlocal ans

                max_left = max(dfs(cur.left),0)
                max_right = max(dfs(cur.right),0)
                ans = max(cur.val + max_left + max_right, ans)
                return max(cur.val + max_left, cur.val + max_right)
            
        dfs(root)
        return ans




