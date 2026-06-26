class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def cal_forward(heights):
            stack = []
            forward_step = [0] * len(heights)
            for i, height in enumerate(heights):
                while stack and height < stack[-1][0]:
                    (num, index) = stack.pop()
                    forward_step[index] = i - index - 1
                
                stack.append((height,i))
            while stack:
                _, idx = stack.pop()
                forward_step[idx] = len(heights) - idx - 1
            return forward_step 
        
        forward_step = cal_forward(heights)
        backward_step = cal_forward(heights[::-1])[::-1]
        rectangles = [(forward_step[i]+backward_step[i]+1)*heights[i] for i in range(len(heights))]

        return max(rectangles)

                
        