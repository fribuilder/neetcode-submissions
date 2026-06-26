class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0

        for _ in range(k+1):
            new_dist = dist[:]
            for u,v,w in flights:
                if dist[u] != INF:
                    new_dist[v] = min(new_dist[v], dist[u] + w)
            dist = new_dist[:]
        
        return dist[dst] if dist[dst] != INF else -1

