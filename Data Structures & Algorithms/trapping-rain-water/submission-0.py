class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        # 1) Build left‐max array
        l_max = 0
        l_max_list = [0] * n
        for i in range(n):
            l_max_list[i] = l_max
            l_max = max(l_max, height[i])

        # 2) Build right‐max array
        r_max = 0
        r_max_list = [0] * n
        for i in range(n-1, -1, -1):
            r_max_list[i] = r_max
            r_max = max(r_max, height[i])

        # 3) Sum up trapped water at each position
        trapped = 0
        for i in range(n):
            # water level is min(maxL, maxR), minus height
            water = min(l_max_list[i], r_max_list[i]) - height[i]
            if water > 0:
                trapped += water

        return trapped