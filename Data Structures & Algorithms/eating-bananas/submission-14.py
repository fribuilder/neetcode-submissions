class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = sum(piles) // h

        if l == 0:
            return 1
            
        while r > l:
            mid = l + (r - l) // 2
            if sum([math.ceil(float(pile) / mid) for pile in piles]) > h:
                l = mid + 1
            elif sum([math.ceil(float(pile) / mid) for pile in piles]) <= h:
                r = mid
        
        return l