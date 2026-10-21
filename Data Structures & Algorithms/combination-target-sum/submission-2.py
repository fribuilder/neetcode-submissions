class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def backtrack(idx):
            if idx > len(nums) - 1 and sum(comb) != target:
                return 
            elif sum(comb) > target:
                return
            elif sum(comb) == target:
                res.append(comb.copy())
                return
            
            comb.append(nums[idx])
            backtrack(idx)
            comb.pop()
            backtrack(idx + 1)
        backtrack(0)
        return res