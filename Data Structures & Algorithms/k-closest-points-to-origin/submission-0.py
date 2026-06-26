class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = -x ** 2 - y ** 2
            heapq.heappush(minheap, [dist,x,y])
            if len(minheap) > k:
                heapq.heappop(minheap) 

        cloest = []
        while minheap:    
            dist,x,y = heapq.heappop(minheap)
            cloest.append([x,y])
        
        return cloest 
        