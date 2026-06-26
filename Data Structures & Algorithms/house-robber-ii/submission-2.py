class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        numsCase1 = nums[2:n-1]
        numsCase2 = nums[1:]

        def rub_house(nums):
            if len(nums) <= 2:
                return max(nums)
            if cache[len(nums) - 1] != -1:
                return cache[len(nums) - 1]
            cache[len(nums) -1] = max(rub_house(nums[2:])+nums[0], rub_house(nums[1:]))
            return cache[len(nums) - 1] 

        cache = [-1 for _ in range(len(numsCase1))]
        n1 = len(cache)
        if numsCase1:
            case1 = rub_house(numsCase1) + nums[0]
        else: case1 = nums[0]

        cache = [-1 for _ in range(len(numsCase2))]
        n1 = len(cache)
        if numsCase2:
            case2 = rub_house(numsCase2)
        else: case2 = 0
        
        return max(case1, case2)