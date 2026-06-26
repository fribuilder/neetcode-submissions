from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connect = [[] for _ in range(n)]
        time_to_reach = [inf for _ in range(n)]
        pq = []
        
        time_to_reach[k-1] = 0
        for node, time in enumerate(time_to_reach):
            heapq.heappush(pq, (time,node + 1))
        for source,target,time in times:
            connect[source-1].append([target,time])

        while pq:
            time, node = heapq.heappop(pq)
            if time > time_to_reach[node-1]:
                continue
            for target,time in connect[node-1]:
                if time_to_reach[node-1] + time < time_to_reach[target-1]:
                    time_to_reach[target-1] = time_to_reach[node-1] + time
                    heapq.heappush(pq, (time_to_reach[target-1], target))
        
        max_time = max(time_to_reach)
        if max_time == inf:
            return -1
        else: return max_time
        

        

