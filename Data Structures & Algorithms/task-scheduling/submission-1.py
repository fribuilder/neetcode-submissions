class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        cnt_val = {}
        for task in tasks:
            cnt_val[task] = cnt_val.get(task, 0) + 1
        max_heap = [-cnt for cnt in cnt_val.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap or q:
            time += 1
            
            if not max_heap:
                time = q[0][1]
            if max_heap:
                cnt = -heapq.heappop(max_heap) - 1
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and time == q[0][1]:
                heapq.heappush(max_heap, -q.popleft()[0])

        return time