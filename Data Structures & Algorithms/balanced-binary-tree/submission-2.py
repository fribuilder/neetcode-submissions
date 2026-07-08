# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root):
        ans = True
        def height(cur):
            nonlocal ans

            if not cur:
                return 0
            else:
                left_height, right_height = height(cur.left),  height(cur.right)
                cur_height = max(left_height, right_height) + 1
                ans = ans and abs(left_height - right_height) < 2
            return cur_height
        height(root)

        return ans