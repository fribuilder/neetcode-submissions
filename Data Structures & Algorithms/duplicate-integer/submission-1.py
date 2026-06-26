class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = set(nums)
        return len(nums_2) != len(nums)