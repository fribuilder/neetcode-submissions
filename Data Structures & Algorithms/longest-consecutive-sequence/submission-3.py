class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        longest = 0
        for num in set_num:
            if num-1 not in set_num:
                candidate = num
                length = 1
                while candidate + 1 in set_num:
                    length += 1
                    candidate += 1
                longest = max(longest, length)
        return longest
