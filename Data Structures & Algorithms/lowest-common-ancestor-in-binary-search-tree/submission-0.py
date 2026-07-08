class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def search(cur):
            nonlocal ans

            if not cur:
                return False, False

            left_p, left_q = search(cur.left)
            right_p, right_q = search(cur.right)

            contain_p = left_p or right_p or cur.val == p.val
            contain_q = left_q or right_q or cur.val == q.val

            if ans is None and contain_p and contain_q:
                ans = cur

            return contain_p, contain_q

        search(root)
        return ans