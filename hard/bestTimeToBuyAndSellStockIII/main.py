class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        from functools import lru_cache

        n = len(prices)

        @lru_cache(None)
        def dp(i, buying, lim):
            if i == n or lim == 0:
                return 0
            if buying:
                buy = dp(i + 1, False, lim) - prices[i]
                skip = dp(i + 1, True, lim)
                return max(buy, skip)
            else:
                sell = dp(i + 1, True, lim - 1) + prices[i]
                skip = dp(i + 1, False, lim)
                return max(sell, skip)

        return dp(0, True, 2)

    def maxProfitTabulation(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[0] * (2) for _ in range(3)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(2, -1, -1):
                for k in range(2):
                    if k == 0:
                        dp[i][j][k] = max(
                            dp[i + 1][j][k + 1] - prices[i], dp[i + 1][j][k]
                        )
                    else:
                        dp[i][j][k] = max(
                            dp[i + 1][j + 1][k - 1] + prices[i] if j < 2 else 0,
                            dp[i + 1][j][k],
                        )
        return dp[0][0][0]

    def maxProfitSlatt(self, prices: list[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        profit1, profit2 = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            profit1 = max(profit1, price - t1_cost)

            t2_cost = min(t2_cost, price - profit1)
            profit2 = max(profit2, price - t2_cost)

        return profit2


print(Solution().maxProfitSlatt([3, 3, 5, 0, 0, 3, 1, 4]))
