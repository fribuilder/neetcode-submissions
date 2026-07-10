# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None 
        count = 0

        def dfs(cur):
            if not cur:
                return None
            else:
                nonlocal ans, count
                dfs(cur.left)
                count += 1
                
                if count == k:
                    ans = cur.val
                
                dfs(cur.right)
        
        dfs(root)
        return ans