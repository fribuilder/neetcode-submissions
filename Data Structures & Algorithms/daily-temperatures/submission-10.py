class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                p = stack.pop()
                res[p[1]] = i - p[1]
                print(t, i)
            stack.append((t, i))
        return res
        