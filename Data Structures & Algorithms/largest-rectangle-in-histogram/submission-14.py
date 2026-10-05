class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            if not stack:
                stack.append((height,i))
                max_area = max(max_area, height)
            idx = i
            while stack and height <= stack[-1][0]:
                higher = stack.pop()
                i = higher[1]
                max_area = max(max_area, higher[0] * (idx - higher[1]))
            stack.append((height, i))
        
        for ele in stack[::-1]:
            higher = stack.pop()
            max_area = max(max_area, higher[0] * (len(heights) - higher[1]))
        
        return max_area
