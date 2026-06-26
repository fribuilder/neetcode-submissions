# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            # returns (height, diameter) for subtree
            if not node:
                return -1, 0  # height=-1 so leaf becomes 0
            
            hL, dL = dfs(node.left)
            hR, dR = dfs(node.right)

            height = 1 + max(hL, hR)
            through = hL + hR + 2
            diameter = max(dL, dR, through)

            return height, diameter
        
        return dfs(root)[1]
        