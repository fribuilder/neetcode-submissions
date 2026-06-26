class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        consective = 1
        longest = 1
        if len(nums) == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i] - 1:
                consective += 1
                if (consective > longest):
                    longest = consective
            elif  nums[i-1] == nums[i]:
                continue
            else:  consective = 1



        return longest
