class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i, num in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i-1] == num:
                continue 
            target = - num
            start = i + 1
            end = len(sorted_nums) - 1
            while start < end:
                if sorted_nums[start] + sorted_nums[end] == target:
                    res.append([num, sorted_nums[start], sorted_nums[end]])
                    start += 1
                    end -= 1
                    while sorted_nums[start] == sorted_nums[start-1] and start < end:
                        start += 1
                elif sorted_nums[start] + sorted_nums[end] < target:
                    start += 1 
                elif sorted_nums[start] + sorted_nums[end] > target:
                    end -= 1
        
        return res