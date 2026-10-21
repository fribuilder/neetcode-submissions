class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        comb = []
        def backtrack(idx):
            if idx > len(nums) - 1:
                res.append(comb.copy())
                return
            comb.append(nums[idx])
            backtrack(idx + 1)
            comb.pop()
            while idx + 1 < len(nums) and nums[idx+1] == nums[idx]:
                idx += 1
            backtrack(idx + 1)
        backtrack(0)
        return res

