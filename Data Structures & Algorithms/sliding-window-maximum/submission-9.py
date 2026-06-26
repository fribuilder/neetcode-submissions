class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        heap = []
        res = []

        for left in range(len(nums) - k + 1):
            while right - left + 1 <= k:
                heapq.heappush(heap, (-nums[right], right))
                right += 1 
                # print(heap, left, right)\
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        
        return res
