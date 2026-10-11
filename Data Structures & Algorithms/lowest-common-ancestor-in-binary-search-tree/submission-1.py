class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans = -1
        cur_depth = float('inf')
        def contain(root, p , q):
            nonlocal ans, cur_depth

            if root:
                left_contain = contain(root.left, p, q)  
                right_contain = contain(root.right, p, q)
                contain_p = root == p or left_contain[0] or right_contain[0]
                contain_q = root == q or left_contain[1] or right_contain[1]
                depth = 1 + max(left_contain[2], right_contain[2])
            else:
                return False, False, 0
            if contain_p and contain_q and depth < cur_depth:
                ans = root
                cur_depth = depth
            return contain_p, contain_q, depth
        
        contain(root, p, q)
        return ans
            
