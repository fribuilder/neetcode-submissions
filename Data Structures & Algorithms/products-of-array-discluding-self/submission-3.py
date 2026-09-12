class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        prod = 1
        for num in nums:
            left.append(prod)
            prod = prod * num

        prod = 1
        for num in nums[::-1]:
            right.append(prod)
            prod = prod * num
        
        return [left[i] * right[len(nums) - i - 1] for i in range(len(nums))]