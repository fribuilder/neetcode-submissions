class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = sum(piles) // h
        max_k = max(piles)

        res = 0
        while min_k <= max_k:
            mid = (max_k - min_k) // 2 + min_k
            if mid == 0:
                return 1

            time = sum([-(-pile//mid) for pile in piles]) 
            if time > h:
                min_k = mid + 1
            else:
                max_k = mid - 1
                res = mid
        return res