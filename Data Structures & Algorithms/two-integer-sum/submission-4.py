class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        diff = set()

        for i, num in enumerate(nums):
            if num in diff:
                return [idx[target - num], i]
            else:
                diff.add(target - num)
                idx[num] = i

