# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        def dfs(cur):
            if not cur:
                ans.append('N/A')
            else:
                ans.append(str(cur.val))
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)
        return ','.join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        start = 0
        def span(ans):
            nonlocal start
            if ans[start] == 'N/A':
                start += 1
                return None
            else:
                cur = TreeNode(int(ans[start]))
                start += 1
                cur.left = span(ans)
                cur.right = span(ans)

            return cur

        return span(data)
