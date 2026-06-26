class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        water = 0 
        while i < j:
            lower = min(heights[i],heights[j])
            water = max(water, lower*(j-i))
            if lower == heights[i]:
                i += 1
            else: j -= 1
        return water



        