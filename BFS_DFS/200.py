class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        visited = [[False] * len(x) for x in grid]
        count = 0

        def dfs(i: int, j: int):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                if (
                    0 <= i < len(grid)
                    and 0 <= j < len(grid[i])
                    and grid[i][j] == '1'
                    and not visited[i][j]
                ):
                    visited[i][j] = True
                    stack.append((i + 1, j))
                    stack.append((i - 1, j))
                    stack.append((i, j + 1))
                    stack.append((i, j - 1))

        for i, grid_i in enumerate(grid):
            for j, grid_i_j in enumerate(grid_i):
                if visited[i][j]:
                    continue
                if grid_i_j == '1':
                    count += 1
                    dfs(i, j)

        return count


def test1():
    assert (
        Solution().numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )


def test2():
    assert (
        Solution().numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
