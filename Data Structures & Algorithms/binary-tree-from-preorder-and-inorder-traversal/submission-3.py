# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val:i for i, val in enumerate(inorder)}
        def build(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start >= preorder_end:
                return None
            root = TreeNode(preorder[preorder_start])
            root_idx = idx[preorder[preorder_start]]
            inorder_start_right = root_idx + 1
            inorder_start_left = inorder_start
            inorder_end_right = inorder_end
            inorder_end_left = root_idx
            len_inorder_left = inorder_end_left - inorder_start_left

            preorder_start_right = preorder_start + len_inorder_left + 1
            preorder_start_left = preorder_start + 1
            preorder_end_right = preorder_end
            preorder_end_left = preorder_start + len_inorder_left + 1

            root.left = build(preorder_start_left, preorder_end_left, inorder_start_left, inorder_end_left)
            root.right = build(preorder_start_right, preorder_end_right, inorder_start_right, inorder_end_right)
            return root
        
        return build(0, len(preorder), 0, len(inorder))

