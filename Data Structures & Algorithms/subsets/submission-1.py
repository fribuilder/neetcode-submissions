class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        comb = []
        def backtrack(idx):
            if idx == len(nums):
                res.append(comb.copy())
                return
            comb.append(nums[idx])
            backtrack(idx + 1)
            comb.pop()
            backtrack(idx + 1)
        backtrack(0)
        return res