class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_time(piles, s):
            return sum([math.ceil(piles[i] / s) for i in range(len(piles))])

        l = max(sum(piles) // h, 1)
        r = max(piles)

        while l < r:
            mid = l + (r - l) // 2
            hour = cal_time(piles, mid)
            if hour > h:
                l = mid + 1
            if hour <= h:
                r = mid
        
        return r

