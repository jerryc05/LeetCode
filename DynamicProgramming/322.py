class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        #     |              |- [dp[amount]] shall be valid
        #     |- cannot have more than [amount] coins; [amount+1] must be more than enough

        for c in coins:
            if c < len(dp):
                dp[c] = 1

        for a in range(amount + 1):
            for c in coins:
                if c < a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1


f = Solution().coinChange


print(f([1, 2, 5], 11))
print(f([2], 3))
print(f([1, 2, 5], 0))
print(f([186, 419, 83, 408], 6249))
print(f([346, 29, 395, 188, 155, 109], 9401))
