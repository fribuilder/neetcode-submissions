class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dic = {}
        for num in nums:
            if num in count_dic.keys():
                return True
            else: count_dic[num] = 1
        return False 
        