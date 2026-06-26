class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(speed: int) -> int:
            total = 0
            for p in piles:
                total += (p + speed - 1) // speed  # ceil(p / speed)
            return total

        while left < right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid  # feasible; try slower
            else:
                left = mid + 1  # too slow; speed up

        return left