import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []  # store negatives (lower half)
        self.minheap = []  # store positives (upper half)

    def addNum(self, num: int) -> None:
        if not self.maxheap:
            heapq.heappush(self.maxheap, -num)
        elif not self.minheap:
            # make sure lower <= upper after inserting second element
            if num < -self.maxheap[0]:
                # move old value to minheap, put new smaller one in maxheap
                old = -heapq.heappop(self.maxheap)
                heapq.heappush(self.maxheap, -num)
                heapq.heappush(self.minheap, old)
            else:
                heapq.heappush(self.minheap, num)
        elif num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # rebalance sizes if needed
        if len(self.minheap) - len(self.maxheap) > 1:
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n)
        if len(self.minheap) - len(self.maxheap) < -1:
            n = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, n)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            if not self.maxheap:  # no numbers at all
                return 0.0
            a = -self.maxheap[0]      # use [0], do NOT pop
            b = self.minheap[0]
            return (a + b) / 2.0
        elif len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return self.minheap[0]
