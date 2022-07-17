class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # dp = [-1] * (amount + 1)

        # def f(amount: int, coin_i: int) -> int:
        #     if amount == 0:
        #         return 1
        #     if amount < 0 or coin_i >= len(coins):
        #         return 0

        #     if dp[amount] == -1:
        #         dp[amount] = sum(
        #             f(amount - i * coins[coin_i], coin_i + 1)
        #             for i in range(amount // coins[coin_i] + 1)
        #         )

        #     print(f'f({amount}, {coin_i}) = {dp[amount]}')
        #     return dp[amount]

        # return f(amount, 0)


g = Solution().change


print(g(5, [1, 2, ]))
# print(g(3, [2]))
# print(g(10, [10]))
# print(g(11, [10, 7, 1]))
# print(g(500, [3, 5, 7, 8, 9, 10, 11]))
