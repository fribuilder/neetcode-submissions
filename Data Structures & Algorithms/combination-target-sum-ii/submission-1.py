class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []
        candidates.sort()

        def backtrack(i,num_sum):
            if num_sum == target:
                res.append(subset.copy())
                return 
            elif num_sum > target:
                return 
            elif i >= len(candidates):
                return

            subset.append(candidates[i])
            num_sum += candidates[i]
            backtrack(i+1, num_sum)

            subset.pop()
            num_sum -= candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, num_sum)
            return 
        backtrack(0,0)

        return res 