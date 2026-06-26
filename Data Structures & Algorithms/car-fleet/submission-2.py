class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [target - pos for pos in position]
        time = [distance[i] / speed[i] for i in range(len(distance))]
        pairs = [(position[i], time[i]) for i in range(len(distance))]
        pairs.sort(reverse = True)

        stack = []
        fleet = 0

        for i in range(len(pairs)):
            if len(stack) == 0:
                stack.append(pairs[i])

            if pairs[i][1] > stack[-1][1]: 
                stack = [pairs[i]] 
                fleet += 1
            
            if i == len(pairs) - 1:
                fleet += 1 

        return fleet
        