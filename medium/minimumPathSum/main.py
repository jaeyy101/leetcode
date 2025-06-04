class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [float("inf")] * (m + 1)
        dp[1] = 0

        for i in range(n):
            for j in range(1, m + 1):
                dp[j] = grid[i][j - 1] + min(dp[j - 1], dp[j])
        return dp[m]
