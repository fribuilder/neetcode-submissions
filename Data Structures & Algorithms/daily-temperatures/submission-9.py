class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((t, i))
                print(stack)
            while stack and (t > stack[-1][0]) :
                res[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
                print(stack)
            stack.append((t,i))


        return res