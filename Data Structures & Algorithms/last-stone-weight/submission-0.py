class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-s for s in stones]
        heapq.heapify(negative_stones)
        while len(negative_stones) > 1:
            a = -heapq.heappop(negative_stones)
            b = -heapq.heappop(negative_stones)
            if a > b:
                heapq.heappush(negative_stones, -(a-b))
            
        heapq.heappush(negative_stones, 0)
        return -negative_stones[0]
        