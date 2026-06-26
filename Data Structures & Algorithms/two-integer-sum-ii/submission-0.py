class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0 
        r = n-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l = l + 1
            else: r = r -  1 
        return [l+1,r+1]

        