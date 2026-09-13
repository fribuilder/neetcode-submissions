class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0
        
        for p in prices:
            if p > min_p:
                profit = max(profit, p - min_p)
            if p < min_p:
                min_p = p 
        
        return profit