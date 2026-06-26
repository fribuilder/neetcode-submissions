# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def cal_depth(depth, root):
            if not root:
                return 0 

            depth = max(depth + cal_depth(depth, root.left) + 1 , depth + cal_depth(depth, root.right) + 1)
            return depth 

        return cal_depth(0,root)
        