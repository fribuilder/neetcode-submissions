class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        heap = [-s for s in stones]
        heapq.heapify(heap)
        while heap and len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)
            if a - b != 0:
                heapq.heappush(heap, - abs(a-b))
        return 0 if not heap else - heap[0]