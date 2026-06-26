class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []
        count = 0
        
        def compare(index, num_compare):
            nonlocal count

            if temperatures[index] >= temperatures[num_compare]:
                count += 1
                if num_compare + 1 == len(temperatures):
                    result.append(0)
                    count -= 1
                    return
                else:   compare(index, num_compare+1)
                count -= 1

            
            if temperatures[index] < temperatures[num_compare]:
                result.append(count)
                return

        for i in range(0,len(temperatures)):
            compare(i,i)

        return result