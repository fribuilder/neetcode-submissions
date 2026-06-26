import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_l = np.inf
        min_l_list = [np.inf]*n
        profit = 0

        for i in range(n):
            min_l_list[i] = min_l
            if prices[i] < min_l:
                min_l = prices[i]

        for i in range(n):
            profit = max(profit,prices[i] - min_l_list[i])
        
        return profit         