class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while i < j - 1:
            if nums[(i+j)//2] >= target:
                j = (i+j)//2
            else: i = (i+j)//2
        
        if nums[j] == target:
            return j
        elif nums[i] == target: 
            return i
        else: return -1
        