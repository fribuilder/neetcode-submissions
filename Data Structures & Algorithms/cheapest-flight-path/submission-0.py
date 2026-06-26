class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    
        INF = 10**18
        dist = [INF] * n
        dist[src] = 0

        # do k+1 relaxations -> paths using at most k+1 edges
        for _ in range(k + 1):
            new_dist = dist[:]  # freeze previous round
            for u, v, w in flights:
                if dist[u] == INF:
                    continue
                if dist[u] + w < new_dist[v]:
                    new_dist[v] = dist[u] + w
            dist = new_dist

        return -1 if dist[dst] == INF else dist[dst]

