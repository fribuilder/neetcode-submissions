class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_nums = {}

        for i, n in enumerate(nums):
            if n in diff_nums:
                return [diff_nums[n], i]
            else: diff_nums[target - n] = i