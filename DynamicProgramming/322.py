from itertools import chain


class Solution:
    dp: 'list[list[int]]|None' = None  # [coins, amount]
    coins: 'list[int]|None' = None

    def coinChange(self, coins: list[int], amount: int) -> int:
        self.dp = [[-2 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        self.coins = coins
        return self.f(0, amount)

    # def f(self, coin_i: int, amount: int) -> int:
    #     dp = self.dp
    #     coins = self.coins
    #     assert dp and coins

    #     if amount == 0:
    #         return 1 if coin_i == len(coins) else 0
    #     if amount < 0 or coin_i >= len(coins):
    #         return -1

    #     if dp[coin_i][amount] == -2:
    #         print(f'f({coin_i}, {amount})')

    #         num_coins = tuple(
    #             filter(
    #                 lambda x: x >= 0,
    #                 chain(
    #                     (self.f(i, amount - coins[i]) for i in range(len(coins))),
    #                     (self.f(i + 1, amount - coins[i]) for i in range(len(coins))),
    #                 ),
    #             )
    #         )

    #         dp[coin_i][amount] = -1
    #         if num_coins:
    #             dp[coin_i][amount] = min(num_coins)+1

    #     return dp[coin_i][amount]


f = Solution().coinChange


# print(f([1, 2, 5], 11))
# print(f([2], 3))
# print(f([1, 2, 5], 0))
# print(f([186, 419, 83, 408], 6249))
print(f([346,29,395,188,155,109],9401))
