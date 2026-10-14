# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')
        def path_sum(root):
            nonlocal max_path
            if not root:
                return 0, 0
            
            left_val = root.left.val if root.left else 0
            right_val = root.right.val if root.right else 0

            left_node_left_path, left_node_right_path = path_sum(root.left)
            right_node_left_path, right_node_right_path = path_sum(root.right)

            cur_left_path = left_val + max(left_node_left_path, left_node_right_path, 0)
            cur_right_path = right_val + max(right_node_left_path, right_node_right_path, 0)

            cur_max_path = root.val + max(cur_left_path, 0) + max(cur_right_path, 0)
            max_path = max(cur_max_path, max_path)

            return cur_left_path, cur_right_path
        
        path_sum(root)
        return max_path