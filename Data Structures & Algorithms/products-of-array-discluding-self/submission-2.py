class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        product = 1

        for i in range(n-1):
            product = product * nums[i]
            left[i+1] = product
        
        product = 1
        for i in range(n-1, 0, -1):
            product = product * nums[i]
            right[i-1] = product
        print(left,right)
        return [left[i] * right[i] for i in range(n)]
