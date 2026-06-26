class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), key = lambda x : x[0], reverse=True)
        position = [x for (x,y) in pairs]
        speed = [y for (x,y) in pairs]

        times = [(target - position[i])/speed[i] for i in range(len(position))]
        print(times)
        stack = []
        res = 1
        for time in times:
            if not stack:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
                res += 1
        
        return res