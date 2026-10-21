
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(nums):
            if not nums:
                res.append(comb.copy())
                return
            for num in nums:
                comb.append(num)
                new_nums = nums.copy()
                new_nums.remove(num)
                backtrack(new_nums)
                comb.pop()
        backtrack(nums)
        return res
