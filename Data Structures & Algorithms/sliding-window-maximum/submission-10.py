class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k 
        res = []
        max_heap = []
        # 建第一个窗口:把前 k 个都 push 进去,不能只 push nums[0]
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        res.append(-max_heap[0][0])

        while end < len(nums):
            heapq.heappush(max_heap, (-nums[end], end))
            start = end - k + 1                    # start 要跟着动
            while max_heap[0][1] < start:          # if → while,pop(0) → heappop
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
            end += 1
        
        return res

