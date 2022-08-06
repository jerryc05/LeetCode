from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # dp[i] is the smallest elem that ends a subsequence of length (i+1)
        # Monotonically increasing since that of len N must be greater than that of len (N-1)
        dp = []
        for x in nums:
            i = bisect_left(dp, x)
            if i == len(dp):
                dp.append(x)
            else:
                dp[i] = x
        return len(dp)
