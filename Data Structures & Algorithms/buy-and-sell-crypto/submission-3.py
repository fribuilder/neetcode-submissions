import numpy as np

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = [0]*len(prices)

        max_num = 0
        for i in range(len(prices)-1, -1, -1):
            max_right[i] = max_num
            max_num = max(max_num, prices[i])
        return max(max([max_right[i] - prices[i] for i in range(len(prices))]), 0)
