class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_diff = {}
        for i in range(len(nums)):
            dict_diff[target - nums[i]] = i

        for i in range(len(nums)):
            if (nums[i] in dict_diff):
                if i != dict_diff[nums[i]]:
                    return [i, dict_diff[nums[i]]]

        