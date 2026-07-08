# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        def dia_depth(cur):
            if not cur:
                return 0, 0
            else:
                left_max, left_depth = dia_depth(cur.left)
                right_max, right_depth = dia_depth(cur.right)
                dia = left_depth + right_depth
                max_dia = max(dia, left_max, right_max)
                return max_dia, 1 + max(left_depth, right_depth)
        
        return dia_depth(root)[0]