class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [0] * (m + 1)
        dp[1] = 1

        for i in range(n):
            for j in range(1, m + 1):
                if obstacleGrid[i][j - 1]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
        return dp[m]
