class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        interval = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            
            while len(stack) != 0 and (stack[-1][0] < num):
                pop_num = stack.pop()
                interval[pop_num[1]] = i - pop_num[1]

            if len(stack) == 0 or stack[-1][0] >= num:
                stack.append((num,i))

        return interval