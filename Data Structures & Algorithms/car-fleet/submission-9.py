class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = [(p, s) for p,s in zip(position, speed)]
        sorted_position.sort(key = lambda x: x[0])
        times = [(target - p)/s for p,s in sorted_position]
        stack = []
        fleet = 1
        for time in times[::-1]:
            if not stack:
                stack.append(time)
            if stack and time > stack[-1]:
                fleet += 1
                stack.append(time)

        #print(sorted_position, times, stack)
        return fleet