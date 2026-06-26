class Solution:
    def rob(self, nums: List[int]) -> int:
        '''special cases'''
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[1],nums[0])
        
        dp = [0] * n #dp[i] means the most can rob before (include) house i
        
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[n-1]
