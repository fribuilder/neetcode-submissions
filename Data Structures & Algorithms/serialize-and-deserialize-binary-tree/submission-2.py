# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append('N/A')
            else:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        start = 0

        def preorder(data):
            nonlocal start
            if start < len(data):
                if data[start] == 'N/A':
                    start += 1
                    return None
                else:
                    node = TreeNode(int(data[start]))
                    start += 1
                    node.left = preorder(data)
                    node.right = preorder(data)

                return node
            else:
                return None
        return preorder(data)