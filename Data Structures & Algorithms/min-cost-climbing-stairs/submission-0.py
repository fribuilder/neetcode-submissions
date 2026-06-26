class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        new_cost = [0] + cost
        N = len(new_cost)

        cache = [-1] * (N+1)
        def claim(i):
            if i >= N:
                return 0
            elif i >= N - 2:
                return new_cost[i]
            if cache[i] != -1:
                return cache[i]
            cache[i] = min(claim(i+1)+new_cost[i], claim(i+2)+new_cost[i])  
            return cache[i]

        return claim(0)