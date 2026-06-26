class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            if sum(subset) > target:
                return 
            if i == len(nums):
                return

            subset.append(nums[i])
            backtrack(i)
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return res
        