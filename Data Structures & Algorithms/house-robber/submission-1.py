class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1 for _ in range(len(nums))]
        n = len(nums)

        def rob_house(nums):
            if len(nums) <= 2:
                return max(nums)
            if cache[len(nums)-1] != -1:
                return cache[len(nums)-1]
            cache[len(nums)-1] =  max(rob_house(nums[2:])+ nums[0], rob_house(nums[1:]))
            return cache[len(nums)-1]

    
        return rob_house(nums)

        