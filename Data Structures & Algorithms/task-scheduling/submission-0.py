class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency = {}
        for task in tasks:
            frequency[task] = frequency.get(task,0) + 1

        minheap = []
        for key, value in frequency.items():
            heapq.heappush(minheap, -value)

        time = 0
        queue = []
        while len(minheap) > 0 or queue:
            time += 1

            while queue and queue[0][1] < time:
                freq, availabe_time = queue.pop(0)
                heapq.heappush(minheap, freq)
            
            if len(minheap) > 0:
                freq = heapq.heappop(minheap)
                if freq < -1:
                    queue.append([freq + 1, time + n])
            
        return time


