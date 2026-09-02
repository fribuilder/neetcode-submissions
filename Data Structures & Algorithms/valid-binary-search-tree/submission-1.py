# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node):
            if not node:
                return True, float('-inf'), float('inf')
            else:
                is_binary_left, max_v_left, min_v_left = dfs(node.left)
                is_binary_right, max_v_right, min_v_right = dfs(node.right)
                max_v_node = max(max_v_left, max_v_right, node.val)
                min_v_node = min(min_v_left, min_v_right, node.val)
                is_binary_node = node.val > max_v_left and node.val < min_v_right and is_binary_left and is_binary_right
            return is_binary_node, max_v_node, min_v_node

        return dfs(root)[0]