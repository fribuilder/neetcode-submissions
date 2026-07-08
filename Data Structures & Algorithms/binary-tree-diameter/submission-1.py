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
                dia = dia_depth(cur.left)[1] + dia_depth(cur.right)[1]
                max_dia = max(dia, dia_depth(cur.left)[0], dia_depth(cur.right)[0])
                return max_dia, 1 + max(dia_depth(cur.left)[1], dia_depth(cur.right)[1])
        
        return dia_depth(root)[0]