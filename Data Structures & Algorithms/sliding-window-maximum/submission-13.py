class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        maxheap = [(-nums[i],i) for i in range(k)]
        heapq.heapify(maxheap)
        res = []
        res.append(-maxheap[0][0])

        while r < len(nums) - 1:
            r += 1
            l += 1
            heapq.heappush(maxheap, (-nums[r],r))
            while maxheap and maxheap[0][1] < l:
                heapq.heappop(maxheap)
            res.append(-maxheap[0][0])
        
        return res

            