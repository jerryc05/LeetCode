class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        dp = [[int(x) for x in y] for y in matrix]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return max(max(x) for x in dp) ** 2


def test1():
    assert (
        Solution().maximalSquare(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
        == 4
    )


def test2():
    assert (
        Solution().maximalSquare(
            [
                ["0", "0", "0", "1"],
                ["1", "1", "0", "1"],
                ["1", "1", "1", "1"],
                ["0", "1", "1", "1"],
                ["0", "1", "1", "1"],
            ]
        )
        == 9
    )
