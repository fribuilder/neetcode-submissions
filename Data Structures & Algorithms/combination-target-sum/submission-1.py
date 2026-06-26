class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        subset_sum = 0

        def backtrack(i):
            nonlocal subset_sum   # 🔴 required

            if subset_sum == target:
                res.append(subset.copy())
                return
            if subset_sum > target:
                return 
            if i == len(nums):
                return

            subset.append(nums[i])
            subset_sum += nums[i]
            backtrack(i)          # reuse nums[i]
            subset.pop()
            subset_sum -= nums[i]
            backtrack(i + 1)      # skip nums[i]

        backtrack(0)
        return res

        