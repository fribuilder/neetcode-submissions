class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_bd = [-1] * len(heights)
        right_bd = [len(heights)] * len(heights)

        stack = []
        for i, height in enumerate(heights):
            if not stack:
                stack.append((height, i)) 
            while stack and (height < stack[-1][0]):
                right_bd[stack[-1][1]] = i
                stack.pop()
            if not stack:
                left_bd[i] = -1
            elif height == stack[-1][0]:
                left_bd[i] = left_bd[stack[-1][1]]
            else:
                left_bd[i] = stack[-1][1]
            
            stack.append((height, i))
        print(left_bd, '\n',right_bd)
        return max([(right_bd[i] - left_bd[i] - 1) * heights[i] for i in range(len(heights))])