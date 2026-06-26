class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_p = 0
        while r <= len(prices) - 1:
            if prices[l] < prices[r]:
                max_p = max(max_p, prices[r] - prices[l])
            else:
                l = r

            r += 1

        return max_p