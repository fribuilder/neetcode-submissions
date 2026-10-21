class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        def backtrack(idx, sum_comb):
            if sum_comb == target:
                res.append(comb.copy())
                return
            if idx > len(candidates) - 1 or sum_comb > target:
                return
            
            comb.append(candidates[idx])
            backtrack(idx + 1, sum_comb + candidates[idx])
            comb.pop()
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            backtrack(idx + 1, sum_comb)

        backtrack(0,0)
        return res