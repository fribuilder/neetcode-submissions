class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in set_num:
                length = 1
                while num + length in set_num:
                    length = length + 1
                longest = max(longest, length)
        
        return longest