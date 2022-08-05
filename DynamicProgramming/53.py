class Solution:
    def maxSubArray(self, nums: 'list[int]') -> int:
        if not nums:
            return 0
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)
