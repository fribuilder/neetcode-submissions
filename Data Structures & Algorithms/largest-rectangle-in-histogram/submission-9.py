class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            if not stack:
                stack.append((i, height))

            else:
                start = i
                while stack and height < stack[-1][1]:
                    index, h = stack.pop()
                    start = index
                    max_area = max(max_area, h * (i - start))
                stack.append((start, height))
        
        print(stack)
        
        for start, height in stack:
            max_area =  max(max_area, height * (len(heights) - start))
        
        return max_area