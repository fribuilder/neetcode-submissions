class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False 

        dict_num = {}
        for num in nums:
            dict_num[num] = dict_num.get(num,0) + 1
        if max(dict_num.values()) > 1:
            return True
        else:
            return False