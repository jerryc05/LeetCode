class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        #######################################################################
        # TC: O(N*M^2) SC: O(N*M)

        # _dp = [[0] * (amount + 1) for _ in range(len(coins))]

        # def dp(coin_i: int, amount: int):
        #     if amount == 0:
        #         return 1
        #     if coin_i < 0:
        #         return 0
        #     return _dp[coin_i][amount]

        # for coin_i, coin_info in enumerate(_dp):
        #     for am in range(1, len(coin_info)):
        #         for i in range(am // coins[coin_i] + 1):
        #             _dp[coin_i][am] += dp(coin_i - 1, am - coins[coin_i] * i)

        # return dp(len(coins) - 1, amount)

        #######################################################################
        # TC: O(N*M) SC: O(N*M)

        # NOT_PROCESSED = -1

        # dp = [[NOT_PROCESSED] * (amount + 1) for _ in range(len(coins))]

        # def f(coin_i: int, amount: int) -> int:
        #     if amount == 0:
        #         return 1
        #     if coin_i < 0 or amount < 0:
        #         return 0
        #     x = dp[coin_i][amount]
        #     if x == NOT_PROCESSED:
        #         dont_take_this_coin = f(coin_i - 1, amount)
        #         # take one of this coin type regardless of whether taken before
        #         take_this_coin_once = f(coin_i, amount - coins[coin_i])
        #         x = dp[coin_i][amount] = dont_take_this_coin + take_this_coin_once
        #     return x

        # return f(len(coins) - 1, amount)

        #######################################################################
        # TC: O(N*M) SC: O(N)

        dp = [[0] * (amount + 1) for _ in range(2)]

        for coin_info in dp:
            coin_info[0] = 1

        for i in range(1, amount // coins[0] + 1):
            dp[0][coins[0] * i] = dp[0][coins[0] * (i - 1)]

        for coin in coins[1:]:
            for amount_ in range(1, amount + 1):
                dont_take_this_coin = dp[0][amount_]
                # take one of this coin type, regardless of whether taken before
                take_this_coin_once = dp[1][amount_ - coin] if amount_ >= coin else 0
                dp[1][amount_] = dont_take_this_coin + take_this_coin_once
            dp[0] = dp[1]

        return dp[min(len(coins)-1,1)][amount]


g = Solution().change


print(
    g(
        5,
        [1, 2, 5],
    ),
    4,
)
print(g(3, [2]), 0)
print(g(10, [10]), 1)
print(g(11, [10, 7, 1]), 3)
print(g(500, [3, 5, 7, 8, 9, 10, 11]), 35502874)
