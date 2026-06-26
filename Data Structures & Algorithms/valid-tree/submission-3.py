class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        connect = [[] for _ in range(n)]
        for start, end in edges: 
            connect[start].append(end)
            connect[end].append(start)

        visit = set()
        def dfs(node, pre):
            if node in visit:
                return False
            
            visit.add(node)
            for adj in connect[node]:
                if adj == pre:
                    continue
                if dfs(adj, node) == False:
                    return False
                
            return True
        
        return dfs(0,-1) and len(visit) == n
